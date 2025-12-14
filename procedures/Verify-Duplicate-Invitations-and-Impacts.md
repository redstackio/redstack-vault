---
id: proc-omise-verify-dups-001
tags:
  - verification
  - impact-assessment
  - duplicates
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.210Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Duplicate Invitations and Impacts

## Summary

This procedure checks the Omise team list and email notifications to confirm successful race condition exploitation resulting in duplicates.

## Description

Post-exploitation, the dashboard's team members section reveals duplicates, and the invitee receives multiple emails. Even after acceptance, entries persist, highlighting business logic flaws. This validation step assesses impact, including errors bypassed for already-invited users. Requires prior exploitation; outcomes confirm vulnerability.

## Requirements

1. Completed race attack with concurrent requests
2. Access to test email inbox
3. Refreshed Omise dashboard session

## Defense

Defensive measures and detection strategies:

- Audit team member lists for duplicates periodically
- Suppress duplicate notifications server-side
- Alert on unusual invitation volumes

## Objectives

1. Inspect team members for duplicates
2. Monitor emails for multiples
3. Test persistence post-acceptance

## Instructions

### Step 1: Check Team Members List

**Context**: Verify UI for duplicate emails.

Refresh team section.

> Same email appears multiple times.

### Step 2: Observe Emails and Errors

**Context**: Confirm side effects.

Check test email; attempt another invite.

> Multiple emails received; error bypassed via race.

### Step 3: Test Post-Acceptance

**Context**: Ensure duplicates remain.

Have invitee accept one; recheck list.

> Duplicates persist.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- impact-assessment
- duplicates
