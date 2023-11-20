2.b)

1. kar upor VITTI kore Isp select korbo.
2. amake ekta DEDICATED internet connection dewar jonno isp ki korbe.

## ei isp kemon service dey seta bolbo but eita secondary. tk koto dewa lage etc

##main point:

# ei isp bangladesh sorkar er nibondhito isp kina. karon amra jani isp gulo internet kene sorkar er kas theke. ei isp jodi nibondhito isp na hoy thake, tahole tar kono validity nai.

#ei isp sorkar er kas theke koto gb kene? .. iig(international internet gateway) theke se koto gb internet kene and tar kotojon client ke se eta die service provide kore.

# er kotogulo public ip hosting ase

# er proxy server ase kina

# er nijosso server ase kina

## dedicated paite hole:

# public ip lagbe. jate isp monitor korte parbe, but okhane gie ar mapping hobe na. orthat amar data amar ip diei chole jabe and

    amar kase jokhon ashbe tokhon o seta mapping hobe na karon amar ip address diei chole asbe.
    this is the work of dedicated connection.
    
    onnothat, jeta lease line/ shared line - private ip dibe, oitake bivinno multiplexing er madhome public network er shathe pair kore, data send and data receive hobe.

## amake ekta ip address dibe -> tader ekta server address thakbe -> tader ekta NAT Box(network address translation) thakbe.

## figure eke bornona korte hobe. cisco packet tracer e jemon message passing hoy, oirkokom kore dekhate hobe

2.c)
ekta computer, arekta computer er shathe jodi data send / data receive korte pare, seta peer to peer connection. eek e vabe, (ekta computer er shathe baki 99 ta computer er connection thakte pare but jokhon data send or data receive korbo, tokhon ekjon er shthei korbo/ ekjon er tai receive korbo.)

for example, hall er lan connection. ekjon data dito, tar shathe peering kore data send/recieve. er subidha hosse network traffic kom hoy.
peer to peer korle speed bare, traffic kome.

3.a)
message to tara code/ encoding korei pathabe. but one way can be 

3.c)
ami data pathanor por, jei key die ei data decipher korte hobe sei key ta public kore disi. jodi process na jana hoy taile ei public key die decipher korte koekso bosor somoy lagbe. (amar moble er pin 0 to 9 projonot bosano jaite pare is a public key)

4.a) not possible because ei web nam er shathe ekta ip address lagbe jei ip address ta kena lagbe and also ei nam tao kena lagbe.

    # private network banaile lagbe na. public network e hosting korte hole organization er assistance lagbe.
    
    # how DNS is associated: ip address amra pailam amader website er nam er jonno. karon amra jani nam die search kora jayna, ip die search kora lage karon packet initiate hoy ip die.
    
    now, jehetu website er nam die search kora hosse, ekhon kaj hosse DNS er kase gie sune asa ei nam er web er ip address koto. 

4.b) eek e isp jokhon internet broadcast kortese and smooth broadcast kortese, ami jodi access korte na pari, and arekjon access korte partese, eta amar device er problem er karone.

    # amar kase packet ashce oi packet ashce oi packet amar receive hoynai. ami jei network or transmission line e asi, oi line e konovabe data interruption hoise jar karone packet pousaynai    
    
    #jehetu eita live telecast, data jodi amar kase na pousay, eita resend korar sujog thake na, karon eta real time broadcast. so real time e oi packet receive korte na parle, oi packet loss.
    
    # network address die example dewa lagbe

4.c) book

** osi model
** routing protocol er 2 ta algorithm

----

https://www.youtube.com/playlist?list=PLMW5djzR9cKPDaY5f30lC4VgqL9nRQG6g
https://www.youtube.com/playlist?list=PLW7fU_8SZVruBsFfULu9QRDsFfFSg77Cu
https://www.youtube.com/playlist?list=PLgH5QX0i9K3p5OI88r3ob-otmKqIm_DbS
https://www.youtube.com/playlist?list=PLjq9G-RJFRrYwU2xgRG4KWLzEoZYLxb6L
https://www.youtube.com/playlist?list=PLab5XCu7ERqDeo4jsQyxbkWvv4w-0wTQk
https://www.youtube.com/playlist?list=PLMW5djzR9cKMTcsk5E2vnXpDnOIjXRd_j

---------

# 2019 1)

Question 1: Will there be any problem?
Yes, there may be compatibility issues and challenges in communication between a computer using the OSI reference model and a friend's computer using a hybrid reference model. The OSI (Open Systems Interconnection) model and hybrid models are not inherently compatible because they have different numbers of layers and may define those layers differently. To ensure successful communication, both sides need to translate or adapt their communication processes to bridge the gap between the models.

Question 2: Process for Communication with Each Layer for Sender and Receiver Side:

Sender (OSI Model):

1. Application Layer:
   
   - The sender initiates communication by running an application (e.g., email client, web browser) and generating a message or request.

