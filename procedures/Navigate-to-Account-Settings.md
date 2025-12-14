---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - navigation
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.324Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Account-Settings

## Summary

This procedure moves from the MoPub dashboard to the account settings page, exposing vulnerable input fields for XSS injection.

## Description

Following authentication, this step targets the account settings interface in MoPub, where fields like currency and company information lack proper sanitization. The attack scenario involves an authenticated user accessing these fields to prepare for payload injection. Expected outcomes include loading the editable form without restrictions.

## Requirements

1. Active authenticated session in MoPub
2. Web browser
3. No additional privileges needed

## Defense

Defensive measures and detection strategies:

- Log and monitor navigation to sensitive pages like account settings
- Rate-limit access to configuration pages

## Objectives

1. Load the account settings interface
2. Identify vulnerable input fields
3. Enable payload injection

## Instructions

### Step 1: Access Account Menu

**Context**: From the dashboard, locate the menu for account management.

Click on the user profile or account icon in the top navigation bar.

**Expected Output**: Dropdown or menu with 'Account Settings' option appears.

### Step 2: Select Settings

**Context**: Direct the browser to the settings page.

Click 'Account Settings' to navigate.

**Expected Output**: Page loads with input fields for currency, company info, etc.

**Success Indicators**:
- Fields are editable
- Page URL includes /account/settings or similar

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-navigation
- settings-access
