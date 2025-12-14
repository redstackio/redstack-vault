---
id: proc-mtn-login-admin-001
tags:
  - access-control
  - auth-bypass
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.313Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login to Admin Dashboard

## Summary

This procedure uses newly created unauthorized admin credentials to authenticate and access the MTN Group admin dashboard, gaining full control over application functionalities.

## Description

After registration, the attacker logs in via the standard authentication endpoint, which redirects to the admin dashboard due to improper role-based access controls. This grants visibility and control over features like transaction approvals, leading to potential financial manipulation in the web-based merchant management system.

## Requirements

1. Valid admin credentials from prior registration
2. Access to the login endpoint
3. Web browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin logins
- Log and alert on logins from unusual IPs or new accounts
- Implement session timeouts and role verification

## Objectives

1. Authenticate as admin
2. Redirect to privileged dashboard
3. Access core administrative functions

## Instructions

### Step 1: Submit Login Credentials

**Context**: POST the username and password to the login endpoint.

Example using curl:

```bash
curl -X POST https://target-app.com/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"attacker_admin","password":"strongpass123"}'
```

> Expected output: 200 OK with session token and redirect to /admin/dashboard.

### Step 2: Follow Redirect to Dashboard

**Context**: Use the returned token or follow browser redirect to load the dashboard.

No command; in browser, the page reloads to show admin interface.

> Verify access by checking for merchant list or transaction controls.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web-vuln]]
