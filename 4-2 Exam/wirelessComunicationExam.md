<mark>**What is Cell? Different Cell shapes**</mark>

Cell represents a geographic area with a group of radio channels.



Ideally, we should consider the shape of the cell a circle, with radius R. But whenever we implement the actual cellular system, shape of the cell can be random depending upon the situation.

<img title="" src="file:///C:/Users/nayem/AppData/Roaming/marktext/images/2023-11-05-09-03-37-image.png" alt="" width="670">

However, we also have other shapes also. for example, Hexagonal shape, square, triangle.

**Now which one of these cells is suitable for cellular system?**

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-05-22-image.png)

a) circle has overlapping areas among the cells. That means, one cell will transmit it's signal to another cell and due to this, there will be interference.

    In another scenario for circle, where the cricles are not overlapping, then there will be gap between the cells. And due to that, if any user is present in that gap, will not be able to get any coverage.

b & c) for equilateral triangle and the square shape, if you consider the omnidirectional antenna, then the coverage of the antenna will be outside of the cell for example:

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-10-46-image.png)

Now if you consider the directional antenna, then the distance from the side and corner is different. so the signal will be either within the cell or reach outside the cell to cover the full triangle. So it will create interference with other cells.

d) so, hexagonal shape is the most preferrable shape. because from the midpoint, each and every side has almost equal distance and so we can cover all the areas of the cell.

Also, it is  very similar the the circular shape so we can use the omnidirectional antenna also.

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-21-32-image.png)





<mark>Frequency Reuse</mark>

<img src="file:///C:/Users/nayem/AppData/Roaming/marktext/images/2023-11-05-09-29-20-image.png" title="" alt="" width="727">



For example, in one cluster we have F1 set of frequency and in that same cluster we also have F2 to F7 set but not another F1 set, Then also in a different cluster we have again the F1 set of frequency. And the important thing is that the distance between this F1 and the other F1 is high enough so that the co-channel interference that is occuring in these co-cells, is tolerable.



<mark>Frequency Reuse Distance</mark>

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-35-44-image.png)

D = Reuse Distance

R = Radius of each and every cell

N (Cluster size or number of cells per cluster/Reuse pattern) = here, F1 to F7 , these 7 set of frequencies is a cluster

q = Reuse factor

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-42-42-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-43-34-image.png)![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-44-15-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-45-50-image.png)



<mark>Frequency Reuse Concept</mark>

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-09-47-30-image.png)



<mark>Handoff</mark>

<u>*wireless-communication-note.pdf*</u>

<mark>• **Handoff operation** </mark>

– identifying a new base station
– re-allocating the voice and control channels with the new base station.



<mark>Handoff scenario at cell boundary</mark>

The graph is showing two situations. (a) Improper handoff situation and (b) proper handoff situation

We have two base-station: base station-1 and base station-2.

the vertical axis is Received signal Strength level and the horizontal axis Time.



**(a) Improper handoff situation**

while user is at base-station-1, the current signal level(signal strength) is the upper line (level A).

currently, user is at point A, and when he starts moving away from base-station-1 towards the base-station-2, the signal strentght of bs1 will reduce.

the user will then arrive at handoff threshold

then he will arrive to point where the signal from bs1 will reduced so that, it will be below the minimum acceptable signal to maintain the call

Now when the user moves to the point (B) which is in bs2, the signal from bs1 will be terminated.



in this scenario, the signal is continuously reduced until terminated and no handoff decision is taken and the call will be dropped. so this is improper handoff situation because we are unable to take the decision of handoff.



**(b) Proper handoff situation**

user is moving away from the bs1 and the signal strength is reducing

whenever the signal is reduced to the handoff threshold level, we will take the decision of handoff through the MSC and then the user will get the signal from bs2 and the signal strength will then increase. So, the handoff decision will occur at the handoff threshold level.




*We should select the handoff threshold very carefully.*

• **Handoff Threshold**
– Minimum usable signal for acceptable voice quality (-90dBm to -100dBm)
– Handoff margin (dell sign) cannot be too large or too 
small.
![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-11-54-42-image.png)



