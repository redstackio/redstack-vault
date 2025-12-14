---
tags:
  - auth-bypass
  - web
  - exploitation
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
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: c2dcddb8-0407-4c13-acfd-dbde4aeeedd5
created_at: '2025-12-14T17:31:30.766Z'
updated_at: '2025-12-14T17:31:30.766Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reload-Page-to-Trigger-Bypass

## Summary

This procedure finalizes the authentication bypass by reloading the page, allowing the manipulated localStorage state to take effect and grant access to protected resources.

## Description

After setting the localStorage auth flag, the application's client-side logic checks this value on page load. Reloading triggers the check, bypassing password validation and exposing sensitive data. In the DoD application, this leads to viewing user phone numbers and emails without any server-side enforcement.

## Requirements

1. localStorage manipulated from previous procedure
2. Page still open in browser
3. No additional tools beyond browser

## Defense

Defensive measures and detection strategies:

- Enforce server-side token validation on every sensitive API call
- Log and alert on direct localStorage access patterns via client-side monitoring
- Use HttpOnly cookies for auth state to prevent client manipulation

## Objectives

1. Apply the bypassed state
2. Access protected data
3. Confirm unauthorized entry

## Instructions

### Step 1: Refresh the Page

**Context**: Reload to re-execute the client-side auth check with tampered state.

Press Ctrl+R (or Cmd+R on Mac) or click the browser refresh button.

> The login prompt should disappear, and the app should load as if authenticated.

### Step 2: Verify Access

**Context**: Navigate to protected sections to confirm bypass success.

Click on user data links or dashboard elements.

> Expected: Display of sensitive info like emails and phone numbers, without credential prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[auth-bypass]]
- [[web]]
- [[exploitation]]
