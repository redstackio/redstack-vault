---
id: proc-uuid-001
name: Attempt-Default-Credentials-on-Geoportal-Login
tags:
  - default-credentials
  - auth-bypass
  - web-vuln
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
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.939Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Default-Credentials-on-Geoportal-Login

## Summary

This procedure exploits a misconfigured web application by attempting authentication with unchanged default administrator credentials, granting unauthorized access to administrative functions such as deleting posts and editing website content in a Department of Defense geoportal.

## Description

In this attack scenario, the target is a publicly accessible geoportal application at `https://███/geoportal/` that retains factory-default login credentials post-deployment. An attacker navigates to the login page and tests common default username-password pairs like 'admin/admin' or 'gptadmin/gptadmin'. Successful authentication provides full administrator privileges, allowing manipulation of site content. This vulnerability stems from improper access control and failure to enforce credential changes during setup. Expected outcomes include immediate privilege escalation without additional exploitation, in a web-based environment requiring only a standard browser.

## Requirements

1. Web browser with internet access
2. Knowledge of the target URL (`https://███/geoportal/`)
3. Awareness of common default credentials (e.g., admin/admin, gptadmin/gptadmin)

## Defense

Defensive measures and detection strategies:

- Enforce mandatory credential changes during application deployment and monitor for defaults in configuration audits
- Implement multi-factor authentication (MFA) on all admin interfaces
- Log and alert on failed login attempts, especially with known default patterns
- Use web application firewalls (WAF) to detect brute-force or default credential usage

## Objectives

1. Authenticate as administrator using default credentials
2. Verify elevated privileges by accessing admin functions
3. Demonstrate impact through content deletion or editing

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the vulnerable login interface to begin authentication attempts.

Open a web browser and enter the target URL in the address bar:

```plaintext
https://███/geoportal/
```

> This loads the login form. No command-line tools are required; perform this manually in the browser.

### Step 2: Attempt Default Credentials

**Context**: Test authentication with unchanged default username-password combinations to bypass access controls.

In the login form, enter the following pairs sequentially:

First attempt:
- Username: `admin`
- Password: `admin`

If unsuccessful, second attempt:
- Username: `gptadmin`
- Password: `gptadmin`

Submit the form.

> Successful authentication redirects to the admin dashboard. Failure results in an error message; no further attempts are needed if defaults are confirmed absent, but in this case, they succeed.

### Step 3: Verify Admin Access

**Context**: Confirm privilege escalation by exercising administrative capabilities.

Once logged in, navigate to sections for managing posts or editing content. Attempt to delete a non-critical post or modify a page.

> Expected output includes successful deletion/editing without permission errors, confirming admin rights.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Default Accounts]] Valid Accounts: Default Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used


## Tools Used


## Tags

- [[default-credentials]]
- [[auth-bypass]]
- [[web-vuln]]
