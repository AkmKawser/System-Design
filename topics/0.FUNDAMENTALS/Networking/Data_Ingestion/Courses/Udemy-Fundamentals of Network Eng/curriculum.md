# Course Curriculum: Fundamentals of Network Engineering

> **Course Metadata**:
> - **Instructor**: Hussein Nasser
> - **Platform**: Udemy
> - **Subject**: Computer Networking, OSI Model, IP, TCP, UDP, TLS, DNS, Routing, Wireshark & Kernel Queues
> - **Ingestion Path**: [`topics/0.FUNDAMENTALS/Networking/Data_Ingestion/Courses/Udemy-Fundamentals of Network Eng/`](./)
> - **Synthesis Deliverable**: [`Networking.md`](../../output/Note_version-1_Networking/Networking.md)

---

## 📋 Course Overview & Ingestion Objectives

This course establishes the engineering foundations of computer networking from the physical and data link layers up to application transport protocols, socket programming, kernel queues, and network performance tuning.

Per `engine/engine.md` § 4.2 (*Channel 2: Courses Ingestion*), this curriculum indexes all 12 modules and 66 lecture transcripts for deterministic retrieval.

---

## 🗂️ Detailed Module Breakdown

### Section 1: Introduction (4 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **1.1** | Welcome to the course | [01_Welcome.md](01_Introduction/01_Welcome.md) |
| **1.2** | Target audience & engineering prerequisites | [02_Who is this course for.md](01_Introduction/02_Who%20is%20this%20course%20for.md) |
| **1.3** | Course outline & roadmap walkthrough | [03_Course Outline.md](01_Introduction/03_Course%20Outline.md) |
| **1.4** | Slides, resources, and companion code downloads | [04_Download Course Slides and resources here.md](01_Introduction/04_Download%20Course%20Slides%20and%20resources%20here.md) |

---

### Section 2: Fundamentals of Networking (3 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **2.1** | Client-Server architecture and physical communication models | [01_Client - Server Architecture.md](02_Fundamentals%20of%20Networking/01_Client%20-%20Server%20Architecture.md) |
| **2.2** | The OSI 7-layer model: protocol abstractions and layering | [02_OSI Model.md](02_Fundamentals%20of%20Networking/02_OSI%20Model.md) |
| **2.3** | Host-to-host communication across networks | [03_Host to Host communication.md](02_Fundamentals%20of%20Networking/03_Host%20to%20Host%20communication.md) |

---

### Section 3: Internet Protocol (IP) (7 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **3.1** | The IP building blocks: packets, headers, and routing | [01_The IP Building Blocks.md](03_Internet%20Protocol%20(IP)/01_The%20IP%20Building%20Blocks.md) |
| **3.2** | IP packet structure, TTL, fragmentation, and MTU | [02_IP Packet.md](03_Internet%20Protocol%20(IP)/02_IP%20Packet.md) |
| **3.3** | ICMP, PING, and TraceRoute: network diagnostics | [03_ICMP, PING, TraceRoute.md](03_Internet%20Protocol%20(IP)/03_ICMP,%20PING,%20TraceRoute.md) |
| **3.4** | Address Resolution Protocol (ARP): IP-to-MAC resolution | [04_ARP.md](03_Internet%20Protocol%20(IP)/04_ARP.md) |
| **3.5** | Capturing IP, ARP, and ICMP packets with `tcpdump` | [05_Capturing IP, ARP and ICMP Packets with TCPDUMP.md](03_Internet%20Protocol%20(IP)/05_Capturing%20IP,%20ARP%20and%20ICMP%20Packets%20with%20TCPDUMP.md) |
| **3.6** | Routing walkthrough: hop-by-hop packet forwarding | [06_Routing Example.md](03_Internet%20Protocol%20(IP)/06_Routing%20Example.md) |
| **3.7** | Private IP addressing (RFC 1918) & Wi-Fi isolation | [07_Private IP addresses.md](03_Internet%20Protocol%20(IP)/07_Private%20IP%20addresses%20(Alaska%20Airlines%20WIFI%20example).md) |

---

