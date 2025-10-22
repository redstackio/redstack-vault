---
id: 9ded0054-1fba-4262-aa6f-b634a87026f2
name: Browse an FTP Site with an Interactive Session
type: procedure
verified: true
submitted: true
created_at: '2020-04-01T00:29:32.993790+00:00'
updated_at: '2023-05-25T20:21:00.177175+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
platforms:
- Linux
- Windows
tags:
- '[[file transfer]]'
- '[[Network]]'
commands:
- '[[Launch an Interactive FTP Session]]'
---

# Browse an FTP Site with an Interactive Session

**Status**: ✓ Verified

## Summary

Authenticate and spawn an interactive FTP session. 

## Description

# Description

Authenticate and spawn an interactive FTP session.

# Instructions

**Command** ([[Launch an Interactive FTP Session]]):

```bash
ftp $_TARGET_IP
```

Note:  To attempt to authenticate anonymously, enter "anonymous" as the username and  anything for the password.

After connecting to FTP,  a number of common filesystem commands are available. 

**Code**: [[cd $_DIR - Change directory
dir - List folder cont]]

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]

## Commands Used

- [[Launch an Interactive FTP Session]]

## Tags

- [[file transfer]]
- [[Network]]
