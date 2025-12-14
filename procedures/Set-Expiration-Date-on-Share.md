---
tags:
  - nextcloud
  - share-expiration
  - set-date
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9efc9bf8-a48f-4c9c-8147-4ed8c5aade72
created_at: '2025-12-14T17:29:09.985Z'
updated_at: '2025-12-14T17:29:09.985Z'
verified: false
validated: true
submitted: true
---
# Set-Expiration-Date-on-Share

## Summary

This procedure configures an expiration date on an existing Nextcloud file share, which serves as a control to verify proper audit logging before testing the unset action.

## Description

Setting an expiration date on a share involves editing the share properties via the UI, entering a specific date. This action is expected to generate a detailed audit log entry, contrasting with the subsequent unset vulnerability. It requires access to the share settings and is performed in the web interface.

## Requirements

1. Existing file share created in Nextcloud
2. Permissions to edit share properties
3. Browser with access to the sharing interface

## Defense

Defensive measures and detection strategies:

- Log all share modifications, including expiration changes
- Enforce expiration policies for sensitive shares
- Alert on frequent share edits

## Objectives

1. Apply a valid expiration date to the share
2. Confirm the change is reflected in the UI
3. Establish a logged baseline action

## Instructions

### Step 1: Edit Share Settings

**Context**: Access the share and locate the expiration field to set the date.

No command required; use the web UI:

- Open the share details
- Find the "Expiration date" option
- Enter a date (e.g., 2023-10-08)
- Click Save

> The UI updates to show the expiration date; this should create a proper log entry.

### Step 2: Validate Change

**Context**: Ensure the expiration is applied correctly.

No command required; use the web UI:

- Refresh the share view
- Verify the date is displayed

> No errors indicate successful setting.

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
- [[share-expiration]]
