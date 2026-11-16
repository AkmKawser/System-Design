# Template Blueprint Specification: Networking

Custom structural blueprints and section standards for **Networking for Systems & Distributed Architecture**.

## Standard Note Schema
1. **Executive Summary & Scope**
2. **Layer Models**: The OSI 7-Layer & TCP/IP 4-Layer Architecture
3. **Layer 2 (Data Link) & Physical Invariants**: MAC Addressing, Ethernet Framing, ARP, Switches vs. Hubs
4. **Layer 3 (Network Layer) Architecture**: IPv4 vs. IPv6, CIDR Subnetting, NAT, ICMP, Routing Protocols (BGP, OSPF)
5. **Layer 4 (Transport Layer) Deep Dive**: TCP (3-Way Handshake, Flow Control, Congestion Control, TIME_WAIT) vs. UDP vs. QUIC
6. **Layer 7 (Application Layer) & Network Services**: DNS Resolution, TLS 1.3 Encryption, HTTP/1.1 to HTTP/3
7. **Operating System & Kernel Networking**: BSD Sockets, Kernel Ring Buffers, I/O Multiplexing (`epoll`, `kqueue`, `io_uring`)
8. **Cloud & Enterprise Network Topologies**: VPCs, Subnets, Gateways, Overlay Networks (VXLAN), L4/L7 Load Balancing
9. **Network Security & Defense**: Firewalls, WAF, DDoS Mitigation (SYN floods, UDP reflection), mTLS, VPNs
10. **Troubleshooting & Observability**: Packet capture (`tcpdump`, Wireshark), diagnostics (`ping`, `traceroute`, `ss`, `dig`)
