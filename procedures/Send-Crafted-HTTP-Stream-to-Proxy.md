---
tags:
  - http-request-smuggling
  - proxy
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
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
id: f5ac112a-80bc-45a8-a9a2-31d1d17accc6
created_at: '2025-12-13T09:01:22.541Z'
updated_at: '2025-12-13T09:01:22.541Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Stream to Proxy

## Summary

This procedure sends the maliciously crafted HTTP request to the front-end proxy, which ignores the invalid header and forwards the request assuming a 0-length body.

## Description

The proxy treats the Content[CR]Length as invalid and processes the request without a body, but the smuggled content is forwarded afterward, setting up desynchronization with the Node.js backend.

## Requirements

1. Crafted HTTP request from previous step
2. Target proxy URL
3. Tool for sending HTTP requests

## Defense

Defensive measures and detection strategies:

- Configure proxies to reject requests with invalid headers
- Log and alert on unusual header formats
- Implement request normalization

## Objectives

1. Transmit the request to trigger proxy behavior
2. Ensure partial forwarding of smuggled request
3. Prepare for backend desynchronization

## Instructions

### Step 1: Transmit the Request

**Context**: Send the full crafted stream to the proxy.

**Command** ([[commands/curl-send-malicious-http-request]]):
```bash
curl --path-as-is -i -s -k -X 'GET' -H 'Host: target.com' -H 'Content\rLength: 42' -H 'Connection: Keep-Alive' --data-binary 'GET / HTTP/1.1\r\nHost: target.com\r\n\r\n' 'http://proxy.target.com/'
```

> This ensures the proxy ignores the malformed header and forwards accordingly.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-malicious-http-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-request-smuggling]]
- [[proxy]]
