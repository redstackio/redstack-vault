---
id: 895a0d7d-107e-4b39-8625-b4bf8cbc7d2d
name: Hardware Additions
type: technique
mitre_id: T1200
mitre_url: null
created_at: '2019-08-28T21:17:31.946893+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
procedures:
- '[[AdminSDHolder Group Rights Abuse]]'
- '[[CSRF JSON GET Request]]'
- '[[CSRF JSON GET Request]]'
- '[[MSSQL List Tables]]'
- '[[XSS Cookie and Access Token Grabber]]'
- '[[XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert]]'
---

# Hardware Additions

**MITRE ID**: T1200

## Description

Computer accessories, computers, or networking hardware may be introduced into a system as a vector to gain execution. While public references of usage by APT groups are scarce, many penetration testers leverage hardware additions for initial access. Commercial and open source products are leveraged with capabilities such as passive network tapping [1], man-in-the middle encryption breaking [2], keystroke injection [3], kernel memory reading via DMA [4], adding new wireless access to an existing network [5], and others.

# Detection

Asset management systems may help with the detection of computer systems or network devices that should not exist on a network. 

Endpoint sensors may be able to detect the addition of hardware via USB, Thunderbolt, and other external device communication ports.

# Mitigation

Establish network access control policies, such as using device certificates and the 802.1x standard. [6] Restrict use of DHCP to registered devices to prevent unregistered devices from communicating with trusted systems. 

Block unknown devices and accessories by endpoint security configuration and monitoring agent.

# Footnotes

[1] Michael Ossmann. (2011, February 17). Throwing Star LAN Tap. Retrieved March 30, 2018.

[2] Nick Aleks. (2015, November 7). Weapons of a Pentester - Understanding the virtual & physical tools used by white/black hat hackers. Retrieved March 30, 2018.

[3] Hak5. (2016, December 7). Stealing Files with the USB Rubber Ducky – USB Exfiltration Explained. Retrieved March 30, 2018.

[4] Ulf Frisk. (2016, August 5). Direct Memory Attack the Kernel. Retrieved March 30, 2018.

[5] Robert McMillan. (2012, March 3). The Pwn Plug is a little white box that can hack your network. Retrieved March 30, 2018.

[6] Wikipedia. (2018, March 30). IEEE 802.1X. Retrieved April 11, 2018.

## Defense

Establish network access control policies, such as using device certificates and the 802.1x standard. (Citation: Wikipedia 802.1x) Restrict use of DHCP to registered devices to prevent unregistered devices from communicating with trusted systems. 

Block 

## Tactics

- [[Initial Access|TA0001 - Initial Access]]

## Related Procedures (6)

- [[AdminSDHolder Group Rights Abuse]]
- [[CSRF JSON GET Request]]
- [[CSRF JSON GET Request]]
- [[MSSQL List Tables]]
- [[XSS Cookie and Access Token Grabber]]
- [[XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert]]
