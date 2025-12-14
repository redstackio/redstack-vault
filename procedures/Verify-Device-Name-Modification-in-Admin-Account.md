---
tags:
  - verification
  - impact-check
  - admin-dashboard
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.373Z'
sub_techniques: []
id: bc5622a9-5b33-4063-8472-af3babcc6bb7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Device-Name-Modification-in-Admin-Account

## Summary

This procedure confirms the success of the authorization bypass by logging into the admin account and checking for the unauthorized device name change in the organization dashboard.

## Description

After forwarding the tampered update request, switch to the admin session (A) and refresh the devices list in the organization. The modified name should appear, demonstrating the read-only user's ability to tamper with admin data. This step validates the IDOR vulnerability's impact, limited to name changes but potentially causing management confusion. Prerequisites: Completed tampering step. Expected outcome: Visible alteration without admin notification.

## Requirements

1. Access to admin account A
2. Knowledge of the expected tampered name
3. Browser for dashboard navigation

## Defense

Defensive measures and detection strategies:

- Enable audit trails for all device modifications, notifying admins of changes
- Cross-verify changes via multi-factor approval for sensitive updates
- Periodic permission audits for invited users

## Objectives

1. Access admin dashboard for the target organization
2. Inspect device list for unauthorized changes
3. Confirm bypass impact

## Instructions

### Step 1: Log In to Admin Account A

**Context**: Switch to the victim session.

Open a new browser tab or incognito window, log in to console.helium.com with Account A's credentials.

> Expected: Admin dashboard loads with organization access.

### Step 2: Navigate to Devices in Organization

**Context**: View the affected resources.

Select the organization and go to the Devices section in the UI.

> Expected: List of devices displays.

### Step 3: Check for Name Modification

**Context**: Identify the tampered device.

Scan the device names; locate the one updated from B's session (e.g., "Tampered Name" appears where it shouldn't).

> Expected Output: Name matches the value set in the tampered request.

### Step 4: Document Impact

**Context**: Validate and log the success.

Screenshot or note the change; attempt to revert if testing.

> Success Indicators: Unauthorized name visible, confirming read-only write bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- impact-check
- admin-dashboard
