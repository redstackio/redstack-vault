---
id: proc-uuid-002
tags:
  - web-modification
  - authorized-access
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
updated_at: '2025-12-14T03:15:30.786Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Approved-Restaurant-Details

## Summary

This procedure accesses and edits an approved restaurant entry on Zomato to prepare for injecting malicious content, leveraging post-moderation edit permissions.

## Description

Following restaurant creation, this step modifies details in Zomato's web interface. The attack scenario targets the edit functionality, assuming approval grants access. Outcomes include updated profile ready for dish addition. Prerequisites: Approved restaurant and account access.

## Requirements

1. Approved restaurant ID from previous step
2. Zomato login credentials
3. Browser access to restaurant management

## Defense

Defensive measures and detection strategies:

- Revoke edit access after initial approval
- Audit edit logs for frequent changes
- Require re-moderation for significant updates

## Objectives

1. Confirm edit permissions
2. Prepare for dish injection
3. Maintain control over the entry

## Instructions

### Step 1: Access Restaurant Profile

**Context**: Locate and enter edit mode.

Log in to Zomato, search for your restaurant, and click 'Edit' or 'Claim' if needed.

### Step 2: Test Minor Edits

**Context**: Verify edit functionality without triggering alerts.

Update a non-sensitive field like phone number and save.

> Expected output: Changes reflected immediately.

### Step 3: Confirm Persistence

**Context**: Ensure edits are saved server-side.

Refresh the page or log out/in to check if changes persist.

> Expected output: Edits visible post-refresh.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[edit-access]]
- [[web]]
