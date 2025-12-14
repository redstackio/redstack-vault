---
id: proc-imgur-nc-listen-001
tags:
  - ssrf
  - netcat
  - listen
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/nc-listen-port]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.537Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Listen-for-SSRF-Requests-with-Netcat

## Summary

This procedure uses netcat to listen on a specified port and capture incoming HTTP requests triggered by the SSRF exploitation in Imgur's ffmpeg.

## Description

After submitting the payload, ffmpeg makes a GET request to the attacker's URL (e.g., http://www.gradeco.ru:12346/BASICSSRF). Netcat logs the connection from Imgur's IP, confirming SSRF with headers like User-Agent: Lavf/55.48.100.

## Requirements

1. Netcat installed on attacker machine
2. Port 12346 open and forwarded if behind NAT
3. Firewall allows inbound TCP on 12346

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected outbound connections from internal services like ffmpeg
- Block or log connections to suspicious domains/ports
- Use network segmentation to isolate media processing

## Objectives

1. Capture proof of SSRF
2. Log request details for analysis
3. Verify exploitation success

## Instructions

### Step 1: Start Netcat Listener

**Context**: Listen verbosely on port 12346 for incoming connections.

Execute [[commands/nc-listen-port]]:

```bash
nc -v -l 12346
```

> Expected output: 'Connection from [Imgur-IP] port 12346' followed by GET /BASICSSRF HTTP/1.1, Host: www.gradeco.ru:12346, User-Agent: Lavf/55.48.100.

### Step 2: Analyze Logs

**Context**: Review captured requests to confirm SSRF.

No command; inspect terminal output or redirect to file with > ssrf.log.

> Success if Imgur IP (e.g., 54.82.61.224) appears with expected headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-port]]

## Tools Used

- [[tools/nc]]

## Tags

- ssrf
- listener
- tcp
