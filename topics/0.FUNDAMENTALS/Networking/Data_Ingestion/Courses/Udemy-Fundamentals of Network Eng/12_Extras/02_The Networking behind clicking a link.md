When you click on a hyperlink, your browser loads the link’s content from a remote server and renders it. Behind the scenes much is happening including, connection establishement, session encryption, protocol negotiation, redirection, domain indication and much more.

In this article I’ll walk you through the networking aspects of clicking a hyperlink on your browser. I’ll be using one of my course links for demonstration purposes.

All mentions of*the client* in the article refer to a browser that supports TLS 1.3 and HTTP/2. All modern browsers support these protocols in 2022.

#### backend.husseinnasser.com

Each of my software engineering courses has a CNAME record my DNS provider hosts that points to a unique Netlify domain. On Netlify, I host an HTML page that redirects to the actual course link. This way I can share the CNAME domain on my socials while having full control to update the course coupons or redirect to a completely different link in case I decided to switch course management systems. The original link remains the same.

Let us take my latest course Fundamentals of Backend communications, Design patterns and protocols hosted on *backend.husseinnasser.com.*Clicking the link redirects the browser to my course on udemy, the process goes through DNS, TCP, TLS, ALPN/SNI and HTTP/2, I detail each section below.

```
backend.husseinnasser.com ---> zen-mccarthy-34c0bb.netlify.app ---> udemy.com/backendcourse
```

#### DNS

When you click on https://backend.husseinnasser.com, the HTTP client (your browser) issues a DNS lookup for *backend.husseinnasser.com* to get the IP address. *backend.husseinnasser.com* is a CNAME (canonical name) hosted on my DNS authoritative name server *enom* that points to a Netlify DNS record *zen-mccarthy-34c0b.netlify.app* where my HTML file is hosted.

> *This means you can visit zen-mccarthy-34c0b.netlify.app on your browser and will also take you to my course.*

The DNS query is a UDP datagram with a unique queryId that aks for the IP address of *backend.husseinnasser.com.*Thefirst stop of the DNS query is your DNS recursor (or resolver), this could be Google *8.8.8.8* or Cloudflare’s *1.1.1.1*for example. The recursor asks the ROOT DNS servers for a *.com* top level domain server (TLD) server. The recursor then send a query to a TLD asking for the authorative name server where *husseinnasser.com* is hosted which returns one of my *enom* servers. Finally the recursor sends the DNS query *backend.husseinnasser.com* to an *enom* server to get the IP address. It discovers that it is a CNAME that points *zen-mccarthy-34c0bb.netlify.app* so it does the a new DNS query to find out the IP address of *zen-mccarthy-34c0bb.netlify.app*and the process is repeated until an IP address is discovered. This is all assumes no caching.

