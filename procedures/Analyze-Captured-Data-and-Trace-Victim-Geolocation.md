---
id: proc-analyze-geolocation
tags:
  - ssrf
  - analysis
  - geolocation
  - ip-trace
type: procedure
tools:
  - '[[tools/ngrok]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-ipinfo-geolocation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Address Translation Traversal]]'
updated_at: '2025-12-14T17:32:01.824Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Address Translation Traversal]]'
---
# Analyze-Captured-Data-and-Trace-Victim-Geolocation

## Summary

This procedure examines the captured SSRF request in ngrok for victim metadata (IP, browser, OS) and uses an IP geolocation service to trace physical location, demonstrating the reconnaissance impact.

## Description

Post-capture, the ngrok interface reveals headers like X-Forwarded-For (victim IP), User-Agent (browser/OS). Querying geolocation services provides location data, enabling further targeting or port scanning. This extends SSRF to active reconnaissance.

## Requirements

1. Captured request in ngrok
2. Victim IP extracted
3. curl or browser access to ipinfo.io

## Defense

Defensive measures and detection strategies:

- Anonymize internal IPs with proxies or NAT
- Block geolocation API queries from internal systems
- Monitor for IP lookup traffic patterns

## Objectives

1. Extract key victim identifiers
2. Perform geolocation to approximate location
3. Identify potential for additional exploits

## Instructions

### Step 1: Review Ngrok Logs

**Context**: Inspect the incoming request for metadata.

**Instructions**: In http://127.0.0.1:4040, click the request to view headers: IP from remote_addr, browser/OS from User-Agent.

> Expected: Details like IP: 192.0.2.1, User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64).

### Step 2: Query Geolocation

**Context**: Use curl to trace the captured IP.

**Command** ([[commands/curl-ipinfo-geolocation]]):
```bash
curl ipinfo.io/IP-address-of-victim
```

> Replace IP-address-of-victim with the extracted IP (e.g., curl ipinfo.io/192.0.2.1). Expected output: JSON like {"ip":"192.0.2.1","city":"Washington","region":"DC","country":"US","loc":"38.8951,-77.0364"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Network Address Translation Traversal]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ipinfo-geolocation]]

## Tools Used

- [[tools/ngrok]]

## Tags

- analysis
- geolocation
- reconnaissance