### Section 4: User Datagram Protocol (UDP) (6 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **4.1** | What is UDP: connectionless datagram transport | [01_What Is UDP.md](04_User%20Datagram%20Protocol%20(UDP)/01_What%20Is%20UDP.md) |
| **4.2** | User datagram structure: 8-byte header | [02_User Datagram Structure.md](04_User%20Datagram%20Protocol%20(UDP)/02_User%20Datagram%20Structure.md) |
| **4.3** | UDP engineering trade-offs: speed vs. reliability | [03_UDP Pros & Cons.md](04_User%20Datagram%20Protocol%20(UDP)/03_UDP%20Pros%20&%20Cons.md) |
| **4.4** | Building a UDP server in JavaScript using Node.js (`dgram`) | [04_UDP Server with Javascript using NodeJS.md](04_User%20Datagram%20Protocol%20(UDP)/04_UDP%20Server%20with%20Javascript%20using%20NodeJS.md) |
| **4.5** | Building a low-level UDP server in C using POSIX sockets | [05_UDP Server with C.md](04_User%20Datagram%20Protocol%20(UDP)/05_UDP%20Server%20with%20C.md) |
| **4.6** | Capturing UDP traffic with `tcpdump` | [06_Capturing UDP traffic with TCPDUMP.md](04_User%20Datagram%20Protocol%20(UDP)/06_Capturing%20UDP%20traffic%20with%20TCPDUMP.md) |

---

### Section 5: Transmission Control Protocol (TCP) (12 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **5.1** | What is TCP: connection-oriented reliable byte streams | [01_What is TCP.md](05_Transmission%20Control%20Protocol%20(TCP)/01_What%20is%20TCP.md) |
| **5.2** | TCP segment format: sequence numbers, ACKs, and window size | [02_TCP Segment.md](05_Transmission%20Control%20Protocol%20(TCP)/02_TCP%20Segment.md) |
| **5.3** | Flow Control: sliding window buffer management | [03_Flow Control.md](05_Transmission%20Control%20Protocol%20(TCP)/03_Flow%20Control.md) |
| **5.4** | Congestion Control: bandwidth estimation and backoff | [04_Congestion Control.md](05_Transmission%20Control%20Protocol%20(TCP)/04_Congestion%20Control.md) |
| **5.5** | Slow Start vs. Congestion Avoidance algorithms | [05_Slow Start vs Congestion Avoidance.md](05_Transmission%20Control%20Protocol%20(TCP)/05_Slow%20Start%20vs%20Congestion%20Avoidance.md) |
| **5.6** | Network Address Translation (NAT) & port forwarding | [06_NAT.md](05_Transmission%20Control%20Protocol%20(TCP)/06_NAT.md) |
| **5.7** | TCP connection states: SYN_SENT, ESTABLISHED, TIME_WAIT | [07_TCP Connection States.md](05_Transmission%20Control%20Protocol%20(TCP)/07_TCP%20Connection%20States.md) |
| **5.8** | TCP engineering trade-offs: pros and cons | [08_TCP Pros and Cons.md](05_Transmission%20Control%20Protocol%20(TCP)/08_TCP%20Pros%20and%20Cons.md) |
| **5.9** | Sockets, connections, and kernel queues (`SYN` vs. `Accept`) | [09_Sockets, Connections and Kernel Queues.md](05_Transmission%20Control%20Protocol%20(TCP)/09_Sockets,%20Connections%20and%20Kernel%20Queues.md) |
| **5.10** | TCP server in JavaScript using Node.js (`net`) | [10_TCP Server with Javascript using NodeJS.md](05_Transmission%20Control%20Protocol%20(TCP)/10_TCP%20Server%20with%20Javascript%20using%20NodeJS.md) |
| **5.11** | Low-level TCP server in C using BSD socket calls | [11_TCP Server with C.md](05_Transmission%20Control%20Protocol%20(TCP)/11_TCP%20Server%20with%20C.md) |
| **5.12** | Capturing TCP segments and handshakes with `tcpdump` | [12_Capturing TCP Segments with TCPDUMP.md](05_Transmission%20Control%20Protocol%20(TCP)/12_Capturing%20TCP%20Segments%20with%20TCPDUMP.md) |

