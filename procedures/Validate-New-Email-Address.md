---
tags:
  - email-validation
  - account-manipulation
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
updated_at: '2025-12-14T17:30:58.983Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: c55ae71a-d20e-4a54-a548-046fe1762d82
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Validate New Email Address

## Summary

This procedure validates the added email in Phabricator by clicking the sent link, activating it for use in password resets without victim awareness.

## Description

After submission, Phabricator sends a unique validation link to the new email. The attacker, controlling the inbox, follows this to confirm ownership, integrating the email into the account's recovery options. This bypasses any 2FA on the original account.

## Requirements

1. Access to the controlled email inbox
2. Received validation email from Phabricator
3. Valid session (optional for validation)

## Defense

Defensive measures and detection strategies:

- Notify users via all registered emails on additions
- Require multi-channel approval for validations
- Monitor rapid email changes

## Objectives

1. Activate the new email
2. Enable reset functionality
3. Solidify persistence in account

## Instructions

### Step 1: Access Inbox

**Context**: Retrieve the validation message.

**Instructions**: Log into the controlled email provider and open the Phabricator email.

> Email contains a clickable validation link.

### Step 2: Click Validation Link

**Context**: Confirm the email.

**Instructions**: Follow the link, which redirects to Phabricator's validation endpoint.

> Account settings update to show validated status.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-hijack]]
- [[phabricator]]
