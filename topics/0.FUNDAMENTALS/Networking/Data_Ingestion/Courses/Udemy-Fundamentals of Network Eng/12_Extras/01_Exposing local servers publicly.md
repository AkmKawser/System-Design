#### Exposing local servers publicly

#### How does it REALLY work

When you build a local web server listening on a private ip on LAN, only hosts from the same network can access it. Simple networking. Your local network can access outside hosts (thanks to NAT) but outside host can’t directly access it without specific routing logic. A common requirement is exposing this local webserver so it can be accessed from anywhere.

[SSH tunneling](https://youtu.be/N8f5zv9UUMI) and [ngrok](https://youtu.be/pR2qNnVIuKE) are example of services that allow you to do that. In this post I explain the networking weeds behind how this works.

#### Public vs Private

When an IP address is routable through the Internet it is called a public IP address. When you create a listener on a public ip address that is routable, clients from anywhere, as long there is a valid BGP route to it, can reach it. When a listener is on a private address no one but hosts in that network can reach it. The known private networks are 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16. And yes this also include localhosts 127.0.0.1 or ::1.

So if my server is listening on 10.0.0.2 or 127.0.0.1 or 192.168.0.2 or 172.16.0.13 no one from the Internet can reach it. However, my private machine can connect to any host on the Internet thanks to NAT (network address translation). My router translates the private ip address to its public ip address with a unique source port to identify my machine. As far as the public services go they only see my router’s public ip, they don’t really know if a host from a private network is trying to access their services.

With that knowledge in mind what tricks can we play to make hosts outside the private network access my local server?

#### Static Port Forwarding

While true your web server is on a private network, your router usually have a public reachable ip address. You can add a port forwarding rule on your router such that if any one attempts to connect (send a SYN) to the router public ip address on port 8080, you let the router pass it to a hardcoded private ip address in your network. This trick works but require admin permissions to the router to add the rule.

So on to the second trick that most services use.

#### Remote Port Forwarding

If we have a server on the public Internet (e.g. on AWS ) under our control we can remotely command it to forward packets on a specific port to us on the local service. The problem is that public server is on the Internet so it can’t access our local server to forward us connections. For that we flip the game, we connect to it instead.

To explain how it works, we need to introduce two new components the public agent and the local agent. The public agent runs on the same network as the public server could be same host or different. The local agent runs in the same network as the local server, again same host or different.

#### 1) The local agent connects to the public agent

This connection is the bridge that links the two agents, we will create our own protocol to send “commands” to instruct public agent to do stuff for us. It will also be used to transmit requests and responses.

#### 2) The local agent commands public agent to listen on a port

Since we are building both the local and public agents, we can add specific commands to achieve our goal. The local agent can send a command to make the public agent listen on a port.

#### 3) The local agent commands public agent to link listen port to its address

The local agent sends another command to instruct the public agent that connections attempts and data sent on that port to be forwarded to local agent as is. But we need more context, so the local agent tells the the public agent the private address and port.

#### 4) A new connection attempt to public agent

New connections to the public agent port will be completed with clients normally. Each client that connects will have a unique source ip and source port and we will use this to uniquely identify the connection to the public agent.

Once the connection is established between client and public agent, the public agent will send a command to the local agent to create a brand new connection to the local service for the client that just connected. This is critical to map that local connection to the public agent remote connection.

#### 5) Client sends data (request) to public agent on connection

Now that we have a connection between a client and the public agent, the client can send its first data, this could be a TLS client hello or whatever protocol is on that connection (HTTP GET). That data is buffered on the public agent as normal and acknowledged. The public agent knows that this particular port, client address and client port is linked with a specific local agent port and address. So the data request is sent on the bridge connection with a special header, this header tells the local agent exactly what local connection to use based on the private ip port of the service and the client port and address. The local agent writes that data to the local connection.

#### 6) Local server response

We did a request, now we need to do a response. The local service responds to the local agent with data (because that is where the local connection is created from), the local agent knows that this local service connection port/ip is mapped to a specific public agent port and to a specific client ip/port so it takes the content and writes it to public agent bridge connection with a special header so that public agent knows which remote connection to write that data to.

> Think of these IP/ports are used are look ups. We could have built the protocol to generate unique UUID identifiers instead.

What we just demonstrated is a very similar concept to how SSH reverse tunneling or remote port forwarding. The connection between the public and local agent is the tunnel. I didn’t want to mention it at the start because your mind will be hooked to SSH and its concepts and I want to illustrate this free of pre-conceived protocols. Learn that we can build things ourselves, learn how things work. Make it better.

> I really don’t prefer using the word tunnel when used in networking, it never resonates with my understanding (just like write-ahead log), but it is used everywhere so I mention it for completeness. I like to use the bare terms, it is just another connection. A bridge if you will.

Worth mentioning also that SSH supports Local Port Forwarding which allows your local client to access hosts in a private network that a public agent also lives in. So the public agent has a public IP and it also has a private IP, using the public IP you can connect to the public agent, and then the public agent using the private network it can connect to the final private host. Useful to access a machine at work when there a public SSH server exposed. It is all the same logic though.

To do a local port forwarding in SSH

```

ssh -L local_port:remote_address:remote_port username@sshserver
```

To do a remote port forwarding in SSH

```
ssh -R remote_port:local_address:local_port username@sshserver
```

> P.s. For Remote Port forwarding the ssh server config /etc/ssh/sshd_config should have a property GatewayPorts yes

#### Take it further

With this approach you create many listeners, one for each service that you want to expose. Each client has an end-to-end session to the local service. If the connection is encrypted with TLS both the public and local agents can’t really see anything being transmitted. Only the local service and the client can. It is pure end-to-end layer 4 tunneling is you wish.

However, is it possible to have everything be done on a single port and use a higher level application concept to identify the service? Yes! We can use domains, subdomains or HTTP paths. Think of how you can augment the protocol to do just that. When you do so you will be building a layer 7 tunnel essentially where requests are decrypted and understood by the public agent, cached, changed, and forwarded to the local service. This is how ngrok does it.

Example, service1.husseinnasser.com maps to a local service on port 8888 while service2.husseinnasser.com maps to another local service on port 9999