---

### Section 6: Overview of Popular Networking Protocols (4 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **6.1** | Networking protocols introduction | [01_Networking Protocols Introduction.md](06_Overview%20of%20Popular%20Networking%20Protocols/01_Networking%20Protocols%20Introduction.md) |
| **6.2** | Domain Name System (DNS): hierarchy and resolution | [02_DNS.md](06_Overview%20of%20Popular%20Networking%20Protocols/02_DNS.md) |
| **6.3** | Transport Layer Security (TLS): asymmetric encryption | [03_TLS.md](06_Overview%20of%20Popular%20Networking%20Protocols/03_TLS.md) |
| **6.4** | HTTPS, TLS certificates, public keys, and CAs | [04_HTTPS, TLS, Keys and Certificates.md](06_Overview%20of%20Popular%20Networking%20Protocols/04_HTTPS,%20TLS,%20Keys%20and%20Certificates.md) |

---

### Section 7: Network Performance (11 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **7.1** | Network performance section overview | [01_What is this section.md](07_Network%20Performance/01_What%20is%20this%20section.md) |
| **7.2** | MSS vs. MTU vs. Path MTU Discovery (PMTUD) | [02_MSS vs MTU vs PMTUD.md](07_Network%20Performance/02_MSS%20vs%20MTU%20vs%20PMTUD.md) |
| **7.3** | Nagle's Algorithm effect on latency and packet batching | [03_Nagle's Algorithm's Effect on Performance.md](07_Network%20Performance/03_Nagle's%20Algorithm's%20Effect%20on%20Performance.md) |
| **7.4** | Delayed Acknowledgment interaction with Nagle's algorithm | [04_Delayed Acknowledgment Effect on Performance.md](07_Network%20Performance/04_Delayed%20Acknowledgment%20Effect%20on%20Performance.md) |
| **7.5** | Connection establishment latency overhead | [05_Cost of Connection Establishment.md](07_Network%20Performance/05_Cost%20of%20Connection%20Establishment.md) |
| **7.6** | TCP Fast Open (TFO): data in SYN packets | [06_TCP Fast Open.md](07_Network%20Performance/06_TCP%20Fast%20Open.md) |
| **7.7** | Listening server backlog and queue saturation | [07_Listening Server.md](07_Network%20Performance/07_Listening%20Server.md) |
| **7.8** | TCP Head-of-Line (HoL) blocking mechanics | [08_TCP Head of line blocking.md](07_Network%20Performance/08_TCP%20Head%20of%20line%20blocking.md) |
| **7.9** | Reverse proxies in network architectures | [09_The importance of Proxy and Reverse Proxies.md](07_Network%20Performance/09_The%20importance%20of%20Proxy%20and%20Reverse%20Proxies.md) |
| **7.10** | Load Balancing: Layer 4 vs. Layer 7 tradeoffs | [10_Load Balancing at Layer 4 vs Layer 7.md](07_Network%20Performance/10_Load%20Balancing%20at%20Layer%204%20vs%20Layer%207.md) |
| **7.11** | Network Access Control (NAC) to database servers | [11_Network Access Control to Database Servers.md](07_Network%20Performance/11_Network%20Access%20Control%20to%20Database%20Servers.md) |

---

### Section 8: Network Routing (2 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **8.1** | Fundamentals of network routing: routing tables and hops | [01_Fundamentals of Network Routing.md](08_Network%20Routing/01_Fundamentals%20of%20Network%20Routing.md) |
| **8.2** | Networking with Docker: bridge, host, and overlay routing | [02_Networking with Docker.md](08_Network%20Routing/02_Networking%20with%20Docker.md) |

---

