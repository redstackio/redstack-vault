---
id: proc-uuid-2-1991214
tags:
  - access-control
  - auth-bypass
  - oracle-apex
  - privilege-escalation
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
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:56.795Z'
skill_level: beginner
impact_level: critical
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Admin-Privileges-in-DoD-App

## Summary

This procedure confirms the successful exploitation of an authentication bypass by checking the active user session and testing administrative functions in the DoD Oracle APEX application, ensuring full control has been obtained.

## Description

Following auto-authentication via the vulnerable URL, this step involves inspecting the user interface to validate the admin role. The session as 'ben auto log user' provides access to sensitive features, including creating submissions with file uploads, viewing all historical data since 2012 (exposing names and emails), managing users (e.g., adding admin roles), sending spam emails, and admin tools for publishing or removing data. This verification step is crucial to assess the scope of compromise and plan further actions like data exfiltration or persistence.

## Requirements

1. Active session from the vulnerable URL access
2. Web browser with the application loaded
3. Basic familiarity with web application interfaces

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) with logging of privilege checks
- Audit user sessions for hardcoded or anomalous logins (e.g., 'ben auto log user')
- Implement multi-factor authentication (MFA) for all admin endpoints
- Regularly scan Oracle APEX apps for misconfigurations in URL handling

## Objectives

1. Validate administrative privileges post-authentication
2. Identify accessible sensitive features for exploitation
3. Confirm the impact on confidentiality and integrity

## Instructions

### Step 1: Inspect User Interface for Session Details

**Context**: Check the top right corner of the application to confirm the logged-in user and role.

No specific command; visual inspection in browser.

Navigate to the loaded page and locate the user profile indicator.

> Look for 'ben auto log user' displayed, indicating admin status. Successful verification shows no standard user limitations.

### Step 2: Test Admin Functions

**Context**: Attempt to access and use admin-exclusive features to ensure privileges are functional.

No command; interact with the UI.

Try actions like viewing historical submissions, adding a user, or uploading a file.

> Expected behavior: All admin actions execute without errors, confirming full access. For example, the submissions history loads data from 2012, exposing sensitive information.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[auth-bypass]]
- [[oracle-apex]]
- [[privilege-escalation]]
