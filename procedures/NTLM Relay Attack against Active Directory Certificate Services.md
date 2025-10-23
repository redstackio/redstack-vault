---
id: 763f048b-aeb0-437a-ac43-4146480d33ce
name: NTLM Relay Attack against Active Directory Certificate Services
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.112777+00:00'
updated_at: '2023-04-10T20:26:28.111396+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC11 - Relaying NTLM to ICPR]]'
commands:
- '[[ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name lab-DC-CA -smb2support]]'
---

# NTLM Relay Attack against Active Directory Certificate Services

## Summary

An attacker can use the NTLM Relay attack technique to relay authentication attempts from a victim machine to a target machine. In this case, the target machine is the Active Directory Certificate Services (AD CS) server, which is responsible for issuing and managing digital certificates. By relayi

## Description

# Description

An attacker can use the NTLM Relay attack technique to relay authentication attempts from a victim machine to a target machine. In this case, the target machine is the Active Directory Certificate Services (AD CS) server, which is responsible for issuing and managing digital certificates. By relaying the victim's credentials to the AD CS server, the attacker can obtain a valid certificate that can be used to authenticate to other systems and services within the network.

To perform this attack, the attacker needs to have a foothold on a victim machine and be able to intercept network traffic between the victim machine and the AD CS server. The attacker can use the Impacket tool to relay the NTLM authentication attempts to the AD CS server and obtain a valid certificate.

The business value of this attack lies in the ability of the attacker to obtain valid certificates that can be used to impersonate legitimate users and gain access to sensitive data and systems within the network.

 

## Requirements

1. Access to a victim machine within the network

1. Ability to intercept network traffic between the victim machine and the AD CS server

1. Impacket tool

 

## Defense

1. Implement network segmentation to limit the exposure of the AD CS server

1. Use strong authentication mechanisms such as multi-factor authentication to prevent the use of stolen credentials

1. Monitor network traffic for signs of NTLM Relay attacks

 

## Objectives

1. Obtain a valid certificate from the AD CS server

1. Impersonate legitimate users within the network

1. Gain access to sensitive data and systems within the network

 

# Instructions

1. To perform an NTLM relay attack using Impacket ntlmrelay, follow these steps:

1. Run the command 'ntlmrelayx.py' followed by the target IP address and the desired relay mode.
2. Specify the ICPR mode and the name of the CA certificate used by the target server.
3. Enable SMB2 support if required.
4. Trigger a connection to the relayed server.

 



**Code**: [[ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR ]]



> The ntlmrelayx.py command is used to setup a relay on a target machine and force it to authenticate to the attacker's machine. This can be used to steal credentials or execute commands on the target machine. The '-t' option is used to specify the target machine, and the '-rpc-mode' option is used to specify the relay mode. The ICPR mode is used to relay the authentication to a Certificate Authority (CA) that is trusted by the target machine. The '-icpr-ca-name' option is used to specify the name of the CA certificate used by the target machine. The '-smb2support' option is used to enable SMB2 support if required. Once the relay is setup, a connection can be triggered to the relayed server to initiate the attack.



**Command** ([[ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name lab-DC-CA -smb2support]]):

```bash
ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name lab-DC-CA -smb2support
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[ntlmrelayx.py -t rpc://10.10.10.10 -rpc-mode ICPR -icpr-ca-name lab-DC-CA -smb2support]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC11 - Relaying NTLM to ICPR]]


