---
tags:
  - privilege-escalation
  - admin-promotion
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:14.142Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3b0620ac-c2e6-489c-9fb1-2515fac21dd9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Promote-Victim-to-Main-Administrator

## Summary

This procedure elevates the victim's role from standard admin to chief or main administrator in the VK.com app, ensuring they are the primary user whose browser will load and execute the stored XSS payload.

## Description

In VK.com app settings, roles can be adjusted to make a user the main admin, which influences how app details are displayed. This promotion is key to the attack as it positions the victim to view the unsanitized app name on the developer page. Requires prior admin addition.

## Requirements

1. Victim already added as admin
2. Access to app role management
3. Victim's acceptance of initial role

## Defense

Defensive measures and detection strategies:

- Limit role promotions to verified owners only
- Require multi-factor confirmation for privilege changes
- Audit logs for unexpected role escalations

## Objectives

1. Elevate victim's permissions in the app
2. Ensure payload visibility on page load
3. Maximize XSS trigger reliability

## Instructions

### Step 1: Access Role Settings

**Context**: Open the admin roles section.

In app management, navigate to administrator settings.

### Step 2: Promote Victim

**Context**: Select and upgrade the victim's role.

Choose the victim from the list and set as chief/main admin.

### Step 3: Save Changes

**Context**: Apply the promotion.

Confirm and save the role update.

**Expected Output**: Victim's role updated to main admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[admin-promotion]]
