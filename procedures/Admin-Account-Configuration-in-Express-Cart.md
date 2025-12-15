---
id: proc-002
tags:
  - authentication
  - admin-setup
  - session
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.173Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Admin-Account-Configuration-in-Express-Cart

## Summary

This procedure configures an admin account in the local express-cart instance, establishing a session-based authentication that can be exploited via CSRF due to missing token validation.

## Description

Access the setup endpoint to create the initial admin user. The authentication in lib/auth.js (around line 60) checks only sessions, making it vulnerable to forgery. This step is essential for simulating an authenticated victim in the attack chain.

## Requirements

1. Local server running on localhost:1111
2. Browser with dev tools for session inspection
3. No prior accounts in the MongoDB database

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls
- Log all admin account creations
- Enforce multi-factor authentication for admins

## Objectives

1. Create an admin user profile
2. Establish a valid session cookie
3. Verify access to admin dashboard

## Instructions

### Step 1: Access Setup Endpoint

**Context**: Navigate to the admin setup page to initiate user creation.

**Command** (Browser Navigation):
No CLI command; use a web browser to visit http://localhost:1111/admin/setup.

> Fill in the form with username, email, and password. Submit to create the account. Expected output: Redirect to login or dashboard.

### Step 2: Authenticate Session

**Context**: Log in to generate the session cookie.

**Command** (Browser Login):
Enter credentials at the login prompt.

> Successful login sets a session cookie (e.g., connect.sid). Expected output: Access to /admin routes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- admin-setup
- session
