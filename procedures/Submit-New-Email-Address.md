---
tags:
  - email-addition
  - unauthenticated
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.987Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8fa18b30-ee1d-4e6b-bf8b-23fed5c8bdcd
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Submit New Email Address

## Summary

This procedure submits an arbitrary email address to a Phabricator account without requiring additional authentication, adding it to the recovery options.

## Description

Leveraging the vulnerable email addition endpoint, the attacker enters a controlled email and submits the form. Phabricator processes this under the existing session without verifying identity further, sending a validation link to the new address. This step is key to the takeover chain.

## Requirements

1. Active session in Phabricator
2. Control over the target email domain/inbox
3. Access to the add email form

## Defense

Defensive measures and detection strategies:

- Mandate password confirmation for email changes
- Rate-limit email additions per session
- Audit logs for unauthorized additions

## Objectives

1. Add controlled email to account
2. Trigger validation email
3. Prepare for reset exploitation

## Instructions

### Step 1: Enter Email

**Context**: Input the new address.

**Instructions**: In the add email form, type the attacker-controlled email (e.g., controlled@evil.com).

> Field accepts input without validation.

### Step 2: Submit Form

**Context**: Process the addition.

**Instructions**: Click 'Add' or 'Submit' button.

> System confirms addition and emails validation link.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[phabricator]]
