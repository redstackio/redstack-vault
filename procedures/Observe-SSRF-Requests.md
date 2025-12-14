---
tags:
  - ssrf
  - observation
type: procedure
tools:
  - '[[tools/Lavf-55.48.100]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/server-get-external-mp4-1]]'
  - '[[commands/server-get-external-mp4-2]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.235Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1f90cd7d-b33c-4c59-b872-c506cea31012
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-SSRF-Requests

## Summary

This procedure monitors server logs on a controlled domain to observe and confirm SSRF requests triggered by Lavf processing of the uploaded M3U8 playlist.

## Description

After uploading the crafted M3U8, the Imgur server uses Lavf/55.48.100 to parse and fetch resources, resulting in outbound GET requests visible in external server logs. This confirms the SSRF and allows assessment of reachable resources. Requires a web server setup for logging.

## Requirements

1. Controlled domain with logging enabled (e.g., Nginx access logs)
2. Prior upload of M3U8 to trigger requests
3. Real-time log monitoring tools

## Defense

Defensive measures and detection strategies:

- Implement request logging and anomaly detection for media processing outbound traffic
- Block or rate-limit requests from known media libraries like Lavf
- Use WAF rules to detect playlist-based URL manipulation

## Objectives

1. Verify SSRF exploitation
2. Identify fetched resources
3. Gather evidence for impact assessment

## Instructions

### Step 1: Monitor Logs for Primary Request

**Context**: Check for the initial MP4 fetch.

**Command** ([[commands/server-get-external-mp4-1]]):
```bash
tail -f /var/log/nginx/access.log | grep "GET /1.mp4 HTTP/1.1" | grep "Lavf/55.48.100"
```

> Expected: Log showing 200 OK, 84 bytes, User-Agent: Lavf/55.48.100.

### Step 2: Monitor Logs for Secondary Request

**Context**: Confirm arbitrary request to non-existent resource.

**Command** ([[commands/server-get-external-mp4-2]]):
```bash
tail -f /var/log/nginx/access.log | grep "GET /2.mp4 HTTP/1.1" | grep "Lavf/55.48.100"
```

> Expected: Log showing 404 Not Found, 169 bytes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/server-get-external-mp4-1]]
- [[commands/server-get-external-mp4-2]]

## Tools Used

- [[tools/Lavf-55.48.100]]

## Tags

- ssrf
- logging
