---
tags:
  - exfiltration
  - file-read
  - mysql
type: procedure
tools:
  - '[[tools/rogue-mysql-server]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:28:20.377Z'
sub_techniques: []
id: 6cd45d15-b0c0-4a00-b3ca-42a31fcebd18
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Receive and Log Exfiltrated File Contents

## Summary

This procedure handles the reception of file contents transmitted by the victim's MySQL client after being tricked by the FB packet, logging them for attacker review.

## Description

Once connected and queried, the victim's client reads the specified file (e.g., /etc/passwd) locally and sends its contents over the MySQL protocol to the rogue server. The server parses and logs this data, achieving remote disclosure. This can bypass PHP restrictions and allow further pivoting.

## Requirements

1. Rogue server actively running
2. Victim connection established
3. Logging enabled in rogue script

## Defense

Defensive measures and detection strategies:

- Audit MySQL client logs for unexpected file reads
- Network monitoring for large outbound MySQL payloads
- File integrity monitoring on sensitive paths like /etc

## Objectives

1. Capture transmitted file data
2. Log contents securely
3. Validate exfiltration success

## Instructions

### Step 1: Enable Logging in Rogue Server

**Context**: Ensure the script outputs received data to a file or console.

**Command**:
```bash
# In rogue_mysql_server.py, add print statements for payload
python rogue_mysql_server.py > exfil_log.txt 2>&1
```

> Redirects output to log file.

### Step 2: Trigger and Receive

**Context**: Wait for victim query; server receives file chunks.

**Command**:
```bash
tail -f exfil_log.txt
```

> Displays incoming file contents in real-time.

### Step 3: Verify Contents

**Context**: Check logged data matches expected file.

**Command**:
```bash
grep 'root:' exfil_log.txt
```

> For /etc/passwd, confirms user entries present.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exfiltration Over Alternative Protocol]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/rogue-mysql-server]]

## Tags

- exfiltration
- file-read
- mysql
