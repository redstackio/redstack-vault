---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - access-bypass
  - redirect
  - privilege-escalation
  - web
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
updated_at: '2025-12-14T17:29:44.445Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Admin Session via Vulnerable Redirect

## Summary

This procedure exploits an improper access control vulnerability in Oracle APEX by accessing a specific page (p=165:56), which automatically redirects to the admin portal (page 45) and grants admin privileges without authentication.

## Description

The vulnerability stems from flawed session management in the Oracle APEX platform, where page 56 provides a valid admin session upon access. This can be triggered directly or via a related endpoint like /apexcrrel/DISDI_PORTAL_DEV.login_admin from another application page. In a DoD-hosted environment, this allows external attackers to gain admin access, impacting confidentiality, integrity, and availability.

## Requirements

1. Web browser in the same session as the verification step
2. Direct URL access to https://████.mil/apexcrrel/f?p=165:56
3. No authentication tokens or cookies from prior admin access

## Defense

Defensive measures and detection strategies:

- Enforce authentication checks on all redirects and session initializations
- Audit Oracle APEX page configurations for hardcoded privileges
- Monitor for anomalous redirects to admin pages and implement least-privilege principles

## Objectives

1. Bypass authentication to establish an admin session
2. Redirect to the admin dashboard without credentials
3. Validate session elevation

## Instructions

### Step 1: Access the Vulnerable Page

**Context**: Navigate to the page that triggers the unauthorized admin session.

No specific command required; use browser navigation.

```plaintext
Visit: https://████.mil/apexcrrel/f?p=165:56
```

> The application will automatically redirect to https://████.mil/apexcrrel/f?p=165:45, loading the admin portal with elevated privileges. Check browser developer tools for the redirect (e.g., 302 status) and confirm no login prompt appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oracle-apex
- redirect-bypass
- admin-escalation
