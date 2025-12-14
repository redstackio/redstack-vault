---
tags:
  - path-traversal
  - web-exploit
type: procedure
tools:
  - '[[tools/Developer-Tools]]'
  - '[[tools/Intercepting-Proxy]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.485Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f8923cdb-2729-4321-b197-8091b20b7fb0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Repeat-for-Password-Reset-Endpoint

## Summary

This procedure replicates the path traversal on the /users/password/new endpoint to confirm the vulnerability's scope and consistency.

## Description

The same invitation_token flaw affects the password reset flow, allowing traversal to arbitrary paths. Repeating the test validates multi-endpoint impact and potential for broader CSRF exploitation, such as in OAuth or report-leaking scenarios if combined with other issues.

## Requirements

1. Browser or proxy from prior steps
2. Target password reset URL (e.g., https://hackerone.com/users/password/new)
3. Monitoring tools active

## Defense

Defensive measures and detection strategies:

- Apply uniform input validation across all endpoints using the same parameters
- Audit for shared code paths in authentication flows
- Implement endpoint-specific logging for parameter anomalies

## Objectives

1. Verify traversal on password endpoint
2. Observe identical unauthorized GET behavior
3. Evaluate chaining potential with CSRF

## Instructions

### Step 1: Construct the Vulnerable URL

**Context**: Adapt the payload for the password endpoint.

Enter in browser: https://hackerone.com/users/password/new?invitation_token=/../../test

> The invitation_token payload remains the same, targeting /test.json via traversal.

### Step 2: Access and Inspect

**Context**: Trigger the request and monitor as before.

Visit the URL with network tools active, then check for GET to https://hackerone.com/test.json.

> Success mirrors the confirmation endpoint, indicating systemic validation failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Developer-Tools]]
- [[tools/Intercepting-Proxy]]

## Tags

- [[path-traversal]]
- [[web-exploit]]
