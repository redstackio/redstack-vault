---
tags:
  - http-request-smuggling
  - exploitation
type: procedure
tools:
  - '[[tools/echo]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-nc-send-request]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 052c3c50-d19f-4927-b82f-3e39830b6a90
created_at: '2025-12-13T09:01:21.676Z'
updated_at: '2025-12-13T09:01:21.676Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Malformed HTTP Request

## Summary

This procedure crafts and sends a malformed HTTP request with a space before the colon in the Content-Length header to exploit the Node.js llhttp parser vulnerability.

## Description

By sending a request violating RFC 7230, this procedure demonstrates how Node.js accepts invalid headers, potentially leading to desynchronization with proxies and HTTP Request Smuggling attacks.

## Requirements

1. Running Node.js server on localhost:5000
2. Tools like echo and nc installed
3. Knowledge of HTTP request formatting

## Defense

Defensive measures and detection strategies:

- Use proxies that strictly validate headers per RFC 7230
- Implement WAF rules to detect malformed headers

## Objectives

1. Exploit the parser by sending invalid request
2. Confirm acceptance of malformed header
3. Enable smuggling of additional requests

## Instructions

### Step 1: Craft and Send Request

**Context**: Use echo to create the raw request string and pipe it to nc for transmission.

**Command** ([[commands/echo-nc-send-request]]):

```bash
echo -en "GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length : 5\r\n\r\nhello" | nc localhost 5000
```

> This crafts a GET request with 'Content-Length : 5' and sends it to the server, including a 5-byte body 'hello'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/echo-nc-send-request]]

## Tools Used

- [[tools/echo]]
- [[tools/nc]]

## Tags

- [[http-request-smuggling]]
- [[exploitation]]
