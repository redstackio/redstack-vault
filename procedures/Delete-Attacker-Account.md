---
tags:
  - account-deletion
  - dos
  - tumblr
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.418Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0c285ffd-b3e8-44bc-aa17-70e03b6a7cd1
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Delete-Attacker-Account

## Summary

This procedure covers the deletion of the attacker account through Tumblr's settings, which triggers the DoS vulnerability by leaving orphaned messages that break the recipient's message box due to improper backend handling.

## Description

Tumblr allows users to delete their accounts via the account settings page. Upon deletion, all associated data, including sent messages, should be cleaned up. However, in this vulnerability, messages from the deleted account cause the recipient's interface to enter an unusable state, likely due to failed references or resource locks. This results in permanent DoS for the victim's messaging. The deletion is irreversible and immediate, with no recovery option for the attacker account.

## Requirements

1. Logged-in session in the attacker account
2. Web browser access to Tumblr settings
3. Awareness that deletion is permanent

## Defense

Defensive measures and detection strategies:

- Implement graceful handling of deleted user messages (e.g., remove or anonymize threads)
- Monitor for account deletions shortly after messaging activity
- Provide user notifications for messages from deleted accounts

## Objectives

1. Permanently remove the attacker account to activate the flaw
2. Cause uncontrolled resource consumption in the victim's message system
3. Achieve medium-severity DoS without further interaction

## Instructions

### Step 1: Access Account Settings

**Context**: Navigate to the deletion option.

Log in to the attacker account if not already, then go to settings (gear icon) and select "Account" or "Delete account" section.

> Settings page loads, showing account management options.

### Step 2: Initiate Deletion

**Context**: Confirm intent to delete.

Follow prompts to delete the account, entering password if required, and confirm the action.

> Warning dialog appears; proceed by clicking delete.

### Step 3: Verify Deletion

**Context**: Ensure the account is gone.

Attempt to log back in with attacker credentials.

> Login fails with account not found error, confirming success.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-deletion]]
- [[dos]]
- [[tumblr]]
- [[web]]
