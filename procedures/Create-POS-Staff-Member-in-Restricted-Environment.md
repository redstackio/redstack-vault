---
id: proc-uuid-002
tags:
  - shopify
  - pos-staff
  - account-creation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:20.153Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create POS Staff Member in Restricted Environment

## Summary

This procedure creates a new POS staff account in a Shopify environment where the feature is typically disabled, leveraging the bypassed beta flag to add staff limited to POS app access.

## Description

After enabling the POS staff feature via response modification, this procedure navigates the admin UI to add a new staff member with details like name, email, and PIN. The new account is visible in account settings but lacks broader permissions. This step exploits the absence of server-side checks post-bypass, targeting /admin/settings/account indirectly through the UI.

## Requirements

1. Enabled POS staff management UI from prior bypass
2. Admin session in Shopify
3. Valid email for staff creation
4. Generated PIN for POS access

## Defense

Defensive measures and detection strategies:

- Validate all UI actions server-side against feature flags
- Log and alert on POS staff creations in restricted environments
- Restrict staff creation to high-privilege roles only

## Objectives

1. Add a testable POS staff account
2. Verify feature accessibility post-bypass
3. Set up target for deletion exploitation

## Instructions

### Step 1: Navigate to Management Section

**Context**: Access the now-enabled POS staff area in the UI.

No command; UI navigation:

Click on 'Manage POS staff' in the POS app.

> The section becomes available after the beta flag modification.

### Step 2: Enter Staff Details and Save

**Context**: Input required information to create the account.

Fill form fields:

- First name: e.g., Test
- Last name: e.g., User
- Email: e.g., test@shop.com
- PIN: Generate a 4-digit PIN, e.g., 1234

Click Save.

> The account is created and saved without errors.

### Step 3: Verify in Account Settings

**Context**: Confirm the new staff is listed.

Navigate to /admin/settings/account.

> The POS staff appears below regular staff members.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- pos-staff
- account-creation
