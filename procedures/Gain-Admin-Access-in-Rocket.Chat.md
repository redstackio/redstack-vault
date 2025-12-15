---
tags:
  - admin-escalation
  - rocketchat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: 73a0bb98-ec3d-4e3c-b643-856168c1cbb4
created_at: '2025-12-14T17:23:36.790Z'
updated_at: '2025-12-14T17:23:36.790Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Gain-Admin-Access-in-Rocket.Chat

## Summary

This procedure outlines how to obtain admin privileges in Rocket.Chat by leveraging self-registration and server creation features, particularly in cloud-hosted environments where any user can spin up a new instance and gain administrative control.

## Description

Rocket.Chat's cloud infrastructure allows users to create personal servers upon registration, automatically granting admin rights on the new instance. For self-hosted deployments, this may involve exploiting weak access controls or chaining with other vulnerabilities like XSS. The procedure assumes network access to the target and focuses on legitimate feature abuse rather than technical exploits, setting the stage for higher-impact attacks like prototype pollution.

## Requirements

1. Internet access to the Rocket.Chat cloud portal or self-hosted URL
2. No prior credentials needed; self-registration is open
3. Browser for UI interaction or API access

## Defense

Defensive measures and detection strategies:

- Disable self-registration and server creation in cloud configs
- Implement role-based access controls (RBAC) with multi-factor authentication (MFA)
- Monitor for unusual admin role assignments in audit logs

## Objectives

1. Secure admin-level access to the Rocket.Chat instance
2. Enable interaction with admin-only endpoints
3. Prepare for privilege-aware exploits like RCE

## Instructions

### Step 1: Register New User

**Context**: Create a basic user account to gain initial foothold.

Navigate to the Rocket.Chat registration page and sign up with arbitrary credentials. No invitation required in default setups.

**Expected Output**: Confirmation email or direct login to user dashboard.

### Step 2: Create Server Instance

**Context**: Use the user portal to spin up a new server, auto-granting admin.

In the cloud dashboard, select 'Create Workspace' or similar; confirm admin role post-creation.

**Expected Output**: New server URL with admin permissions visible in settings.

### Step 3: Verify Admin Access

**Context**: Confirm elevated privileges for subsequent steps.

Access admin panels (e.g., /admin) and check user roles API.

**Expected Output**: Full admin UI and API responses showing 'admin' role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-escalation]]
- [[rocketchat]]
