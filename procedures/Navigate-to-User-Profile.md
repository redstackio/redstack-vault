---
tags:
  - navigation
  - profile
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
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:31:10.989Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 169ad589-6bb3-4731-bca7-420283e63bf0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Navigate-to-User-Profile

## Summary

This procedure moves from the Uber dashboard to the user profile section, positioning the attacker to access notification settings.

## Description

Following authentication, navigation to the profile exposes links to configurable account features. The target is the Uber web interface, with prerequisites including an active session. Success allows reaching pages with embedded authentication tokens.

## Requirements

1. Active authenticated session
2. Standard web browser
3. No ad blockers interfering with UI elements

## Defense

Defensive measures and detection strategies:

- Log profile access events
- Require re-auth for sensitive sections
- Rate-limit navigation patterns

## Objectives

1. Reach profile menu
2. Identify settings links
3. Maintain session integrity

## Instructions

### Step 1: Locate Profile Icon

**Context**: Identify the entry point to account settings.

In the top-right corner of the dashboard, locate the user avatar or profile icon.

> Hovering should show a dropdown preview.

### Step 2: Open Profile Menu

**Context**: Load the profile interface.

Click the icon to expand the menu with options like "Account," "Privacy," and "Help."

> The menu should list navigable sections without additional auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[profile]]
- [[uber]]
