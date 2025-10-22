---
id: af67038e-9ba9-40f1-904f-9fc6fea7ca2a
name: voiphopper
type: tool
verified: false
created_at: '2019-08-28T21:17:41.984500+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# voiphopper

## Overview

VoIP Hopper is a GPLv3 licensed security tool, written in C, that rapidly runs a VLAN Hop into the Voice VLAN on specific ethernet switches. VoIP Hopper does this by mimicking the behavior of an IP Phone, in Cisco, Avaya, Nortel, and Alcatel-Lucent environments.  This requires two important steps i

## Description

VoIP Hopper is a GPLv3 licensed security tool, written in C, that rapidly runs a VLAN Hop into the Voice VLAN on specific ethernet switches. VoIP Hopper does this by mimicking the behavior of an IP Phone, in Cisco, Avaya, Nortel, and Alcatel-Lucent environments.  This requires two important steps in order for the tool to traverse VLANs for unauthorized access.  First,  discovery of the correct 12 bit Voice VLAN ID (VVID) used by the IP Phones is required.  VoIP Hopper supports multiple protocol discovery methods (CDP, DHCP, LLDP-MED, 802.1q ARP) for this important first step.  Second, the tool creates a virtual VoIP ethernet interface on the OS.  It then inserts a spoofed 4-byte 802.1q vlan header containing the 12 bit VVID into a spoofed DHCP request.  Once it receives an IP address in the VoIP VLAN subnet, all subsequent ethernet frames are “tagged” with the spoofed 802.1q header.  VoIP Hopper is a VLAN Hop test tool but also a tool to test VoIP infrastructure security.
