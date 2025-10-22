---
id: 0d4d7411-a5be-45d4-b747-ba415cbe183a
name: firewalk
type: tool
verified: false
created_at: '2019-08-28T21:17:37.924715+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# firewalk

## Overview

Firewalk is an active reconnaissance network security tool that attempts to determine what layer 4 protocols a  given IP forwarding device will pass. Firewalk  works  by sending out TCP or UDP packets with a TTL one greater than the targeted gateway.  If the gateway allows the traffic, it will forw

## Description

Firewalk is an active reconnaissance network security tool that attempts to determine what layer 4 protocols a  given IP forwarding device will pass. Firewalk  works  by sending out TCP or UDP packets with a TTL one greater than the targeted gateway.  If the gateway allows the traffic, it will forward the packets to the next hop where they will expire and elicit an ICMP_TIME_EXCEEDED  message.  If the gateway hostdoes not allow the traffic, it will likely drop the packets on  the floor and we will see no response.To get  the  correct  IP  TTL that will result in expired packets one beyond the gateway we need  to  ramp  up  hop-counts.   We  do  this  in the same manner that traceroute works.  Once we have the gateway hopcount (at  that point the scan is said to be `bound`) we can begin our scan.It is significant to note the fact that the ultimate destination host does not have to be reached.  It just  needs to be somewhere downstream, on the other side of the gateway, from the scanning host.
