---
id: proc-burp-session-verify-001
tags:
  - session-persistence
  - access-verification
  - bypass
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.130Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Persistent-Session-Access

## Summary

This procedure checks if an existing admin session in Burp Suite Enterprise remains valid after a password reset, confirming the vulnerability that allows persistent unauthorized access.

## Description

Following a password change via the admin script, this procedure returns to the original browser session to test access to the admin console. The technical approach relies on the application's failure to invalidate session tokens or cookies upon password reset. In a web-based Java environment, this verifies ongoing admin privileges without re-authentication. Prerequisites: An active session from prior login.

## Requirements

1. Original browser session from the compromised login
2. Access to the admin dashboard URL
3. No new login attempts in the browser

## Defense

Defensive measures and detection strategies:

- Implement automatic session logout on password changes
- Monitor for concurrent sessions from multiple IPs
- Use anomaly detection for prolonged session activity post-reset

## Objectives

1. Test session validity post-password reset
2. Confirm persistent access to admin functions
3. Demonstrate the impact of the session management flaw

## Instructions

### Step 1: Return to Browser Session

**Context**: Switch back to the browser tab or window used for the initial admin login.

No specific command; navigate to the admin dashboard URL if needed.

> The page should load without prompting for credentials, indicating session persistence.

### Step 2: Perform Admin Action

**Context**: Execute a privileged action to validate full access.

No specific command; attempt to view or modify admin settings, such as user permissions.

> Successful execution without authentication challenges confirms the vulnerability. Expected output: Admin features functional as before.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-persistence
- access-verification
