---
id: ef81f284-c57c-460d-8f97-96bb7c1dca28
name: Portforwarding with Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.457851+00:00'
updated_at: '2023-04-10T20:24:59.731718+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Portforward]]'
commands:
- '[[Add Port Forwarding Rule]]'
---

# Portforwarding with Meterpreter

## Summary

Portforwarding with Meterpreter is a technique used to bypass firewalls and network security measures. By forwarding a port from the local machine to a remote host, an attacker can connect to a service running on the remote host that is not directly accessible from the attacker's machine. This tech

## Description

# Description

Portforwarding with Meterpreter is a technique used to bypass firewalls and network security measures. By forwarding a port from the local machine to a remote host, an attacker can connect to a service running on the remote host that is not directly accessible from the attacker's machine. This technique is commonly used to exfiltrate data from a target network. 

Technical Explanation: Meterpreter is a post-exploitation tool used to gain remote control of a compromised system. It provides a shell interface to interact with the compromised system and execute various commands. The portforward command in Meterpreter allows an attacker to forward a local port to a remote host, creating a tunnel through which traffic can be sent and received. 

Business Value: This technique can be used to exfiltrate sensitive data from a target network, such as customer data or intellectual property. By bypassing network security measures, an attacker can avoid detection and gain access to valuable information.

## Requirements

1. Meterpreter access to a compromised system

1. Knowledge of the target network topology

1. Access to a remote host

## Defense

1. Implement strict firewall rules to block inbound and outbound traffic on non-standard ports

1. Use network segmentation to isolate critical assets from the rest of the network

1. Monitor network traffic for signs of portforwarding activity

## Objectives

1. To forward a port from the local machine to a remote host

1. To bypass network security measures

1. To exfiltrate data from a target network

# Instructions

1. To forward a port from your local machine to a remote machine, use the 'portfwd add' command followed by the local port number (-l), the remote IP address (-r), and the remote port number (-p).

**Code**: [[portfwd add -l 7777 -r 172.17.0.2 -p 3006]]

> -l: The local port number that you want to forward.
-r: The IP address of the remote machine where you want to forward the port.
-p: The remote port number that you want to forward.

**Command** ([[Add Port Forwarding Rule]]):

```bash
portfwd add -l 7777 -r 172.17.0.2 -p 3006
```

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Add Port Forwarding Rule]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Portforward]]
