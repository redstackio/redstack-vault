---
id: 123e4567-e89b-12d3-a456-426614174003
name: Execute-and-Observe-SSRF-to-Internal-Host
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.228Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - exploitation
commands:
  - '[[commands/undici-request-ssrf-demo]]'
platforms:
  - Node.js
  - JavaScript
tools:
  - '[[tools/undici]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Execute-and-Observe-SSRF-to-Internal-Host

## Summary

This procedure executes the SSRF by triggering undici.request with the malicious pathname, observing the redirection to internal hosts and potential data exposure.

## Description

Once the payload is injected, the server-side request is processed incorrectly, combining the protocol from the origin with the hostname from the pathname, resulting in requests to localhost or other internal resources. This can lead to exposure of metadata, internal APIs, or further chaining to other exploits. Observation involves monitoring network traffic or service logs.

## Requirements

1. Vulnerable application with undici <= 5.8.1
2. Payload from previous procedure
3. Access to monitor internal traffic (e.g., tcpdump or logs)

## Defense

Defensive measures and detection strategies:

- Upgrade to undici 5.8.2 or later
- Network segmentation to block internal requests from app servers
- Implement request logging and anomaly detection for localhost traffic

## Objectives

1. Trigger unauthorized internal requests
2. Observe successful SSRF execution
3. Assess impact on internal services

## Instructions

### Step 1: Execute Malicious Request

**Context**: Run the undici.request with crafted input to initiate SSRF.

**Command** ([[commands/undici-request-ssrf-demo]]):
```javascript
const undici = require("undici");
undici.request({origin: "http://example.com", pathname: "//127.0.0.1"});
```

> This sends a request to http://127.0.0.1/ instead of the expected path on example.com.

### Step 2: Monitor and Verify

**Context**: Check for evidence of internal request.

Use tools like netstat or application logs to confirm traffic to 127.0.0.1.

> Expected: Logs show connection to localhost; potential response data from internal service.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/undici-request-ssrf-demo]]

## Tools Used

- [[tools/undici]]

## Tags

- [[ssrf]]
- [[exploitation]]
