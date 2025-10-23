---
id: f26c611c-de92-4700-80b7-4ba08b18e09f
name: Network Pivoting with Gost
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.846806+00:00'
updated_at: '2023-04-10T20:25:21.045958+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Gost]]'
- '[[Network Pivoting Techniques]]'
---

# Network Pivoting with Gost

## Summary

Network pivoting is a technique used by attackers to move laterally within a network, gaining access to resources that are normally inaccessible from the outside. Gost is a tool that can be used for network pivoting. It allows an attacker to create a SOCKS5 proxy server on the compromised system, w

## Description

# Description

Network pivoting is a technique used by attackers to move laterally within a network, gaining access to resources that are normally inaccessible from the outside. Gost is a tool that can be used for network pivoting. It allows an attacker to create a SOCKS5 proxy server on the compromised system, which can then be used to pivot to other systems within the network.

From a technical standpoint, Gost works by intercepting network traffic and redirecting it through the proxy server. This allows the attacker to access systems that are not directly accessible from the outside. From a business perspective, network pivoting can be used to gain access to sensitive data or systems, allowing an attacker to steal intellectual property, financial data, or other confidential information.


 

## Requirements

1. Access to a compromised system within the target network

1. Ability to run the 'Git Clone and Build Gost' command on the compromised system

 

## Defense

1. Segment your network to limit lateral movement

1. Monitor network traffic for signs of network pivoting

1. Use endpoint protection software to detect and prevent the installation of malicious software

 

## Objectives

1. Gain access to systems within a network that are not directly accessible from the outside

1. Steal sensitive data or access confidential information

 

# Instructions

1. To use this command, you must have Git and Go installed on your system. 

1. First, clone the Gost repository by running the command 'git clone https://github.com/ginuerzh/gost'. 
2. Navigate to the Gost cmd directory by running the command 'cd gost/cmd/gost'. 
3. Build Gost by running the command 'go build'. 
4. To use Gost as a SOCKS5 proxy, run 'gost -L=socks5://:1080' on the server side and 'gost -L=:8080 -F=socks5://server_ip:1080?notls=true' on the client side. 
5. To use Gost for local port forwarding, run 'gost -L=tcp://:2222/192.168.1.1:22 [-F=..]'.

 



**Code**: [[git clone https://github.com/ginuerzh/gost
cd gost]]



> This command clones the Gost repository from Github, navigates to the Gost cmd directory, and builds the Gost binary. It also provides instructions on how to use Gost as a SOCKS5 proxy and for local port forwarding. The '-L' flag is used to specify the listening address and protocol. The '-F' flag is used to specify the forwarding address and protocol. The 'notls=true' argument is used to disable TLS encryption for the SOCKS5 proxy. The '-L' flag is followed by the listening address and port number, while the '-F' flag is followed by the forwarding address and port number. For local port forwarding, the '-L' flag is followed by the local address and port number, and the '-F' flag is followed by the remote address and port number.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Tags

- [[Gost]]
- [[Network Pivoting Techniques]]


