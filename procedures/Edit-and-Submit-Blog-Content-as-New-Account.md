---
tags:
  - content-manipulation
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 07d1f70f-070d-4c72-8a7b-cdef8d697688
created_at: '2025-12-14T17:30:07.255Z'
updated_at: '2025-12-14T17:30:07.255Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Edit-and-Submit-Blog-Content-as-New-Account

## Summary

Edit the draft blog post and submit updates using the new account's session, demonstrating full unauthorized control over the feature.

## Description

With the draft now accessible, the bypass allows arbitrary modifications and submissions, potentially leading to malicious content publication on Lichess.

## Requirements

1. Access to the draft URL
2. Logged-in new account session
3. Form editing capabilities

## Defense

Defensive measures and detection strategies:

- Implement edit permissions tied to creation eligibility
- Scan submitted content for malicious patterns
- Require moderation for new account blogs

## Objectives

1. Modify blog details
2. Confirm submission succeeds
3. Escalate to potential publication

## Instructions

### Step 1: Load Edit Form

**Context**: Open the draft for changes.

On the blog draft page, locate and click any edit options if available, or the form should be pre-loaded.

### Step 2: Edit and Submit

**Context**: Update content to test control.

Change title, body, or add elements, then submit the form.

**Expected Output**: Success message or redirect to updated draft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[content-manipulation]]
- [[web]]
