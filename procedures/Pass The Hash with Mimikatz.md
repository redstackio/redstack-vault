---
id: b3dcd07d-2e06-4b6d-abdf-c780963d4df3
name: Pass The Hash with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.244754+00:00'
updated_at: '2023-04-10T20:37:19.140533+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Pass The Hash]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[mimikatz pth]]'
---

# Pass The Hash with Mimikatz

## Summary

Pass the Hash is a technique used by attackers to authenticate to a remote system using the NTLM hash of a user's password, rather than the plaintext password itself. Mimikatz is a powerful post-exploitation tool that can extract these hashes from memory on a compromised system, allowing an attacke

## Description

# Description

Pass the Hash is a technique used by attackers to authenticate to a remote system using the NTLM hash of a user's password, rather than the plaintext password itself. Mimikatz is a powerful post-exploitation tool that can extract these hashes from memory on a compromised system, allowing an attacker to use them to move laterally within a network.

From a technical perspective, Mimikatz works by exploiting weaknesses in the Windows authentication process. When a user logs into a Windows system, their password is hashed and stored in memory. Mimikatz can extract these hashes from memory, allowing an attacker to use them to authenticate to other systems without needing the original plaintext password.

The business value of this technique is that it allows attackers to move laterally within a network and access sensitive resources. By using stolen credentials, attackers can bypass authentication mechanisms and gain access to systems and data that would otherwise be protected.

## Requirements

1. Access to a compromised Windows system

1. Mimikatz tool

## Defense

1. Implement strong password policies and enforce regular password changes

1. Use multi-factor authentication to prevent attackers from using stolen credentials

1. Monitor network traffic for signs of lateral movement and anomalous authentication activity

## Objectives

1. Authenticate to a remote system using stolen credentials

1. Move laterally within a network

1. Access sensitive resources

# Instructions

1. Execute a Pass-the-Hash attack using mimikatz and obtain a shell as the SCCM$ user in the IDENTITY domain.

**Code**: [[mimikatz # sekurlsa::pth /user:SCCM$ /domain:IDENT]]

> This command uses the mimikatz tool to perform a Pass-the-Hash attack. The /user argument specifies the target user account to impersonate, in this case the SCCM$ account. The /domain argument specifies the target domain, in this case the IDENTITY domain. The /ntlm argument specifies the NTLM hash of the target user's password. The /run argument specifies the command to run after obtaining the impersonated user's token, in this case powershell. This command can be used to gain access to a system without knowing the user's password, but requires an existing NTLM hash of the user's password.

**Command** ([[mimikatz pth]]):

```powershell
mimikatz # sekurlsa::pth /user:SCCM$ /domain:IDENTITY /ntlm:e722dfcd077a2b0bbe154a1b42872f4e /run:powershell
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[mimikatz pth]]

## Tags

- [[Pass The Hash]]
- [[Windows - Mimikatz]]
