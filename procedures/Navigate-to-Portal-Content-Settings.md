---
tags:
  - shopify
  - settings-navigation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 59257d97-47ae-4349-82bc-a11ecc2f4484
created_at: '2025-12-14T00:11:16.166Z'
updated_at: '2025-12-14T00:11:16.166Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Portal-Content-Settings

## Summary

This procedure guides navigation within the Return Magic app to the Portal Content section, where user-supplied HTML can be edited without sanitization.

## Description

The app's UI uses tabs and sidebars for configuration. Selecting Settings > Portal > Content exposes a textarea vulnerable to stored XSS due to lack of input validation. This positions the attacker to inject payloads targeting other users' sessions.

## Requirements

1. Active session in Return Magic admin dashboard
2. Browser supporting HTML editing
3. Admin privileges in the app

## Defense

Defensive measures and detection strategies:

- Audit app UI changes for unauthorized navigation
- Implement session timeouts for admin interfaces
- Monitor for repeated access to sensitive settings

## Objectives

1. Reach the content editing interface
2. Expose the vulnerable textarea
3. Set up for payload injection

## Instructions

### Step 1: Select Settings Tab

**Context**: Enter configuration mode.

Click the Settings tab at the top of the dashboard.

### Step 2: Choose Portal Section

**Context**: Focus on portal-related options.

From the left menu, select Portal.

### Step 3: Open Content Editor

**Context**: Load the editable content area.

Click Content under Portal to display the textarea and editor tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[settings-navigation]]
