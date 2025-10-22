---
id: cdd9123c-25fb-43a7-9b6a-eadc3ccff0cf
name: SAMAccountName Spoofing via SMB Credential Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.069604+00:00'
updated_at: '2023-04-10T20:26:08.295592+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[samAccountName spoofing]]'
commands:
- '[[crackmapexec smb]]'
---

# SAMAccountName Spoofing via SMB Credential Enumeration

## Summary

This procedure involves using the SMB Credential Enumeration command to extract password hashes from a target system. These hashes can then be used to perform a SAMAccountName spoofing attack, where an attacker can impersonate a legitimate user by changing their samAccountName to match that of the 

## Description

# Description

This procedure involves using the SMB Credential Enumeration command to extract password hashes from a target system. These hashes can then be used to perform a SAMAccountName spoofing attack, where an attacker can impersonate a legitimate user by changing their samAccountName to match that of the target user. This allows the attacker to bypass authentication mechanisms and gain unauthorized access to sensitive systems and data. From here, the attacker can escalate privileges and eventually obtain a SYSTEM shell on the domain controller, giving them complete control over the Active Directory environment.

From a technical perspective, this procedure takes advantage of weaknesses in the way Active Directory stores and manages user credentials. By extracting password hashes and spoofing user accounts, an attacker can bypass authentication mechanisms and gain access to sensitive systems and data. The business value of this attack lies in the ability for an attacker to gain access to critical systems and data, potentially causing significant financial and reputational damage to the organization.

## Requirements

1. Access to the target system

1. Authentication credentials with sufficient privileges

1. SMB Credential Enumeration tool

## Defense

1. Implement strong password policies and regularly rotate passwords

1. Monitor for unusual activity, such as multiple failed login attempts or changes to user account information

1. Use multi-factor authentication to prevent unauthorized access even if credentials are compromised

## Objectives

1. Extract password hashes from a target system

1. Perform a SAMAccountName spoofing attack to gain unauthorized access

1. Escalate privileges and obtain a SYSTEM shell on the domain controller

# Instructions

1. This command is used to enumerate SMB credentials from a target machine. The '-u' flag specifies the username to use for authentication, '-p' specifies the password, '-d' specifies the domain to authenticate against, and '-M nopac' disables the use of pre-authentication. 

**Code**: [[crackmapexec smb 10.10.10.10 -u '' -p '' -d domain]]

> This command can be used for penetration testing purposes to identify weak credentials on a target machine. It is important to note that unauthorized use of this command may be illegal and could result in legal consequences.

**Command** ([[crackmapexec smb]]):

```bash
crackmapexec smb 10.10.10.10 -u '' -p '' -d domain -M nopac
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[crackmapexec smb]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[samAccountName spoofing]]
