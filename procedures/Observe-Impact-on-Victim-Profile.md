---
tags:
  - impact
  - disclosure
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 0132d9d0-6b30-47f8-9c7f-b1635fe066df
created_at: '2025-12-14T17:25:47.342Z'
updated_at: '2025-12-14T17:25:47.342Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Observe-Impact-on-Victim-Profile

## Summary

This verification procedure checks the victim's HackerOne profile for unauthorized public feedback and monitors email for disclosed private information, confirming the IDOR success.

## Description

Post-exploitation, the public review appears under the victim's 'What Programs Say' section, damaging reputation. The victim receives an email with private feedback and report title. This step validates the attack on the web profile and email system, with no additional tools needed beyond profile access.

## Requirements

1. Access to victim's profile (public) and email (if controlled)
2. Knowledge of submitted feedback content
3. Time for email delivery (~1-2 minutes)

## Defense

Defensive measures and detection strategies:

- Audit feedback postings for authorization anomalies
- Notify users of profile changes and review email logs

## Objectives

1. Confirm unauthorized public review visibility
2. Verify information disclosure via email
3. Assess reputation impact

## Instructions

### Step 1: Check Victim's Profile

**Context**: Navigate to the profile to view feedback section.

Log in or view publicly the victim's HackerOne profile and scroll to 'What Programs Say'.

### Step 2: Monitor Victim's Email

**Context**: Observe notifications for private details.

Check the victim's email for HackerOne notification containing private feedback and report title.

**Expected Output**: Public comment 'Japz is awesome :)' on profile; email with 'Thanks for your report.' and report details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Impact]]
- [[disclosure]]
- [[web]]
