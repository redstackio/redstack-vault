---
tags:
  - nextcloud
  - share-expiration
  - unset-date
  - vulnerability
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 366ae681-b71d-4747-bb13-d525a4ef7d57
created_at: '2025-12-14T17:29:09.978Z'
updated_at: '2025-12-14T17:29:09.978Z'
verified: false
validated: true
submitted: true
---
# Unset-Expiration-Date-on-Share

## Summary

This procedure removes the expiration date from a Nextcloud file share, exploiting the vulnerability where this action results in an incomplete or useless audit log entry.

## Description

Unsetting the expiration date via the share settings UI triggers the core vulnerability: while the action succeeds, the admin audit log records only a vague or non-informative entry, potentially concealing administrative changes. This step follows setting an expiration and requires edit access to the share.

## Requirements

1. File share with an existing expiration date
2. Permissions to modify share properties
3. Access to the Nextcloud web interface

## Defense

Defensive measures and detection strategies:

- Patch Nextcloud to fix logging for unset actions
- Implement supplemental logging for share changes
- Conduct regular audits of share configurations manually

## Objectives

1. Remove the expiration date from the share
2. Trigger the logging deficiency
3. Observe the action's success in the UI despite poor logging

## Instructions

### Step 1: Access and Clear Expiration

**Context**: Edit the share to remove the previously set expiration date.

No command required; use the web UI:

- Open the share settings
- Clear the expiration date field
- Click Save

> The share updates without expiration; however, the audit log will show an inadequate entry.

### Step 2: Confirm Removal

**Context**: Verify the change took effect.

No command required; use the web UI:

- Check share details
- Ensure no expiration date is listed

> UI confirmation without errors, but log review (next procedure) reveals the issue.

## MITRE ATT&CK Mapping

### Tactics

- None

### Techniques

- None

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[nextcloud]]
- [[insufficient-logging]]