<mark>Handoff Concepts</mark>

1. Prioritizing Handoffs

2. Umbrella Cell Approach

3. Cell Dragging

4. Microcell Zone Concept



<mark>**Prioritizing Handoffs:**</mark>

Determining the order in which handover requests are managed. We can do prioritizing handoff in 2 ways:

1. lets consider that we have 10 number of channels available, now out of these available channels, reserve 3 channels for the handoff and 7 channels for the carried traffic. ![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-12-24-46-image.png)

2. We are taking the advantage of this time interval and putting the user into queue and when a channel becomes availble, we will assign that channel to the user. in this queuing method, instead of utilizing some fixed fraction of channels, we are utilizing all available channels for the carried traffic as well as for the handoff. so if any channel is available, we are using it for the carry traffic as well as the handoff.
   
   Advantage is we are using all channels. however when all channels are busy, then increased new call blocking probability![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-12-37-55-image.png)



<mark>Umbrella Cell Approach:</mark>

Umbrella cell approach is a practical handoff consideration.![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-12-45-32-image.png)

<u>wireless-communication-note.pdf(page 24)</u>



<mark>Cell Dragging:</mark>

Cell dragging results from pedestrian users that provide a very strong signal to the Base Station. 
Such a situation occurs in an urban environment when there is a line-of-sight (LOS) radio path 
between the subscriber and the BS. As the user travels away from the Base Station at a very slow 
speed, the average signal strength does not decay rapidly. Even when the user has travelled well 
beyond the designed range of the cell, the received signal at the base station may be above the 
hand off threshold, thus a handoff may not be made. This creates a potential interference and 
traffic management problem.

To solve the cell dragging problem, handoff thresholds and radio coverage parameters must 
be adjusted carefully.

<img src="file:///C:/Users/nayem/AppData/Roaming/marktext/images/2023-11-05-12-51-40-image.png" title="" alt="" width="238">



<mark>MICROCELL ZONE CONCEPT</mark>

* Due to sectoring, the cell is divided into a number of parts and due to this sectoring concept, there will be an increased number of handoff in the system which will create an increased load on the MSC and the mobile system.
  
  * in microcell zone concept, a region is divided into 3 different zone. these 3 zones will have individual transmitter and receiver and it will be connected to the Zone Selector via Microwave or fibre optic link. All the 3 zones are connected to the Base Station. So the whole region is covered by only a single base station. Due to it, whenever a user moves from one zone to another zone,  it won't require to change any channel and also it won't require the handoff. That's how, with the help of microzone concept, we are reducing the number of handoff.

* Three zones are connected to a single base station

* Multiple zones and a single base station make up a cell.

* As a mobile travels from one zone to another within the cell, it retains the same channel.

* it reduces the handoff and is specially useful in highway areas.

* ![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-13-59-14-image.png)



<mark>Microcell zone concept reduces co-channel interferenc:</mark>

<img src="file:///C:/Users/nayem/AppData/Roaming/marktext/images/2023-11-05-14-01-32-image.png" title="" alt="" width="705">



<mark>Handoff detection strategies:</mark>

in cellular system we have 3 types of handoff detection stratesies:

1. Mobile Controlled Handoff (MCHO)

2. Network Controlled Handoff (NCHO)

3. Mobile Assisted Handoff (MAHO)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-14-10-45-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-14-12-30-image.png)

MAHO is the most popular handoff strategy because the mobile is measuring the signal strength, which will provide more accurate result and all the processing will be done at the network, that will reduce the load on the mobile.

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-14-17-10-image.png)



<mark>Channel Assignment Strategies</mark>

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-14-37-46-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-14-46-41-image.png)

<u>*wireless-communication-note.pdf*</u>



<mark>Interference:</mark>

page 28

Interference is the major limiting factor in the performance of cellular radio systems.

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-15-10-10-image.png)



<mark>Fading</mark>

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-16-43-38-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-16-56-22-image.png) 

## Large Scale Fading

* This refers to the attenuation of signal power due to obstacles between the transmitter and receiver.

