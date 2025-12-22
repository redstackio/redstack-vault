---
tags:
  - idor
  - request-manipulation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-modify-project-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.751Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 38867676-1db4-4df2-947d-0057eca5f70e
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Modify-Request-to-Target-Arbitrary-Project

## Summary

This procedure modifies the project ID in the URL path of the Localize endpoint to target a project not owned by the user, exploiting missing cross-project authorization checks.

## Description

The vulnerability stems from the endpoint directly using user-supplied project IDs without verifying ownership. By changing the path from /pages/create_project/{owned_id} to /pages/create_project/{target_id}, an attacker can interact with foreign projects. This enables IDOR-style access, setting up for deletion in subsequent steps.

## Requirements

1. Valid project ID for a target project (e.g., obtained via enumeration or prior knowledge)
2. Authenticated session and CSRF token
3. Proxy tool or curl for URL manipulation

## Defense

Defensive measures and detection strategies:

- Enforce project ownership validation on all endpoints
- Monitor for requests with mismatched user-project IDs
- Use signed or hashed project references instead of plain IDs

## Objectives

1. Bypass project-specific permissions
2. Confirm endpoint accepts arbitrary project IDs
3. Prepare for parameter injection in target project

## Instructions

### Step 1: Identify Target Project ID

**Context**: Determine a foreign project ID, e.g., '8h' from URL observation or guessing.

### Step 2: Craft Modified Request

**Context**: Alter the URL path to the target project and send a benign request to test acceptance.

**Command** ([[commands/curl-modify-project-id]]):
```bash
curl -X POST 'https://localize.example.com/pages/create_project/8h' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'CSRFToken=your_csrf_token&group_name=test'
```

> Expect a response indicating processing; no errors confirm the IDOR.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-project-id]]

## Tools Used


## Tags

- [[idor]]
- [[request-manipulation]]
