---
tags:
  - ssrf
  - recon
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/nc-listen-ssrf]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.594Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1722c0c0-ae8b-44bb-ab12-90bd6b1892b5
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-SSRF-Request-with-Netcat

## Summary

This procedure uses netcat to listen on a specified port and capture incoming HTTP requests triggered by SSRF from Imgur's ffmpeg processing the m3u8 playlist, confirming arbitrary access.

## Description

After submitting the malicious upload, ffmpeg makes a GET request to the embedded URL in the m3u8. Netcat captures this, revealing Imgur's IP, User-Agent (Lavf/55.48.100 indicating ffmpeg version), and confirming SSRF success.

## Requirements

1. Netcat installed on attacker's machine
2. Open port 12346 on attacker's firewall
3. Prior setup of m3u8.php with embedded URL

## Defense

Defensive measures and detection strategies:

- Block outbound connections to non-standard ports from media processors
- WAF rules to detect anomalous request patterns
- Network segmentation to isolate internal services

## Objectives

1. Verify SSRF by capturing requests
2. Gather intelligence on target (e.g., ffmpeg version)
3. Validate exploit chain entry

## Instructions

### Step 1: Start Netcat Listener

**Context**: Listen for the SSRF-induced connection.

**Command** ([[commands/nc-listen-ssrf]]):
```bash
nc -v -l 12346
```

> Netcat listens in verbose mode on port 12346. Expected output: Connection from Imgur IP, GET /BASICSSRF with User-Agent: Lavf/55.48.100.

### Step 2: Trigger and Monitor

**Context**: Submit the Imgur request and watch for incoming data.

Submit the upload (from Step 1 procedure), then observe netcat output.

> Success: Logs show request details, confirming SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-ssrf]]

## Tools Used

- [[tools/nc]]

## Tags

- ssrf
- recon
