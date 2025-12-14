---
tags:
  - validation-testing
  - api-comparison
type: procedure
tools:
  - '[[tools/node-fetch]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/api-response-without-live]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2eb4091f-ae77-4ffe-b0ba-b8159f5d06f1
created_at: '2025-12-14T17:28:36.439Z'
updated_at: '2025-12-14T17:28:36.439Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-API-Response-Without-Live-Parameter

## Summary

Send a POST request to the TikTok API omitting the 'live' parameter to verify that no data leakage occurs, confirming the vulnerability's dependency on tampering.

## Description

This validation step compares normal API behavior against the exploited one. Without 'live' or with 'live': true, the endpoint returns empty results, highlighting the flaw. Use a modified node-fetch request in a Node.js environment. This isolates the issue to parameter manipulation.

## Requirements

1. Node.js and node-fetch
2. Same authentication as exploitation step
3. API endpoint details

## Defense

Defensive measures and detection strategies:

- Ensure default behavior denies access to inactive data
- Monitor for parameter absence in requests
- Implement comprehensive input validation

## Objectives

1. Confirm restricted access in normal usage
2. Validate exploitation requires specific tampering
3. Document baseline response

## Instructions

### Step 1: Modify Payload

**Context**: Remove 'live' from the JSON body.

**Command** ([[commands/api-response-without-live]]):
```json
{"code":0,"data":{"amount":null,"invited_amount":0},"message":"success"}
```

> This represents the expected response. Send via node-fetch omitting 'live'.

### Step 2: Execute Request

**Context**: Run the test request and log output.

Use a fetch script similar to exploitation but without 'live'.

> Expected output: Success message with null/empty data, no products returned.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/api-response-without-live]]

## Tools Used

- [[tools/node-fetch]]

## Tags

- validation-testing
- api-testing
