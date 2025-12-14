---
id: proc-120312-verify-creation
tags:
  - verification
  - web
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.341Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Unauthorized Venue Creation

## Summary

This procedure confirms the success of the IDOR exploit by checking that the new venue is created under the unauthorized parent in the Veris application hierarchy.

## Description

Post-submission, verification involves querying the venue list or dashboard to observe the structural changes. This step validates the privilege escalation, as the attacker now has visibility or control over restricted parents. If successful, it indicates full bypass of access controls.

## Requirements

1. Successful submission response from previous step
2. Access to Veris venue management interface
3. Knowledge of the targeted parent ID

## Defense

Defensive measures and detection strategies:

- Audit logs for venue creation events and cross-reference with user permissions
- Real-time hierarchy integrity checks

## Objectives

1. Confirm venue placement under unauthorized parent
2. Assess extended access implications
3. Document proof of exploitation

## Instructions

### Step 1: Refresh Venue List

**Context**: Reload the application to view updated hierarchy.

Navigate to the venues dashboard and refresh or search for the new venue name.

**Expected Output**: New venue listed as child of the unauthorized parent (e.g., ID 456).

### Step 2: Test Access to Restricted Area

**Context**: Attempt interactions with the unauthorized parent to confirm escalation.

Try editing or viewing details under the parent venue.

**Expected Output**: Successful access without permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[web]]
- [[Discovery]]
