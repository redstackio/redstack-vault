---
id: proc-uuid-003
tags:
  - ssrf
  - observation
  - netcat
  - listener
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:58.404Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-SSRF-Request-with-Netcat

## Summary

This procedure uses netcat to listen on a target port and capture the incoming SSRF-forwarded request from the GitLab instance, confirming successful exploitation of the blind SSRF.

## Description

After triggering the SSRF, the GitLab server attempts an HTTPS POST to the specified Host:port (e.g., 162.243.147.21:81), which can be intercepted on an internal listener. This reveals the payload, including OAuth parameters, proving internal network pivoting without authentication.

## Requirements

1. netcat (nc) installed on the target internal host
2. Port 81 (or chosen) open and not firewalled
3. IP reachable from the GitLab instance's network
4. Trigger the SSRF first (from previous procedure)

## Defense

Defensive measures and detection strategies:

- Segment internal networks to isolate GitLab from sensitive services
- Monitor for unexpected inbound connections on non-standard ports
- Use IDS/IPS to detect anomalous internal HTTP traffic from app servers
- Disable unnecessary OAuth integrations if not in use

## Objectives

1. Capture and verify the SSRF request payload
2. Confirm internal access capability
3. Analyze request for further exploitation opportunities

## Instructions

### Step 1: Start Netcat Listener

**Context**: Bind to the target port to await the SSRF connection.

**Command** (nc usage):

```bash
nc -l 0.0.0.0 81
```

> This listens on all interfaces port 81. Keep it running before triggering SSRF.

### Step 2: Trigger and Observe

**Context**: After sending the SSRF request (from [[procedures/Trigger-SSRF-with-Manipulated-Host-Header]]), watch for incoming data.

No new command; inspect nc output for POST / HTTP/1.1, Host: ..., and body with OAuth params.

> Expected: Connection from GitLab IP, showing forwarded POST data. If HTTPS, may need ssl support or observe TCP connect.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nc]]

## Tags

- ssrf
- observation
- netcat
- listener
