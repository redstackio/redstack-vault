---
tags:
  - cors
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.037Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f387a5fc-d48a-4681-b5e1-3228f030117e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CORS-Misconfiguration

## Summary

This procedure identifies CORS misconfigurations on web APIs by testing cross-origin requests, allowing attackers to bypass the Same Origin Policy and access restricted endpoints.

## Description

In the context of the StudyRoom API at https://studyroom.line.me, this involves sending requests with a forged Origin header to check if the server responds without enforcing origin restrictions. Prerequisites include basic web knowledge and access to developer tools or curl. Expected outcome is confirmation of vulnerable CORS policy enabling unauthorized requests.

## Requirements

1. Internet access to the target API
2. Browser with developer console or curl installed
3. Knowledge of target endpoints (e.g., profile API)

## Defense

Defensive measures and detection strategies:

- Implement strict Access-Control-Allow-Origin headers
- Use CORS preflight checks and validate origins
- Monitor for anomalous cross-origin requests in logs

## Objectives

1. Confirm SOP bypass via CORS
2. Identify exploitable API endpoints
3. Assess potential for data access

## Instructions

### Step 1: Test Cross-Origin Request with Curl

**Context**: Simulate a request from an unauthorized origin to check server response.

Use curl to send a request with a custom Origin header:

```bash
curl -H "Origin: https://evil.com" -H "Access-Control-Request-Method: GET" -X OPTIONS https://studyroom.line.me/api/profile
```

> This preflight request tests if the server allows the method from the fake origin. Expected output: 200 OK with Access-Control-Allow-Origin: * or matching evil.com, indicating misconfiguration.

### Step 2: Verify with GET Request

**Context**: Follow up with an actual GET to confirm data access.

```bash
curl -H "Origin: https://evil.com" https://studyroom.line.me/api/profile
```

> If the response includes profile data without blocking, CORS is vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cors]]
- [[recon]]
- [[web]]
