---
tags:
  - http-request
  - malformed-header
  - transfer-encoding
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/http-get-malformed-transfer-encoding]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a41c5c90-ac91-48d6-a262-e168c4eb4d1c
created_at: '2025-12-13T09:01:17.333Z'
updated_at: '2025-12-13T09:01:17.333Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Request with Malformed Transfer-Encoding

## Summary

This procedure involves sending a specially crafted HTTP request with an invalid Transfer-Encoding header to test if the Node.js server parses it incorrectly as valid chunked encoding.

## Description

By setting Transfer-Encoding to 'chunkedchunked' and including a chunked body, the request exploits the llhttp parser's flaw in validating the header value. This can lead to desynchronization in proxy setups. The procedure targets Node.js HTTP servers and requires a running test server from prior steps.

## Requirements

1. Running Node.js HTTP server on localhost:80
2. Tool to send raw HTTP requests (e.g., netcat or curl with raw mode)
3. Knowledge of HTTP request formatting

## Defense

Defensive measures and detection strategies:

- Implement strict header validation in proxies or WAFs
- Log and alert on unusual Transfer-Encoding values

## Objectives

1. Test parsing of invalid headers
2. Confirm vulnerability presence
3. Prepare for smuggling demonstration

## Instructions

### Step 1: Construct and Send the Request

**Context**: This step sends the malformed request to observe server behavior.

**Command** ([[commands/http-get-malformed-transfer-encoding]]):
```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

1
a
0


```

> This request includes the invalid header and a simple chunked body. Expected output is the server accepting it as chunked, with body 'a'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/http-get-malformed-transfer-encoding]]

## Tools Used

- [[tools/Node-js]]

## Tags

- [[http-request]]
- [[malformed-header]]