### Section 9: Analyzing Protocols with Wireshark (5 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **9.1** | Wiresharking UDP packets | [01_Wiresharking UDP.md](09_Analyzing%20Protocols%20with%20Wireshark/01_Wiresharking%20UDP.md) |
| **9.2** | Wiresharking TCP and HTTP requests | [02_Wiresharking TCPHTTP.md](09_Analyzing%20Protocols%20with%20Wireshark/02_Wiresharking%20TCPHTTP.md) |
| **9.3** | Wiresharking HTTP/2 and decrypting TLS traffic | [03_Wiresharing HTTP2 (Decrypting TLS).md](09_Analyzing%20Protocols%20with%20Wireshark/03_Wiresharing%20HTTP2%20(Decrypting%20TLS).md) |
| **9.4** | Wiresharking MongoDB wire protocol | [04_Wiresharking MongoDB.md](09_Analyzing%20Protocols%20with%20Wireshark/04_Wiresharking%20MongoDB.md) |
| **9.5** | Wiresharking Server-Sent Events (SSE) streaming | [05_Wiresharking Server Sent Events.md](09_Analyzing%20Protocols%20with%20Wireshark/05_Wiresharking%20Server%20Sent%20Events.md) |

---

### Section 10: Answering Your Questions (2 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **10.1** | Should Layer 4 proxies buffer TCP segments? | [01_Should Layer 4 Proxies buffer segments.md](10_Answering%20your%20Questions/01_Should%20Layer%204%20Proxies%20buffer%20segments.md) |
| **10.2** | How does the OS kernel manage TCP connections? | [02_How does the Kernel manage TCP connections.md](10_Answering%20your%20Questions/02_How%20does%20the%20Kernel%20manage%20TCP%20connections.md) |

---

### Section 11: Course Summary (1 Lecture)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **11.1** | Complete network engineering course summary | [01_Course Summary.md](11_Course%20Summary/01_Course%20Summary.md) |

---

### Section 12: Extras & Deep Dives (9 Lectures)
| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **12.1** | Exposing local servers publicly via tunneling | [01_Exposing local servers publicly.md](12_Extras/01_Exposing%20local%20servers%20publicly.md) |
| **12.2** | The networking behind clicking a link | [02_The Networking behind clicking a link.md](12_Extras/02_The%20Networking%20behind%20clicking%20a%20link.md) |
| **12.3** | Server Name Indication (SNI) TLS extension | [03_What is SNI.md](12_Extras/03_What%20is%20SNI%20(Server%20Name%20Indication%20TLS%20Extension).md) |
| **12.4** | Replacing TCP for data centers (Part 1) | [04_Replacing TCP for Data Centers (Part 1).md](12_Extras/04_Replacing%20TCP%20for%20Data%20Centers%20(Part%201).md) |
| **12.5** | Replacing TCP for data centers (Part 2) | [05_Replacing TCP for Data Centers (Part 2).md](12_Extras/05_Replacing%20TCP%20for%20Data%20Centers%20(Part%202).md) |
| **12.6** | Replacing TCP for data centers (Part 3) | [06_Replacing TCP for Data Centers (Part 3).md](12_Extras/06_Replacing%20TCP%20for%20Data%20Centers%20(Part%203).md) |
| **12.7** | Running out of TCP source ports | [07_Running out of TCP Source Ports.md](12_Extras/07_Running%20out%20of%20TCP%20Source%20Ports.md) |
| **12.8** | Postgres failure caused by a Cisco router (TCP window issue) | [08_Postgres failure caused by a Cisco router.md](12_Extras/08_Postgres%20failure%20caused%20by%20a%20Cisco%20router%20(TCP%20issue).md) |
| **12.9** | TLS 0-RTT: early data and replay vulnerabilities | [09_TLS 0-RTT.md](12_Extras/09_TLS%200-RTT.md) |

---

## 🔗 Repository Integration & Traceability

1. **Full Text Transcript**: The unedited continuous course transcript is archived in [`Course Fundamentals of Network Engineering_Full.md`](Course%20Fundamentals%20of%20Network%20Engineering_Full.md).
2. **Master Architecture Synthesis**: Synthesized networking fundamentals, socket lifecycles, and cloud topologies are documented in [`Networking.md`](../../output/Note_version-1_Networking/Networking.md).
3. **Audit Compliance**: Verified with zero rendering errors under `engine/scripts/audit_rendering.py`.
