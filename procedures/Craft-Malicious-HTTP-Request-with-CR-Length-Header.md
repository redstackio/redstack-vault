---
tags:
  - http-request-smuggling
  - node.js
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-malicious-http-request]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 920ea3e2-cd93-425e-b716-a9eee09bd037
created_at: '2025-12-13T09:01:22.542Z'
updated_at: '2025-12-13T09:01:22.542Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious HTTP Request with CR Length Header

## Summary

This procedure involves crafting a malicious HTTP request that includes a carriage return (CR) in the header name, such as Content[CR]Length, to exploit Node.js's conversion of CR to hyphens, leading to HTTP Request Smuggling.

## Description

In this attack, the crafted header is ignored by the front-end proxy as invalid, but Node.js interprets it as Content-Length after conversion, causing desynchronization. This is useful in scenarios with a proxy in front of a Node.js application, enabling smuggling of additional requests.

## Requirements

1. Access to a tool for sending custom HTTP requests, like curl
2. Knowledge of the target proxy and Node.js endpoint
3. Network connectivity to the proxy

## Defense

Defensive measures and detection strategies:

- Update Node.js to patched versions that handle CR in headers correctly
- Use strict header validation in proxies and backends
- Monitor for anomalous HTTP requests with invalid characters

## Objectives

1. Create a request that desynchronizes proxy and backend parsing
2. Enable HTTP Request Smuggling
3. Achieve potential for cache poisoning or XSS

## Instructions

### Step 1: Construct the HTTP Stream

**Context**: Build the request with the malformed header and a follow-up request.

**Command** ([[commands/curl-send-malicious-http-request]]):
```bash
curl -H "Host: target.com" -H "Content\rLength: 42" -H "Connection: Keep-Alive" --data "GET / HTTP/1.1\r\nHost: target.com\r\n\r\n" http://proxy.target.com/
```

> This crafts the request with CR in the header, setting up for smuggling.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-malicious-http-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-request-smuggling]]
- [[node.js]]
