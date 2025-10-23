---
id: b2b9e57b-6237-4dd1-b733-f20e3baabe99
name: Windows Netsh Port Forwarding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.395634+00:00'
updated_at: '2023-05-26T00:59:52.725055+00:00'
tags:
- '[[Network Pivoting Techniques]]'
- '[[Windows netsh Port Forwarding]]'
commands:
- '[[Forwarding ports 4545 and 80]]'
- '[[Opening ports 80 and 4545 on the machine]]'
- '[[Port Forwarding from local port to destination port]]'
---

# Windows Netsh Port Forwarding

## Summary

Windows netsh Port Forwarding is a network pivoting technique used by attackers to redirect traffic from one network to another. This technique involves using the netsh command to create a port forwarding rule on a compromised Windows machine. Once the rule is in place, attackers can use the compro

## Description

# Description

Windows netsh Port Forwarding is a network pivoting technique used by attackers to redirect traffic from one network to another. This technique involves using the netsh command to create a port forwarding rule on a compromised Windows machine. Once the rule is in place, attackers can use the compromised machine as a proxy to access other machines on the target network.

From a technical perspective, netsh Port Forwarding works by creating a TCP port forwarding rule on the compromised machine. This rule redirects traffic from a specific port on the compromised machine to a specific port on another machine on the target network. By doing so, attackers can bypass network security controls and gain access to machines that are otherwise inaccessible.

The business value of Windows netsh Port Forwarding lies in its ability to provide attackers with a foothold on a target network. Once attackers have access to one machine on the network, they can use this technique to pivot to other machines and gain access to sensitive data and systems.

 

## Requirements

1. Compromised Windows machine with netsh command access

1. Access to target network

 

## Defense

1. Implement network segmentation to limit lateral movement

1. Monitor network traffic for signs of port forwarding activity

1. Disable unnecessary services and protocols to limit attack surface

 

## Objectives

1. Gain access to machines on a target network

1. Bypass network security controls

1. Steal sensitive data and compromise systems

 

# Instructions

1. Use the following commands to forward ports on your machine:

 



**Code**: [[netsh interface portproxy add v4tov4 listenaddress]]



> The above commands will allow you to forward ports on your machine. The 'listenaddress' and 'listenport' fields specify the local address and port where the traffic is coming from, while the 'connectaddress' and 'connectport' fields specify the destination address and port where the traffic will be forwarded to. The 'netsh advfirewall firewall add rule' commands are used to open the specified ports on the machine's firewall.



**Command** ([[Port Forwarding from local port to destination port]]):

```bash
netsh interface portproxy add v4tov4 listenaddress=localaddress listenport=localport connectaddress=destaddress connectport=destport
netsh interface portproxy add v4tov4 listenport=3340 listenaddress=10.1.1.110 connectport=3389 connectaddress=10.1.1.110
```





**Command** ([[Forwarding ports 4545 and 80]]):

```bash
netsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44 connectport=4545
netsh interface portproxy add v4tov4 listenport=80 connectaddress=192.168.50.44 connectport=80
```





**Command** ([[Opening ports 80 and 4545 on the machine]]):

```bash
netsh advfirewall firewall add rule name="PortForwarding 80" dir=in action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="PortForwarding 80" dir=out action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=in action=allow protocol=TCP localport=4545
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=out action=allow protocol=TCP localport=4545
```



## Commands Used

- [[Forwarding ports 4545 and 80]]
- [[Opening ports 80 and 4545 on the machine]]
- [[Port Forwarding from local port to destination port]]

## Tags

- [[Network Pivoting Techniques]]
- [[Windows netsh Port Forwarding]]


