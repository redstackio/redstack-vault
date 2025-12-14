---
id: proc-modify-reencode-node-id
tags:
  - idor
  - graphql
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/base64-encode-modified-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.647Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-and-Re-encode-Node-ID-for-Enumeration

## Summary

This procedure modifies the decoded primary key in a HackerOne GraphQL node ID by incrementing the integer and re-encoding it in base64, allowing attackers to target and enumerate additional EmbeddedSubmissionForm objects via IDOR.

## Description

After decoding reveals the auto-incremental key (e.g., 9), attackers increment it (e.g., to 10) to form a new GID string like `gid://hackerone/EmbeddedSubmissionForm/10`, then base64-encode it. This creates valid node IDs for unauthorized queries, bypassing protections meant to rely on random UUIDs. The target environment is HackerOne's public GraphQL API, with no authentication required.

## Requirements

1. Decoded GID from previous step (e.g., `gid://hackerone/EmbeddedSubmissionForm/9`).
2. Base64 encoder utility.
3. List of sequential integers to test (e.g., 1-100 for enumeration).

## Defense

Defensive measures and detection strategies:

- Enforce UUID-based identifiers to prevent predictability.
- Add authentication checks on node queries.
- Log and alert on sequential node ID access patterns.

## Objectives

1. Generate new node IDs for untargeted forms.
2. Enable broad enumeration of submission forms.
3. Prepare IDs for GraphQL exploitation.

## Instructions

### Step 1: Modify the Primary Key

**Context**: Increment the integer in the decoded GID to target another object.

**Command** (Manual edit):
Edit the string manually: Change `gid://hackerone/EmbeddedSubmissionForm/9` to `gid://hackerone/EmbeddedSubmissionForm/10`.

> This step identifies potential forms by assuming sequential assignment.

### Step 2: Re-encode the Modified GID

**Context**: Base64-encode the new GID to create a queryable node ID.

**Command** ([[commands/base64-encode-modified-id]]):
```bash
echo 'gid://hackerone/EmbeddedSubmissionForm/10' | base64
```

> Outputs `Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vMTA=`, a new node ID for querying.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/base64-encode-modified-id]]

## Tools Used

- None

## Tags

- [[idor]]
- [[graphql]]
- [[enumeration]]
