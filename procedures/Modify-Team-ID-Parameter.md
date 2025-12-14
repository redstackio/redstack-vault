---
id: proc-slack-modify-teamid-001
tags:
  - parameter-tampering
  - auth-bypass
  - slack
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:30:47.025Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Team-ID-Parameter

## Summary

This procedure alters the team ID parameter in the intercepted Slack signup request to an arbitrary value from another workspace, exploiting lack of validation to target unauthorized workspaces.

## Description

Slack's `api/signup.createUser` endpoint does not properly validate the team ID against the invitation source, allowing replacement with any valid team ID (e.g., from another invitation email). Using the proxy's editor, change the parameter in the request body or headers. This step is key to the auth bypass and only succeeds for workspaces without admin approval. Prerequisites: Intercepted request and target team ID. Outcome: Request now points to unauthorized workspace.

## Requirements

1. Intercepted HTTP request from previous step
2. Target team ID from another workspace invitation
3. Proxy tool with request editing capabilities

## Defense

Defensive measures and detection strategies:

- Validate team ID against invitation token server-side
- Implement request signing or CSRF tokens
- Log and alert on mismatched team IDs in signup requests

## Objectives

1. Replace original team ID with arbitrary one
2. Maintain request integrity for forwarding
3. Enable unauthorized workspace access

## Instructions

### Step 1: Locate Parameter

**Context**: Find the team ID in the request.

In the proxy editor, inspect the POST body (likely JSON) for `team_id` or similar field.

**Expected Output**: Parameter identified, e.g., `"team_id": "T_original"`.

### Step 2: Edit and Save

**Context**: Perform the modification.

Replace the value with the target team ID, e.g., `"team_id": "T_arbitrary_123"`. Ensure JSON remains valid.

**Expected Output**: Updated request body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[parameter-tampering]]
- [[auth-bypass]]
- [[slack]]