> *A slight difference in terminology between a DNS lookup and DNS resolve. DNS lookup in OS speak means it will try to look-up the IP, this involves checking local caches, hosts file and finally making a network call to resolve. The DNS resolve is just the final part, going through the network to do DNS.*[*getaddrinfo*](https://man7.org/linux/man-pages/man3/getaddrinfo.3.html)*is the linux function that does the lookup one reason why this function is*[*synchronous*](https://medium.com/@hnasr/when-nodejs-i-o-blocks-327f8a36fbd4)*.*

We can see this by doing an nslookup (or dig) to the domain.

As part of the DNS query where we got the zen-mccarthy domain, we also get two A records associated with IPv4 address for zen-mccarthy netlify domain. The client will pick one IP and establish a TCP connection is established to 35.247.66.204.

> *DNS can be configured to return multiple A records IP addresses. Round-robin DNS change the order of the returned A records so that clients can distribute connections on different IP addresses. This is so traditional clients who always picks the first IP doesn’t overload that particular service. Of course, nice tricks can be applied at the client level to force what I refer to as client side load balancing.*

#### TCP

Now that we have an IP address we can actually establish the TCP connection. Establishing TCP connection requires 4 tuples, source IP, source port, destination IP and destination Port. The client needs all four before it can connect.

The client knows the destination IP thanks to DNS, its *35.247.66.204* , the destination port is 443 since the link explicitly says *https://*The source port can be any available port between 0–2¹⁶ and the source IP is your machine.

> *While the source IP might normally start as the machine private IP address, it changes to the gateway’s public IP address before it leaves private network, a process called NAT or Network address translation. The source port also changes and an entry is added to the NAT table to remember what the change was made so the gateway knows how to forward the packets back to the original machine.*

With the 4 tuples, the client sends a SYN TCP segment carried in an IP packet, the server gets the SYN and replies back with SYN/ACK changing the destination IP to the client’s IP (gateway more likely) and finally the client finishes the handshake with the ACK. We now have a connection.

> *Technically speaking the connection establishment at the server side is done by whatever kernel OS is running on the server 35.247.66.204 on port 443. Two queues are allocated when the backend application listens on a port/address, SYN queue and the ACCEPT queue. The SYN queue holds the incomplete SYN until the final matching ACK comes back from the client where a connection is created and is moved to Accept queue. The connection waits in the Accept queue until the backend application calls accept() to create a file descriptor and read the data.*

```
Client ------------SYN -------> netlify (35.247.66.204)       <---------SYN/ACK------       ------------ACK-------->
```

#### TLS

Any data sent on the TCP connection at its current state is plain text and can be observed by anyone intercepting traffic. That is why the communication is encrypted to ensure security (the S in HTTPS).

Our protocol of choice for encryption is [TLS](https://medium.com/@hnasr/the-many-configurations-of-https-4fa005a456ad) or Transport layer security. The main part of TLS is the handshake which its main goals are :

- Exchange a symmetric key that can be used for encryption
- Negotiate application protocols
- Indicate and Authenticate the server

The client sends a TLS client hello message to initiate the TLS handshake, requesting session encryption and proposing both HTTP/1.1 and HTTP/2 in the process. The server replies back with a server hello message to complete the TLS handshake.

```
Client ------------SYN -------> netlify (35.247.66.204)       <---------SYN/ACK------       ------------ACK-------->       ------Client Hello ---->        <-----Server Hello------
```

The client sets many TLS extensions as part of its client hello message, we are interested in two in particular. The first is ALPN which stands for application layer protocol negotiation and the second is SNI which stands for Server name indication. Let us explain their purpose.

> *The client proposes both TLS protocol versions TLS 1.3 and TLS 1.2 but it doesn’t really know (yet) what protocol the server will accept. If the server chooses TLS 1.3 the handshake finishes in one round trip, else, the handshake takes two round trips. We assume TLS 1.3 here because we know Netlify is on TLS 1.3.*

#### ALPN

ALPN is a TLS extension that indicates the application protocols the client supports. The client in our case proposes both HTTP/1.1 and HTTP/2 (h1 and h2 for short) as part its ALPN and the highest protocol supported by both client and server is usually selected. The server in this case selects HTTP/2.

A trace from cURL, notice the client offers both h2 and http/1.1 and the server (last line accepted h2)

#### SNI

Probably the most important piece in the TLS handshake is SNI or server name indication. This extension indicates to the server what domain the client is interested in. This is because one IP address can host thousands of websites, and indicating the domain helps the server know exactly what website the client is interested in, so the server knows what certificate to return.

The client SNI is set to *backend.husseinnasser.com*. Netlify server receives the TLS client hello handshake and using the SNI, it knows exactly what certificate it need to serve the client back for authentication. This certificate was generated by Netlify for my domain when I linked my domain with them, the certificate authority is lets encrypt.

Let’s encrypt certificate generated for backend.husseinnasser.

The server sends the server hello to finish the TLS handshake, with the *backend.husseinnasser.com* certificate, the cipher parameters and an the application protocol of choice which is HTTP/2. Both the client and the server have the symmetric key for encryption, they are ready to encrypt and send HTTP requests.

> *Because we use TLS 1.3, the certificate among other things is encrypted since the server. The reason is the server has the symmetric key. Unlike TLS 1.2, where the server sends the certificate in plain text in the server hello because the key is not created until the second round trip. I talk about the reasoning behind this in this*[*article*](https://medium.com/@hnasr/the-many-configurations-of-https-4fa005a456ad)*.*

#### HTTP/2

We have an encrypted session on a TCP connection. Now the client can send the HTTP GET request to fetch the page. The application layer protocol of choice is HTTP/2 so the client needs an HTTP/2 stream to send the request on.

Since it is a new connection, the client creates a new stream for the request (stream 1). The client sends the HTTP request with the method GET, the path is / since nothing is after the *backend.husseinnasser.com*, and the protocol version HTTP/2. The client sets the HTTP headers and sends the request.

Here is an example of how this looks like. Take note of the *Host* header, one of the most important HTTP headers.

> *HTTP/2 odd numbered streams are client initiated while even numbered streams are server initiated. Example of a server initiated stream is HTTP/2 push which is deprecated for reasons I go through on my course.*
>
>
>
> *gRPC takes full advantage of the HTTP/2 protocol and these streams really matter for the functionality of this protocol.*

#### The Host header

Without the host header, the whole thing breaks down. The host header was optionally added back in HTTP/1.0 to solve some challenges for web masters. Some of these challanges are:

- Enable hosting multiple websites on a single IP address
- Proxy server support

Because of that, the Host header was later made required in HTTP/1.1 and future protocols.

Take Netlify for instance, the IP 35.247.66.204 hosts thousands of websites. Many clients connects to the same IP address, but how does the Netlify server know what website the client really wants to consume. The host header is used by the server to know exactly what website to fetch. Notice that the client sets *backend.husseinnasser.com* as the host header so netlify servers can point to a copy of my github repo content and serve the HTML page from there.

The client might also send cookies header with GET request which the server use to identify the user.

In a proxy configuration, the client’s destination IP is the proxy, so we need another indication at the application layer for the proxy to know what website the client actually want to connect to.

The server receives the GET request on stream 1, and processes the GET request by looking at the host header, fetch default page index.html. Based on whether cookies are sent or not, the server writes back different HTTP response to the same stream.

> *It is important to mention that HTTP requests to the same domain will try to use an existing connection when possible. This is in order to avoid the cost of creating and encrypting new connections. In HTTP/2 request multiplexing is supported and client can send multiple concurrent requests on the same connection on different streams. In HTTP/1.1 however one connection can only serve one request at a time.*

#### Redirect to udemy

The client finally gets an HTTP response with the index.html page. The page contains a simple HTML as follows

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <meta http-equiv="refresh" content="0; URL=https://www.udemy.com/course/fundamentals-of-backend-communications-and-protocols/?couponCode=BACKEND10V2" />    <title>Fundementals of Backend Communication Design Patterns and Protocols</title></head><body>   <h1>Redirecting to udemy ...</h1>   <h2>Enjoy my Fundementals of Backend Engineering Course</h2>  </body></html>
```

Pay attention to the meta header http-equiv refresh and content=0 and the URL. This tells the browser to immediately redirect to udemy on that URL. The exact steps are repeated, as if the user clicked another link. Here are the steps:

- We DNS udemy.com, find the IP address
- Create a TCP connection
- Establish TLS
- Negotiate HTTP protocols
- Create HTTP/2 stream
- Send a new GET request where the path is*/course/fundamentals-of-backend-communications-and-protocols/?couponCode=BACKEND10V2*
- If you are logged in to udemy, cookies will be sent
- Udemy server responds back with course page based on your sign in state

The coupon code is a query parameter at the end of the url named couponCode. Every month I update the coupon and push my changes to github which triggers a Netlify rebuild. Anyone visiting backend.husseinnasser.com gets the latest coupon. In the future if I decided to switch course providers, I update the URL in index.html. The original link never changes.

#### Summary

The goal of this article is to shed light at the art of software engineering. A lot of work has been put by great engineers who designed and implemented the communication protocols that power everything on the Internet.

As a fellow engineer I feel that this work is often taken for granted and rarely acknowledged. Understanding how protocols work is the first step to contribute to the evolution of network engineering and potentionally making better protocols. You saw what it takes to achieve a simple task such as a clicking a link, the question becomes, can we make it better?

Thanks for reading.