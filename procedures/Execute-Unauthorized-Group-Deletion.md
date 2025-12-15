---
tags:
  - privilege-escalation
  - data-deletion
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-execute-group-deletion]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.746Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 76277dd9-67d3-48a5-a33b-e34c0a5fd807
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Unauthorized-Group-Deletion

## Summary

This procedure sends a POST request with the deleteGroup[id] parameter to the abused endpoint, deleting groups in arbitrary projects by enumerating sequential IDs.

## Description

Due to insufficient authorization, the server processes the deletion parameter without checking if the user owns the target project or group. Group IDs are sequential (e.g., 95, 96), allowing easy guessing. This leads to data disruption, such as loss of project organization for other users.

## Requirements

1. Target project ID and guessed group ID (start from low numbers like 1 and increment)
2. Authenticated session and CSRF token
3. Ability to verify deletion (e.g., via another account or logs)

## Defense

Defensive measures and detection strategies:

- Validate user permissions for every group action
- Implement ID obfuscation or non-sequential numbering
- Alert on deletion attempts from mismatched projects

## Objectives

1. Delete unauthorized groups to disrupt projects
2. Demonstrate privilege escalation impact
3. Validate full exploit chain

## Instructions

### Step 1: Guess Group ID

**Context**: Enumerate potential group IDs sequentially, starting from 1.

### Step 2: Send Deletion Request

**Context**: Include deleteGroup[id] in the body to trigger deletion.

**Command** ([[commands/curl-execute-group-deletion]]):
```bash
curl -X POST 'https://localize.example.com/pages/create_project/8h' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'CSRFToken=your_csrf_token&deleteGroup[id]=95'
```

> Successful deletion returns no error; verify by checking the project.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-execute-group-deletion]]

## Tools Used


## Tags

- [[privilege-escalation]]
- [[data-deletion]]