2. Presentation Layer:
   
   - Data from the application layer is formatted and transformed if necessary to ensure compatibility with the OSI model.

3. Session Layer:
   
   - The session layer establishes, maintains, and terminates sessions between the sender and receiver if needed (e.g., setting up a connection).

4. Transport Layer:
   
   - Data from the session layer is divided into segments or packets.
   - The transport layer adds source and destination port numbers and error-checking information (such as checksums) to each segment.

5. Network Layer:
   
   - The network layer adds source and destination IP addresses to the segments.
   - Routing decisions are made based on the destination IP address to determine the path the data should take.

6. Data Link Layer:
   
   - Data from the network layer is further divided into frames.
   - MAC addresses are added to the frames.
   - Error detection and correction may occur at this layer.

7. Physical Layer:
   
   - The frames are converted into electrical or optical signals and transmitted over the physical medium (e.g., cables, wireless).

Receiver (Hybrid Model):

1. Physical Layer:
   
   - The received signals are converted back into frames.
   - Error detection and correction may occur at this layer.

2. Data Link Layer:
   
   - Frames are stripped of MAC addresses.
   - The frames are reassembled into packets.

3. Network Layer:
   
   - The network layer processes packets and may perform routing based on destination IP addresses.

4. Transport Layer:
   
   - Transport layer information (source/destination ports, error-checking) is extracted from the packets.

5. Application Layer:
   
   - Data is delivered to the appropriate application, which processes and displays the message or content to the user.

In the above scenario, there might be challenges in mapping the hybrid model's layers to the OSI model's layers, and some translation or adaptation may be necessary for successful communication between the sender and receiver. The specific implementation details of the hybrid model would determine how these mappings are performed.

# 2019 2-b)

Question 1: Criteria for ISP Selection Based on Technical Grounds

When selecting an Internet Service Provider (ISP) based on technical considerations, it's essential to evaluate the following criteria:

1. **Public and Private IP Addresses**:
   
   - Assess the availability and pricing of static or dynamic public IP addresses. Determine if the ISP offers private IP addressing for internal network use.

2. **DNS Server Quality**:
   
   - Investigate the reliability and responsiveness of the ISP's DNS servers, as they impact web browsing and service accessibility.

3. **Bandwidth Allocation and Quality of Service (QoS)**:
   
   - Inquire about the ISP's policies regarding bandwidth allocation and QoS guarantees, particularly if you rely on critical applications or services.

4. **Peering Agreements and BGP Routing**:
   
   - Understand the ISP's peering agreements with other networks and whether they support BGP routing for greater control and redundancy.

5. **Government Bandwidth Allocations**:
   
   - In regions with government-allocated bandwidth, learn about the ISP's allocation, as it can affect network stability and performance.

6. **IPv6 Support**:
   
   - Ensure that the ISP provides IPv6 support if needed, especially with the growth of IPv6-enabled devices.

7. **IP Address Resources**:
   
   - Inquire about the ISP's available IP address resources, which can impact network flexibility and configuration options.

8. **Network Security**:
   
   - Discuss the ISP's network security measures, including DDoS protection and threat mitigation strategies.

9. **Redundancy and Failover**:
   
   - Determine if the ISP has redundancy and failover mechanisms to minimize downtime during network failures.

10. **Traffic Management Policies**:
    
    - Understand the ISP's traffic management policies, including any restrictions on specific traffic types or protocols.

11. **Upstream Providers**:
    
    - Learn about the ISP's upstream providers and their role in network reliability and performance.

Question 2: ISP's Activities in Providing Internet Connection

Once you've selected your ISP based on technical considerations, here's an overview of the activities they typically undertake to provide you with an internet connection:

1. **Infrastructure Deployment**:
   
   - The ISP deploys necessary network infrastructure in your area, including cables, fiber optics, and network nodes.

2. **Connection Setup**:
   
   - A technician visits your location to set up the physical connection, including installing cables, modems, and routers.

3. **Configuration**:
   
   - The ISP configures your modem or router with the required settings to establish a connection to their network.

4. **Provisioning**:
   
   - The ISP activates your account, assigns an IP address, and configures access based on your selected plan and technical requirements.

5. **DNS Server Configuration**:
   
   - The ISP configures DNS server settings on your equipment to ensure reliable and fast name resolution.

6. **Testing and Quality Assurance**:
   
   - Comprehensive testing is conducted to ensure a stable, secure, and high-performance connection in line with the technical specifications.

7. **Customer Support**:
   
   - The ISP offers ongoing customer support for troubleshooting issues and technical assistance.

8. **Billing and Payment**:
   
   - Billing is typically done on a monthly basis, with various payment options available for your convenience.

9. **Network Monitoring and Maintenance**:
   
   - The ISP continuously monitors the network for performance, reliability, and security, performing maintenance and upgrades as necessary.

10. **Compliance with Regulations**:
    
    - The ISP adheres to local and national regulations related to internet service provision, including data privacy and security laws.

