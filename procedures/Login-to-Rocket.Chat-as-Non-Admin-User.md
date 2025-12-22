---
id: proc-uuid-1
tags:
  - authentication
  - rocket-chat
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
updated_at: '2025-12-14T17:29:09.757Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Rocket.Chat-as-Non-Admin-User

## Summary

This procedure authenticates a regular user into the Rocket.Chat instance without administrative privileges establishing a session for exploiting access control vulnerabilities in app management.

## Description

In the context of broken access control in Rocket.Chat the attacker logs in as a non-admin user to gain a valid session. This session is then used to access admin endpoints like app installation without proper authorization checks. The target environment is a standard Rocket.Chat web deployment and the outcome is a authenticated session enabling further unauthorized actions.

## Requirements

1. Valid non-admin username and password for the Rocket.Chat instance
2. Web browser or HTTP client like curl
3. Network access to the Rocket.Chat login endpoint

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) with strict privilege checks on all admin endpoints
- Monitor login events for unusual user agents or IP addresses
- Implement multi-factor authentication (MFA) for all users

## Objectives

1. Establish a valid non-admin session
2. Prepare for unauthorized access to admin features
3. Avoid triggering admin-only login paths

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Rocket.Chat login interface to begin authentication.

**Command** (Manual Browser Action):

Open a web browser and go to `http://<rocket-chat-url>/login`.

> Enter non-admin credentials and submit the form. Expected output: Redirect to user dashboard.

### Step 2: Verify Non-Admin Session

**Context**: Confirm the session lacks admin privileges.

**Command** (Browser Dev Tools):

Inspect the page source or network requests to ensure no admin panels or elevated permissions are visible.

> Expected output: Standard user interface without admin navigation items.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- rocket-chat
