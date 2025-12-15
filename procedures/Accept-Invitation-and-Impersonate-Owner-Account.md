---
tags:
  - impersonation
  - account-switch
  - streamlabs
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.356Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 02737152-a2be-47b0-a51c-9029e65880d7
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Accept-Invitation-and-Impersonate-Owner-Account

## Summary

This procedure involves accepting an admin invitation in Streamlabs and switching to impersonate the owner's account, gaining a dashboard view as the admin.

## Description

Using a separate user account (e.g., MrMax), open the invitation link to accept admin privileges on the owner's account (e.g., MrX). Upon acceptance, the admin can select and view the owner's dashboard, setting the stage for accessing hidden features. This exploits the lack of strict separation between admin and owner views. Prerequisites: The invitation link from the previous procedure and a logged-in admin browser session. Expected outcomes: Successful impersonation without authentication prompts.

## Requirements

1. Invitation link with admin role
2. Separate admin account credentials
3. Web browser session logged in as admin

## Defense

Defensive measures and detection strategies:

- Log all invitation acceptances and account switches
- Enforce session isolation between roles
- Alert on unusual account access patterns

## Objectives

1. Gain admin access to the owner's dashboard
2. Enable lateral movement within the account
3. Position for privilege escalation to restricted settings

## Instructions

### Step 1: Open Invitation Link

**Context**: Use the admin's browser to access and accept the invitation.

Paste the invitation URL (e.g., from shared-access settings) into a browser logged in as the admin user.

> The acceptance page will prompt confirmation of the admin role.

### Step 2: Switch to Owner's Account

**Context**: After acceptance, select the owner's account to impersonate it.

Click on the owner's account name (e.g., MrX) in the post-acceptance interface to load the impersonated dashboard.

> This grants the admin view of the owner's resources without full owner credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation-acceptance
- account-impersonation
