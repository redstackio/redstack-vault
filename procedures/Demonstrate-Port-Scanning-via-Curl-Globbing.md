---
tags:
  - curl
  - globbing
  - port-scanning
  - ssrf
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-port-scan-glob]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:26:06.308Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 54f456b1-d896-47c2-8a32-fa02a9341ef8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Demonstrate-Port-Scanning-via-Curl-Globbing

## Summary

This procedure uses curl's port field globbing to expand a range like [80-9000], generating multiple HTTP requests to scan for open ports, enabling reconnaissance or SSRF in filtered environments.

## Description

By globbing the port in a URL (e.g., http://1.1.1.1:[80-9000]/), curl attempts connections across the range, revealing open services via responses. This bypasses port restrictions and is effective for internal network scanning on Linux.

## Requirements

1. Curl with HTTP protocol support
2. Network access to target host (e.g., 1.1.1.1)
3. Verbose mode for connection details
4. No firewall blocking the range

## Defense

Defensive measures and detection strategies:

- Disable globbing with --globoff
- Implement rate limiting on inbound connections
- Log and alert on rapid port probes from single sources
- Use IDS like Snort for globbed URL patterns

## Objectives

1. Scan port range for open services
2. Identify potential SSRF targets
3. Gather network reconnaissance data

## Instructions

### Step 1: Execute Port Range Globbing

**Context**: Craft a URL with port glob to force multiple connection attempts, using verbose output to observe successes and failures.

**Command** ([[commands/curl-port-scan-glob]]):
```bash
curl -vv 'http://1.1.1.1:[80-9000]/'
```

> Expands to 8921 requests (ports 80-9000); open ports return HTTP responses, closed ones timeout or refuse, allowing port map inference from verbose logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-port-scan-glob]]

## Tools Used

- [[tools/curl]]

## Tags

- port-scanning
- ssrf
