---
tags:
  - idor
  - id-manipulation
  - encoding
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
updated_at: '2025-12-14T17:25:48.276Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 700d4cee-9536-4b45-9d10-98892681e6e7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Campaign-ID-for-IDOR

## Summary

Alter the decoded GlobalID by changing the numeric campaign identifier to target an unauthorized campaign, then re-encode to base64 for use in the tampered request.

## Description

The IDOR arises because the backend decodes the base64 but fails to verify ownership. By incrementing or setting the ID to another program's campaign (e.g., from 244 to 500), attackers can reference arbitrary objects. Re-encoding ensures the request format remains valid.

## Requirements

1. Decoded GlobalID string
2. Knowledge of target campaign IDs (e.g., sequential guessing or prior recon)
3. Base64 encoder

## Defense

Defensive measures and detection strategies:

- Validate that the decoded campaign belongs to the user's team_id before processing
- Rate-limit GraphQL mutations and monitor for ID pattern anomalies

## Objectives

1. Create a valid tampered ID
2. Ensure re-encoding matches original format
3. Target a specific unauthorized campaign

## Instructions

### Step 1: Edit the GlobalID

**Context**: Change the numeric part to a desired target.

Example: From 'gid://hackerone/Campaign/244' to 'gid://hackerone/Campaign/500'.

### Step 2: Re-Encode to Base64

**Context**: Prepare for request substitution.

**Command** (base64 encode):
```bash
echo -n 'gid://hackerone/Campaign/500' | base64
```

> Output: Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzUwMA==. Verify by decoding back.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- manipulation
