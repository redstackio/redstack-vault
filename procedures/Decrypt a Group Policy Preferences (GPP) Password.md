---
id: b84cf1aa-9379-4fdf-8b0b-1da6ce4658ad
name: Decrypt a Group Policy Preferences (GPP) Password
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T18:34:03.961833+00:00'
updated_at: '2023-05-25T19:53:01.794693+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[Cryptography]]'
- '[[data encryption]]'
- '[[known vulnerability]]'
commands:
- '[[gpp-decrypt Extract Password from a GPP Encrypted String]]'
---

# Decrypt a Group Policy Preferences (GPP) Password

**Status**: ✓ Verified

## Summary

Decrypt a Group Policy Preference Password using gpp-decrypt. While passwords contained in these GPP files are encrypted, Microsoft published the AES key, making decryption trivial. GPP files are often found on SYSVOL shares, as administrators use them to apply the same settings across multiple mac

## Description

# Description

Decrypt a Group Policy Preference Password using gpp-decrypt. While passwords contained in these GPP files are encrypted, Microsoft published the AES key, making decryption trivial. GPP files are often found on SYSVOL shares, as administrators use them to apply the same settings across multiple machines.



# Instructions





**Command** ([[gpp-decrypt Extract Password from a GPP Encrypted String]]):

```bash
gpp-decrypt $_ENCRYPTED_STRING
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[gpp-decrypt Extract Password from a GPP Encrypted String]]

## Tags

- [[Cryptography]]
- [[data encryption]]
- [[known vulnerability]]


