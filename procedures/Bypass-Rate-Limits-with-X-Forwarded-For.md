---
id: proc-uuid-5
tags:
  - rate-limit-bypass
  - header-manipulation
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/bypass-rate-limit-with-x-forwarded-for]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Direct Network Flood]]'
updated_at: '2025-12-13T23:55:20.706Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Direct Network Flood]]'
---
# Bypass-Rate-Limits-with-X-Forwarded-For

## Summary

This procedure spoofs the client's IP using the X-Forwarded-For header, which the server reflects and trusts, allowing bypass of IP-based rate limits for high-volume attacks like brute-force or DoS.

## Description

The server uses reflected X-Forwarded-For values for rate limiting without verification, treating requests as from spoofed IPs (e.g., bing.com). This enables unlimited requests from a single source by rotating spoofed values, amplifying other exploits like XSS flooding.

## Requirements

1. Ability to craft HTTP requests with custom headers
2. Target endpoint with rate limits (echo.urbandictionary.biz)
3. Tool like curl for testing

## Defense

Defensive measures and detection strategies:

- Verify X-Forwarded-For against real client IP (e.g., via trusted proxies)
- Implement rate limits based on actual source IP, not headers
- Log and block suspicious header values like domain names in XFF

## Objectives

1. Evade IP-based throttling
2. Send excessive requests without blocks
3. Confirm bypass via response volume

## Instructions

### Step 1: Craft Spoofed Request

**Context**: Add X-Forwarded-For to POST.

**Command** ([[commands/bypass-rate-limit-with-x-forwarded-for]]):
```bash
curl -X POST https://echo.urbandictionary.biz/asd.aspx -H "X-Forwarded-For: bing.com" -d "test"
```

> Server reflects header, treats as from bing.com; repeat to bypass limits.

### Step 2: Rotate Spoofed Values

**Context**: Vary the header to simulate multiple IPs.

**Instructions**: Change to different domains/IPs in subsequent requests.

> Expected: No rate limit hits; high request throughput.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Direct Network Flood]] Direct Network Flood

### Sub-Techniques


## Commands Used

- [[commands/bypass-rate-limit-with-x-forwarded-for]]

## Tools Used


## Tags

- [[bypass]]
- [[dos]]