* Large-scale fading is called “large-scale” because the variations occur over long distances, typically several kilometers.
- Unlike small-scale fading, which affects individual symbols or bits, large-scale fading affects the entire signal.
- Large-scale fading is a slow-varying phenomenon, meaning that it changes over time scales of seconds to minutes.
- Overall, large-scale fading is an important factor to consider in wireless communication system design, as it can significantly impact the quality of the received signal.

### Path Loss

- Path loss is the reduction in signal power as the signal travels from the transmitter to the receiver.
- Path loss is caused by a variety of factors, including distance, the frequency of the signal, obstacles in the path of the signal, and the characteristics of the environment.
- The path loss is generally modeled using an attenuation equation
- Path loss is generally a slow-varying phenomenon and affects the overall received signal power.
- Path loss can be mitigated by increasing the transmitted power, using directional antennas, or reducing the distance between the transmitter and the receiver.

### Shadowing

- Shadowing is a type of large-scale fading that occurs due to the presence of obstacles or obstructions in the path of the signal.
- Shadowing causes the signal power to vary as the receiver moves in the environment
- Shadowing is a slow-varying phenomenon and affects the overall received signal power.
- Shadowing can be mitigated by using techniques such as diversity, where multiple antennas are used to combine multiple signal paths, or by using signal processing techniques to estimate the shadowing effects and compensate for them.



## Small Scale Fading

- Small-scale fading is a common issue in wireless communication.
- It happens when a signal is transmitted from a transmitter to a receiver and it experiences multiple signal paths due to reflection, diffraction, and scattering from objects in the environment.
- Small-scale fading is called “small-scale” because the variations occur over short distances, such as a few centimeters to a few meters.
- Small-scale fading can happen very quickly, sometimes in microseconds or less.
- It is primarily caused by the multipath propagation of the signal.

### Multipath delay spread

- Multipath delay spread is a type of small-scale fading that occurs when a transmitted signal takes multiple paths to reach the receiver.
- The different components of the signal can arrive at the receiver at different times.

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-17-11-06-image.png)

### Doppler Spread

- Doppler spread is a type of small-scale fading that occurs when there is relative motion between the transmitter and the receiver.
- The relative motion causes a shift in the frequency of the transmitted signal, known as the Doppler shift.
- The Doppler shift causes different frequency components of the signal to arrive at the receiver with different phases and amplitudes.
- This results in rapid variations in signal amplitude and phase, which can cause fading and errors in the received signal.

Doppler spread is of 2 types:

## Fast fading

The phenomenon of fast fading is represented by rapid fluctuations of signal over small areas (i.e. bandwidth). When the signals arrive from all the directions in theplane, fast fading will be observed for all directions of motion.
Fast fading occurs when channel impulse response changes very rapidly within the symbol duration.
• High Doppler spread
• Coherence time < Symbol period
• Signal Variation < Channel variation

## Slow fading

Slow fading is result of shadowing by buildings, hills, mountains and other objects over the path.
• Low Doppler Spread
• Coherence time > Symbol period

• Signal Variation > Channel Variation


Slow fading results in a loss of SNR. Error correction coding and receiver diversity techniques 
are used to overcome effects of slow fading.



**<mark>GSM</mark>**

GSM is a larger system which is divided into further 3 subsystems:

1. **BSS :** BSS stands for Base Station Subsystem. BSS handles traffic and signaling between a mobile phone and the network switching subsystem. BSS having two components **BTS** and **BSC.** 
2. **NSS :** NSS stands for Network and Switching Subsystem. NSS is the core network of GSM. That carried out call and mobility management functions for mobile phone present in network. NSS have different components like **VLR, HLR** and **EIR.**
3. **OSS :** OSS stands for Operating Subsystem. OSS is a functional entity by which the network operator monitors and controls the system. **OMC**  is the part of OSS.

