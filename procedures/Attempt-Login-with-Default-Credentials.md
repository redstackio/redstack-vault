---
id: proc-default-creds-login
tags:
  - default-credentials
  - auth-bypass
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
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:29:45.067Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
---
# Attempt-Login-with-Default-Credentials

## Summary

This procedure demonstrates how to bypass authentication on a web application by using default administrator credentials, specifically targeting servers that fail to change or disable default accounts. In this case, it applies to a U.S. Department of Defense server, allowing immediate admin access upon successful login.

## Description

Default credentials are pre-configured usernames and passwords set by vendors for initial setup, often left unchanged in production environments. This procedure involves manually accessing the login endpoint of a target web server, such as one hosted on a .mil domain, and submitting the known default credentials (e.g., username 'Administrator' and a common default password like 'admin' or vendor-specific). The root cause is the failure to enforce password changes or account disabling post-installation, violating CWE-521 (Weak Password Requirements). Successful execution grants administrator privileges to the default organization, enabling potential data exfiltration, configuration changes, or further lateral movement. Prerequisites include public accessibility of the login page and knowledge of the default credentials, which are often publicly documented or guessed from common patterns.

## Requirements

1. Web browser with internet access to reach the target .mil domain
2. Knowledge of the login endpoint URL (e.g., https://example.mil/login)
3. Awareness of default credentials (username: 'Administrator', password: vendor default, redacted here for security)

## Defense

Defensive measures and detection strategies:

- Immediately change all default credentials upon system deployment and enforce strong password policies
- Disable or remove default accounts entirely if not needed
- Implement multi-factor authentication (MFA) on all login endpoints
- Monitor login attempts for failures or suspicious patterns using tools like fail2ban or SIEM systems
- Conduct regular vulnerability scans for default credential exposure using automated tools like credential stuffing detectors

## Objectives

1. Primary objective: Achieve unauthorized login to gain administrator access
2. Secondary objective: Validate admin privileges within the default organization
3. Expected outcome: Full control over the web application's administrative functions, potentially leading to system compromise

## Instructions

### Step 1: Navigate to Login Endpoint

**Context**: Access the public-facing login page of the target DoD server to prepare for credential submission. This step confirms the endpoint is reachable and presents a login form.

No specific command required; use a web browser to visit the URL.

> Open your browser and enter the target URL, such as https://████.mil/████████. Verify the login form loads without errors.

### Step 2: Submit Default Credentials

**Context**: Enter the default administrator username and password to attempt authentication. This exploits the unchanged default settings.

No specific command required; manually input into the web form.

> In the login form, enter username 'Administrator' and the default password (e.g., redacted as _█████_). Click submit or press enter.

> Expected output: Successful authentication, redirect to the admin dashboard showing access to the default organization with elevated privileges.

### Step 3: Validate Access

**Context**: Confirm administrator privileges by performing a simple admin action, such as viewing user lists or system settings.

No specific command required; interact with the dashboard.

> Once logged in, navigate to admin sections (e.g., organization management). Look for indicators like 'Administrator' role or access to sensitive features.

> Expected output: Unrestricted access to admin tools without additional prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- [[default-credentials]]
- [[auth-bypass]]
- [[web]]
