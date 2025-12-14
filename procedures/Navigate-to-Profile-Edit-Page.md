---
tags:
  - navigation
  - profile-edit
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.679Z'
sub_techniques: []
id: 80ca9913-13bf-4294-aacc-7316cc4ca4d9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Profile-Edit-Page

## Summary

This procedure describes moving from the Uber Partners dashboard to the profile edit page, where vulnerable input fields like VAT number can be accessed.

## Description

After authentication, the attacker must locate and access the profile settings. This involves clicking on user menu options or direct URL navigation to https://partners.uber.com/profile/. The target environment is the web-based Uber Partners Portal, and success enables interaction with editable form fields. Prerequisites include an active session.

## Requirements

1. Active authenticated session in Uber Partners Portal
2. Web browser navigation capabilities
3. No ad blockers interfering with site functionality

## Defense

Defensive measures and detection strategies:

- Rate-limit navigation to sensitive pages to prevent automated probing
- Log access to profile edit pages for unusual patterns

## Objectives

1. Reach the profile edit interface
2. Expose input fields for manipulation
3. Confirm the presence of the VAT number field

## Instructions

### Step 1: Locate Profile Option

**Context**: From the dashboard, find the link to profile settings.

No command required; click on the user avatar or 'Profile' link in the navigation menu.

> The browser should load the profile view page.

### Step 2: Access Edit Mode

**Context**: Switch to editable form if not already in edit mode.

No command required; click the 'Edit Profile' button or directly navigate to https://partners.uber.com/profile/.

> The edit form loads with input fields, including VAT number.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- navigation
- profile-edit
