---
tags:
  - privilege-escalation
  - shopify
  - pin-modification
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.044Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 08d2222f-e20a-43f3-8493-32a8e81145d8
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Change PIN of Full Permissions Staff in POS

## Summary

This procedure updates the POS PIN for a full-permissions staff account using the limited 'Manage Staff' interface, enabling inheritance of elevated privileges upon re-login.

## Description

Under limited permissions, the POS allows editing of staff details including PINs, without re-validating broader access. This step abuses that to prepare a backdoor PIN, assuming the limited role can view full staff. It requires the POS session from prior steps.

## Requirements

1. Active POS session under limited user
2. Full-permissions staff account existing
3. 'Manage Staff' permission active

## Defense

Defensive measures and detection strategies:

- Restrict PIN changes to owner-only roles
- Audit all staff edits in POS logs
- Validate role permissions before UI edits

## Objectives

1. Set a known PIN for the full staff account
2. Ensure change persists across sessions
3. Avoid triggering permission checks

## Instructions

### Step 1: Access Staff Section

**Context**: Locate the target staff in limited view.

In POS, go to the Staff menu and search for the full-permissions staff from Step 1.

> Staff list displays, allowing selection.

### Step 2: Edit and Update PIN

**Context**: Modify authentication details.

Select the staff, click Edit. Change the POS PIN field to '1234'. Save the updates.

> A success message confirms the PIN change without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[pin-modification]]
