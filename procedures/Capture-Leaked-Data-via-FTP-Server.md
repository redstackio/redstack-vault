---
id: proc-003
tags:
  - ftp-server
  - data-capture
  - pwntools
type: procedure
tools:
  - '[[tools/python3]]'
  - '[[tools/pwntools]]'
tactics:
  - '[[Exfiltration]]'
commands:
  - '[[commands/python3-run-poc-ftp-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:25:13.321Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Capture-Leaked-Data-via-FTP-Server

## Summary

This procedure sets up a simple FTP server using Python and pwntools to listen on port 1337, handle basic FTP commands from the libcurl client, and capture the leaked heap data sent in the PASS command.

## Description

The server responds to USER with a 331 prompt and receives the PASS command, which contains the over-read heap data due to the vulnerability. This allows the attacker to observe disclosed memory like uninitialized data, pointers, or secrets. Targeted at Linux with Python 3 and pwntools installed.

## Requirements

1. Python 3 and pwntools library
2. Port 1337 free on localhost
3. Prior execution of libcurl trigger

## Defense

Defensive measures and detection strategies:

- Block unauthorized FTP listeners on non-standard ports
- Network monitoring for anomalous FTP traffic with large or binary passwords
- Use application firewalls to restrict libcurl outbound connections

## Objectives

1. Establish FTP listener to receive the exfiltrated data
2. Parse and display the leaked password contents
3. Validate the over-read by checking for expected heap patterns

## Instructions

### Step 1: Prepare and Run Server Script

**Context**: Create or use a server.py script with pwntools to handle FTP protocol minimally.

**Command** ([[commands/python3-run-poc-ftp-server]]):

```bash
python3 server.py
```

> Script example: from pwn import *; l = listen(1337); c = l.wait_for_connection(); print(c.recvuntil(b'USER')); c.send(b'331 Please specify the password.\r\n'); pass_cmd = c.recvuntil(b'\r\n'); print(f"Received PASS: {pass_cmd}");. Expected: Server starts, waits for connection, prints leaked PASS like b'PASS AAAAAAAAAAAAAA\r\n'.

### Step 2: Analyze Captured Data

**Context**: Review the output for signs of heap leakage.

**Command** (Post-capture):

```bash
# Manual review of console output
```

> Look for non-credential data in PASS, such as repeated 'A's or binary artifacts. Success: Confirmation of over-read beyond the intended token.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration]] Exfiltration

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel Using Interactive Command

### Sub-Techniques


## Commands Used

- [[commands/python3-run-poc-ftp-server]]

## Tools Used

- [[tools/python3]]
- [[tools/pwntools]]

## Tags

- ftp-server
- data-capture
- pwntools
