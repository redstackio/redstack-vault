---
id: proc-access-khan-settings-207552
tags:
  - web-access
  - account-settings
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
updated_at: '2025-12-14T17:32:58.257Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Access-Khan-Academy-Account-Settings

## Summary

This procedure outlines how to navigate to the account settings page on Khan Academy using an active logged-in session, setting the stage for unauthorized modifications.

## Description

In the context of exploiting weak authentication, an attacker with brief access to a logged-in session can quickly reach the settings interface. The Khan Academy platform's account settings are accessible via the profile menu without additional barriers. This step is prerequisite for sensitive actions like password changes. Expected outcomes include loading editable forms for account details, with no session timeouts during manual testing.

## Requirements

1. Active logged-in session to a Khan Academy account
2. Web browser with JavaScript enabled
3. Direct access to khanacademy.org without blocks

## Defense

Defensive measures and detection strategies:

- Implement session timeouts and IP binding for logged-in sessions
- Monitor for unusual navigation patterns in account settings access
- Require re-authentication for settings entry via OTP or biometrics

## Objectives

1. Reach the account settings page undetected
2. Prepare for subsequent account manipulation
3. Validate session viability for takeover

## Instructions

### Step 1: Log In and Access Profile

**Context**: Ensure the session is active and click the profile to open the menu.

No command required; perform UI action:

- Click the profile name in the top right corner.

> This opens the dropdown menu. Expected output: Menu with 'settings' option visible.

### Step 2: Select Settings

**Context**: Load the settings page to access forms.

No command required; perform UI action:

- Select 'settings' from the dropdown.

> Page loads with editable fields. Expected output: Settings interface without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[account-access]]
