---
tags:
  - blind-ssrf
  - enumeration
  - tunneling
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/blind-ssrf-enumeration]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.019Z'
sub_techniques: []
id: bbd80444-c7a2-4cc2-8b3f-17b1b3773554
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Perform-Blind-SSRF-for-Internal-Host-Enumeration

## Summary

This procedure uses blind SSRF over HTTPS to enumerate internal DoD hosts by observing response differences like SSL errors and DNS timeouts, enabling mapping of intranet resources without direct feedback.

## Description

Building on initial SSRF, attackers target known internal IPs (e.g., military networks like NIPERNET) by crafting Host headers that tunnel requests internally. Differences in server responses (timeouts for non-existent hosts, errors for valid ones) allow inference of active infrastructure.

## Requirements

1. Burp Suite for crafting HTTPS-enabled payloads
2. List of potential internal IPs (e.g., from prior leaks)
3. Patience for timing-based analysis

## Defense

Defensive measures and detection strategies:

- Enforce strict internal request validation and IP allowlisting
- Rate-limit and timeout backend connections
- Deploy IDS to detect patterned blind probing

## Objectives

1. Confirm existence of internal hosts via indirect indicators
2. Enumerate accessible intranet segments
3. Identify potential tunneling paths

## Instructions

### Step 1: Craft Blind Payload

**Context**: Modify Host to point to internal targets via attacker domain.

**Command** ([[commands/blind-ssrf-enumeration]]):
```http
GET / HTTP/1.1
Host: www.██████████:80@████████
Pragma: no-cache
Cache-Control: no-cache, no-transform
Connection: close
```

> Send multiple variants; longer DNS timeouts or SSL handshake failures indicate valid internal hosts.

### Step 2: Analyze Responses

**Context**: Compare timing and error patterns.

> Use Burp's timing features to differentiate hits from misses.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/blind-ssrf-enumeration]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- blind-ssrf
- enumeration
- tunneling
