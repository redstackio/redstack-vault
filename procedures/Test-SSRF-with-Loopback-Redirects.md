---
id: proc-test-loopback-ssrf
tags:
  - ssrf
  - loopback
  - testing
type: procedure
tools:
  - '[[tools/nc-netcat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/echo-nc-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.079Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SSRF-with-Loopback-Redirects

## Summary

Test SSRF by targeting loopback addresses to detect internal redirects or server configurations.

## Description

Requesting http://127.0.0.1:81/ via SSRF reveals a 301 redirect, indicating internal handling quirks in the ProxySG.

## Requirements

1. Active SSRF vulnerability
2. Netcat access

## Defense

Defensive measures and detection strategies:

- Block loopback requests in proxy config
- Monitor for 301 responses to internal URIs

## Objectives

1. Probe internal loopback
2. Identify redirect behaviors
3. Uncover config details

## Instructions

### Step 1: Send Loopback Request

**Context**: Target port 81 on loopback.

**Command** ([[commands/echo-nc-ssrf-trigger]]):
```bash
echo -ne "GET http://127.0.0.1:81/ HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80
```

> Expect 301 Moved Permanently, confirming internal access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/echo-nc-ssrf-trigger]]

## Tools Used

- [[tools/nc-netcat]]

## Tags

- [[ssrf]]
- [[loopback]]
- [[testing]]
