---
id: proc-access-edit-acronis-001
tags:
  - web-navigation
  - account-management
  - csrf-prereq
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.627Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Account Edit Page in Acronis Academy

## Summary

This procedure details navigating to the account edit interface in Acronis Academy, where contact information can be managed, setting the stage for vulnerability analysis and exploitation.

## Description

The Acronis Academy application uses a single-page application (SPA) structure with hash-based routing (#/account/edit). Accessing this page requires an active session and the victim's account ID. This step enables viewing and modifying contacts, essential for adding data to exploit the CSRF deletion flaw. Technical approach involves direct URL navigation post-authentication.

## Requirements

1. Active authenticated session
2. Knowledge of the victim's account ID (e.g., from URL or profile)
3. Web browser supporting JavaScript

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) to limit edit permissions
- Log all account page accesses for anomaly detection
- Use CSRF tokens on navigation to sensitive pages

## Objectives

1. Load the contact management interface
2. Confirm edit capabilities for contacts
3. Identify contact IDs for targeting

## Instructions

### Step 1: From Dashboard, Locate Account Settings

**Context**: Find the link to account management.

Click on the user profile or settings icon in the dashboard.

> This should lead to account overview.

### Step 2: Navigate to Edit Endpoint

**Context**: Use the specific URL to access contact editing.

Enter or navigate to https://academy.acronis.com/#/account/edit/account_id/<victim_account_id>, replacing <victim_account_id> with the actual ID.

> The page loads with forms for email, telephone, fax, address, and Skype.

### Step 3: Verify Access

**Context**: Ensure the interface is functional.

Inspect the page for editable fields and any existing contacts.

> Success: Fields are present and savable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-navigation
- account-edit
