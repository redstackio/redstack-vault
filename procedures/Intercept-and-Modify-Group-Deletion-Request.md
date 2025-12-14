---
tags:
  - idor
  - web
  - modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-modify-group-id]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 401133e4-cfca-485a-a8f0-d410640870e3
created_at: '2025-12-14T17:25:23.192Z'
updated_at: '2025-12-14T17:25:23.192Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Group-Deletion-Request

## Summary

This procedure intercepts a legitimate group deletion request in the Veris application and modifies the group_id parameter to target a group from an unauthorized organization, exploiting the IDOR vulnerability.

## Description

Building on the captured request from the initial access, this step uses a proxy to tamper with the HTTP DELETE request by replacing the group_id with one belonging to another organization. The vulnerability stems from the absence of server-side validation for user ownership or organizational boundaries, allowing direct object manipulation. This is typically done in tools like Burp Suite's Repeater. Outcomes include a ready-to-send tampered request that evades authorization, leading to privilege escalation through unauthorized actions.

## Requirements

1. Captured legitimate DELETE request from own organization
2. Knowledge of target group_id from another organization (e.g., via enumeration or prior recon)
3. Proxy tool configured for interception and editing

## Defense

Defensive measures and detection strategies:

- Enforce server-side ownership checks on group_id before processing deletions
- Monitor for unusual parameter changes in API logs using SIEM tools
- Rate-limit deletion requests per user to detect rapid tampering attempts

## Objectives

1. Successfully alter the group_id without breaking the request format
2. Bypass authorization by direct object reference
3. Prepare for execution of unauthorized deletion

## Instructions

### Step 1: Set Up Interception

**Context**: Configure proxy to capture the delete request during UI interaction.

**Command** ([[commands/curl-modify-group-id]]):
```bash
# In Burp Suite or similar, forward the captured request to Repeater
curl -X DELETE 'https://veris.example.com/api/groups/{own-group-id}' -H 'Authorization: Bearer {token}'
```

> Edit the URL or body to replace {own-group-id} with {target-group-id}.

### Step 2: Modify and Validate Request

**Context**: Change the group_id and ensure headers/tokens remain intact.

**Command** ([[commands/curl-modify-group-id]]):
```bash
curl -X DELETE 'https://veris.example.com/api/groups/{target-group-id}' -H 'Authorization: Bearer {token}' -H 'Content-Type: application/json'
```

> Test the modified request in the proxy; expected output is no syntax errors, ready for sending.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-group-id]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[web]]
- [[modification]]