11. **Service Upgrades and Changes**:
    
    - The ISP allows you to upgrade or modify your service plan to accommodate changing needs, ensuring flexibility and scalability.

These activities ensure that your selected ISP provides a reliable and high-quality internet connection that meets your technical requirements and expectations.

# 3-a)

A packet is a unit of data that is typically used in network communication. It is a formatted chunk of data that includes not only the actual message or payload but also metadata such as source and destination addresses, error-checking information, and control information. Packets are used to efficiently transmit data across networks and are an essential part of the OSI reference model.

Here's a chronology of how the message "I am a Student" is converted into a packet and frame at both the sender and receiver sides using the OSI reference model:

Sender (OSI Model):

1. Application Layer:
   
   - The sender initiates communication by composing the message "I am a Student."

2. Presentation Layer:
   
   - The message is prepared for transmission, which may involve character encoding or compression (if needed).

3. Session Layer:
   
   - The session layer may establish a session, although it's not explicitly required for a short message like this.

4. Transport Layer:
   
   - The transport layer divides the message into smaller segments, if necessary. In this case, the message is small, so it might remain as a single segment.

5. Network Layer:
   
   - The network layer adds source and destination IP addresses. For this example, let's assume the sender's IP address is 192.168.1.100, and the receiver's IP address is 192.168.1.200.

6. Data Link Layer:
   
   - The data link layer prepares the data for transmission by adding source and destination MAC (Media Access Control) addresses. This layer also includes error-checking information, such as CRC (Cyclic Redundancy Check), for data integrity.

7. Physical Layer:
   
   - The frame, consisting of the data link layer's work, is converted into electrical or optical signals and transmitted over the physical medium.

Receiver (OSI Model):

1. Physical Layer:
   
   - The receiver detects the incoming signals and converts them into a frame.

2. Data Link Layer:
   
   - The data link layer extracts the frame from the physical medium.
   - It checks for errors using the CRC and ensures the frame is addressed to the receiver's MAC address.

3. Network Layer:
   
   - The network layer processes the frame and extracts the source and destination IP addresses.
   - It checks if the destination IP address matches the receiver's IP address (192.168.1.200 in this example).

4. Transport Layer:
   
   - The transport layer processes the remaining data and reassembles it into a single segment, reconstructing the original message "I am a Student."

5. Presentation Layer:
   
   - The presentation layer may perform any necessary decoding or decompression.

6. Application Layer:
   
   - The message "I am a Student" is delivered to the appropriate application, which can display it to the receiver.

This process ensures that the original message is successfully transmitted from the sender to the receiver, passing through the layers of the OSI model along the way.

## Error:

Handling errors in data transmission is crucial to ensure data integrity and reliability. Errors can occur at various layers of the OSI model, and there are different techniques and protocols for error detection and correction. Here's a general process for handling errors during the transmission described in the previous response within the context of the OSI model:

1. Error Detection:
   
   - At the sender's side:
     
     - Data Link Layer: The sender's data link layer includes error-checking information (e.g., CRC) in the frame. Before sending, it computes this information based on the frame's contents and appends it to the frame.
     - Transport Layer: Some transport layer protocols (e.g., TCP) include error-checking mechanisms, such as checksums, for detecting errors in the segment.
   
   - At the receiver's side:
     
     - Data Link Layer: Upon receiving a frame, the data link layer checks the error-checking information (CRC) to detect any errors. If an error is detected, the frame is typically discarded.
     - Transport Layer: If the transport layer checksum indicates an error, the segment is discarded.

2. Error Notification:
   
   - If an error is detected at any layer, an error notification or acknowledgment may be sent back to the sender. The sender may then take corrective action, such as retransmitting the data.

3. Retransmission (if necessary):
   
   - If an error is detected, the sender may need to retransmit the affected data. The specific protocol used (e.g., TCP) handles the details of retransmission, ensuring the receiver gets the correct data.

4. Handling Errors at the Application Layer:
   
   - At the application layer, the application itself may have error-handling mechanisms. For example, if the receiver's application detects an error in the received message, it can request the sender to resend the message or take other appropriate actions.

5. Error Correction:
   
   - Some protocols, like Forward Error Correction (FEC), can correct errors on the fly. In such cases, the receiver can correct minor errors without requesting retransmission.

6. Redundancy:
   
   - Redundancy can be introduced at different layers to enhance error detection and correction. For example, in wireless communication, redundant data bits (parity bits) may be added at the physical layer to help detect and correct errors.

7. Error Logging and Analysis:
   
   - Systems often log error information for analysis and troubleshooting purposes. Network administrators can use these logs to identify patterns of errors and take preventive measures.

It's important to note that the specific error-handling mechanisms and protocols can vary depending on the technology used, such as Ethernet, Wi-Fi, or cellular networks, as well as the transport and application layer protocols (e.g., TCP, UDP). The OSI model provides a framework for understanding where errors can occur, but the exact methods and protocols for handling errors can differ based on the specific communication technologies and standards in use.
