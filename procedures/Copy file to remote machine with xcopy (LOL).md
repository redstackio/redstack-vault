---
id: 309b8128-bfae-4f82-b76b-2c584d14fea2
name: Copy file to remote machine with xcopy (LOL)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T22:19:00.525565+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
platforms:
- Windows
tags:
- '[[file transfer]]'
commands:
- '[[Copy file to folder]]'
- '[[Map remote target folder as local drive (LOL)]]'
---

# Copy file to remote machine with xcopy (LOL)

## Summary

Copy a file to a remote machine using xcopy. 

## Description

# Description

Copy a file to a remote machine using xcopy.

## Objectives

1.  "net use" will authenticate to the remote machine using its local credentials and mount the target folder as a drive.

2. xcopy will copy the file from the local folder to the target folder of remote machine

# Instructions

1. Mount target folder from remote machine to a local drive while authenticating to its local user credentials

**Command** ([[Map remote target folder as local drive (LOL)]]):

```bash
net use t: \\$DOMAIN\C$\Users\Public /user:$DOMAIN\$USERNAME $PASSWORD
```

2. Copy the file to the target machine

**Command** ([[Copy file to folder]]):

```bash
xcopy C:\$FILENAME t:\FILENAME
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]

## Commands Used

- [[Copy file to folder]]
- [[Map remote target folder as local drive (LOL)]]

## Tags

- [[file transfer]]
