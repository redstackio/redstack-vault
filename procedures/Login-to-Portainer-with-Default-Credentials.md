---
id: proc-login-portainer-defaults
tags:
  - default-credentials
  - auth-bypass
  - portainer
type: procedure
tools:
  - '[[tools/Portainer]]'
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
updated_at: '2025-12-14T17:23:28.053Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Login to Portainer with Default Credentials

## Summary

This procedure exploits unchanged default administrator credentials in Portainer to gain unauthorized access to the Docker management interface, common in misconfigured demo setups like Nextcloud.

## Description

Portainer's default login (admin:password) was not altered, allowing immediate authentication upon accessing the login page. This grants full admin rights to the backend, exposing Docker resources. The attack scenario targets public-facing instances; prerequisites are a confirmed exposed service. Outcomes include dashboard access, enabling container management.

## Requirements

1. Access to the Portainer login page
2. Knowledge of default credentials (admin:password)
3. No additional tools beyond a web browser

## Defense

Defensive measures and detection strategies:

- Change default credentials immediately upon deployment
- Enable multi-factor authentication (MFA) for admin accounts
- Log and alert on failed/successful logins from external IPs

## Objectives

1. Authenticate as administrator
2. Bypass security controls
3. Access the management dashboard

## Instructions

### Step 1: Enter Credentials

**Context**: Submit default username and password via the login form.

No command; interact with the UI: username 'admin', password 'password', click login.

> Upon success, the interface redirects to the backend dashboard.

### Step 2: Confirm Access

**Context**: Verify administrative privileges post-login.

Check for dashboard elements like container lists.

> Indicators include full UI access without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Default Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used

- [[tools/Portainer]]

## Tags

- [[default-credentials]]
- [[auth-bypass]]