![Lightbox](https://media.geeksforgeeks.org/wp-content/uploads/20210401115316/gsm11.png)

**1. MS :** MS stands for Mobile Station. MS comprises of user equipment and software needed for communication with a mobile network.  Mobile Station (MS) =  Mobile Equipment(ME) + Subscriber Identity Module (SIM). Now, these mobile stations are connected to tower and that tower connected with BTS through TRX. TRX is a transceiver which comprises transmitter and receiver. Transceiver has two performance: sending and receiving.

**2. BTS :** BTS stands for Base Transceiver Station which facilitates wireless communication between user equipment and a network. Every tower has BTS. 

**3. BSC :** BSC stands for Base Station Controller. BSC has multiple BTS. consider the BSC which has multiple towers and each tower have BTS.

**4. MSC :** MSC stands for Mobile Switching Center. MSC is associated with communication switching functions such as call setup, call release and routing. Call tracing, call forwarding - all functions are performed at the MSC level.  MSC has components like HLR, VLR, AUC, EIR and PSTN.

- **HLR :** HLR stands for Home Location Register. HLR is a database containing data regarding subscribers authorized to use a GSM network. you purchase SIM card from the HLR. HLR is like a home which contains all data like your ID, which plan you are taking, which caller tune you are using etc.
- **VLR :** VLR stands for Visitor Location Register. VLR is a database which contains the exact location of all mobile subscribers currently present in the service area of MSC. If you are going from one state to another state then your entry is marked into the database of VLR.
- **AUC :** AUC stands for  Authentication Center. AUC authenticates the mobile subscriber that wants to connect in the network.
- **EIR :** EIR stands for Equipment Identity Register. EIR is a database that keeps the record of all allowed or banned in the network. If you are banned in the network then you can’t enter the network, and you can’t make the calls.
- **PSTN :** PSTN stands for Public Switched Telephone Network. PSTN connects with MSC. PSTN originally a network of fixed line analog telephone systems. Now almost entirely digital in its core network and includes mobile and other networks as well as fixed telephones. The earlier landline phones which places at our home is nothing but PSTN.

**5.OMC** : OMC stands for Operation Maintenance Center. OMC monitors and maintains the performance of each MS, BSC and MSC within a GSM system.

Three subsystem BSS, NSS and OSS are connected with each other via some interfaces. Total three interfaces are there:

1. **Air Interface :** Air interface is also known as UM interface. Interface  between MS and BTS is called as UM interface because it is mobile analog to the U interface of ISDN.
2. **Abis Interface :** It is a BSS internal interface linking with BTS and BSC.
3. **A interface :** It provides communication between BSS and MSC.







<mark>Free Space Propagation Model</mark>

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-20-02-03-image.png)



**Equation for predicting Received signal strength:**

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-20-13-30-image.png)



![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-20-15-21-image.png)

effective aperture is related to the wavelength of a signal. It will help us calculate the antenna gain.









![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-20-24-28-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-20-25-01-image.png)



after considering the Fraunhofer distance df, 

the received power at a distance d

d0 = close in reference distance

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-20-31-32-image.png)







**<mark>Two Ray Ground propagation Model:</mark>**

1.  We have a ground plain

2. we have a base station, ht is the height of transmitter. Also, we have a receiver, hr is the height of receiver.

3. distance between the Transmitter and Receiver is d

4. let's assume that the Transmitter sends a signal to the receiver by a direct line of sight signal (ELOS)

5. let's also assume that another signal from the Transmitter, incident on the ground plane with angle theta-i, which we call the angle of incident. And then, it will be reflected back to the receiver, this angle is theta-0 and Energy will be Er = Eg

6. so we have a ground reflection and we have 2 rays. one is direct line of sight signal, another is reflected signal.



Total Energy, Etot = Elos + Eg

It is used to predict large scale signal strength over large distance

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-23-27-54-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-23-39-02-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-23-44-43-image.png)



path difference = d" - d'

<img src="file:///C:/Users/nayem/AppData/Roaming/marktext/images/2023-11-05-23-49-16-image.png" title="" alt="" width="431">







Now for **Path loss**, 

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-05-23-52-17-image.png)









![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-06-10-25-04-image.png)

![](C:\Users\nayem\AppData\Roaming\marktext\images\2023-11-06-10-27-02-image.png)

Dwell time: the time over which a call may be maintained within a cell without handoff
Dwell time depends on
 propagation
 interference
 distance
 speed
