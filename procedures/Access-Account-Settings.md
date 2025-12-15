---
tags:
  - account-takeover
  - web-ui
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:57.807Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2eb8bb9e-6d3e-4136-b466-b7927c0902d2
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Access-Account-Settings

## Summary

This procedure outlines navigating to the account settings in Infogram while in a victim's logged-in session to prepare for unauthorized modifications.

## Description

In scenarios where an attacker gains temporary access to a victim's browser session (e.g., shared device or XSS-induced session), this step involves locating the profile settings to enable further account manipulation. The target is the Infogram web platform, where account details like email are editable without additional checks. Expected outcome is reaching the editable profile page, setting the stage for takeover.

## Requirements

1. Active logged-in session as the victim in a web browser
2. Access to the Infogram dashboard
3. No special permissions beyond standard user access

## Defense

Defensive measures and detection strategies:

- Implement session timeouts and device binding to limit shared access risks
- Monitor for unusual profile access from new IPs or user agents
- Enable multi-factor authentication (MFA) to add recovery layers

## Objectives

1. Gain visibility into account details for modification
2. Position for email change exploitation
3. Confirm session validity

## Instructions

### Step 1: Log In and Navigate to Dashboard

**Context**: Ensure the session is active and reach the main interface.

Open the Infogram website (infogram.com) in the browser where the victim's session is active. If not already on the dashboard, click any link to load the user-specific content.

> No command required; this is UI navigation. Expected: Personalized dashboard loads without login prompt.

### Step 2: Locate Settings Menu

**Context**: Find the entry point to account management.

Click the user avatar or profile icon in the top-right corner to open the dropdown menu. Select "Account Settings," "Profile," or similar option.

> Expected: Settings page loads, showing editable fields including email.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[web-ui]]
