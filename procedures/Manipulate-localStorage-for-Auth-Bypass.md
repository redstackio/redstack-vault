---
tags:
  - auth-bypass
  - localstorage
  - javascript
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 9660c6b7-aacb-4891-917f-1d7df4c476eb
created_at: '2025-12-14T17:31:30.769Z'
updated_at: '2025-12-14T17:31:30.769Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[JavaScript]]'
---
# Manipulate-localStorage-for-Auth-Bypass

## Summary

This procedure exploits client-side authentication by directly modifying the localStorage to set an authentication flag, bypassing the need for a valid password.

## Description

The vulnerability stems from the application's reliance on localStorage to store the authenticated state (e.g., a key like '█████' set to 'true' upon successful login). By using browser developer tools, an attacker can inspect the JavaScript (revealed via error messages) and manually set this value, tricking the app into granting access. This affects a DoD application, exposing sensitive data like phone numbers and emails.

## Requirements

1. Access to the login page from previous procedure
2. Browser developer tools enabled
3. Knowledge of the specific localStorage key from JS inspection

## Defense

Defensive measures and detection strategies:

- Move authentication state to secure server-side sessions with JWT or cookies
- Validate all client-side state on the server for sensitive operations
- Obfuscate or encrypt localStorage values and detect tampering attempts

## Objectives

1. Identify the auth-related localStorage key
2. Set it to the authenticated value
3. Simulate a logged-in state

## Instructions

### Step 1: Inspect JavaScript for Key

**Context**: Analyze the client-side code to find the localStorage key used for auth state.

Open developer tools (F12), go to Sources tab, and search for 'localStorage' in the JS file.

> Look for code like localStorage.setItem('█████', 'true'); on successful auth. Note the exact key name.

### Step 2: Set localStorage Value

**Context**: Manually update localStorage to bypass auth.

In the Console tab, execute: localStorage.setItem('█████', 'true');

> Confirmation: Run localStorage.getItem('█████') to verify it returns 'true'. No server interaction occurs, confirming client-side only.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[auth-bypass]]
- [[localstorage]]
- [[JavaScript]]
