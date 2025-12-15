---
tags:
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0a71b10e-5c3b-4703-84f1-ae8c8ff2b04d
created_at: '2025-12-14T17:28:51.742Z'
updated_at: '2025-12-14T17:28:51.742Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Edit-Coinbase-Account-Settings-Without-Additional-Auth

## Summary

This procedure modifies Coinbase account settings, such as changing passwords or deleting the account, without requiring further verification, leveraging the persistent bypassed session.

## Description

On the settings page, forms for updates lack secondary auth checks for mobile sessions, allowing alterations that could lead to account takeover or permanent damage. This is due to flawed enforcement in the update endpoints.

## Requirements

1. Access to settings page from prior navigation
2. Valid session token from bypass
3. Knowledge of desired changes (e.g., new password)

## Defense

Defensive measures and detection strategies:

- Mandate MFA or email confirmation for all settings changes
- Audit logs for modifications from mobile user-agents
- Rate-limit and anomaly detection on account edits

## Objectives

1. Alter account credentials for takeover
2. Perform destructive actions like deletion
3. Escalate impact from disclosure to control

## Instructions

### Step 1: Select Modification Option

**Context**: Choose the setting to edit, such as password change.

Locate the password or account section and enter new details.

> Form submits without additional prompts.

### Step 2: Submit and Confirm Changes

**Context**: Execute the update to test bypass persistence.

Click save or update button.

> Changes apply immediately, confirming lack of verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
