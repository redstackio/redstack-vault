---
id: proc-discover-poc-defaults
tags:
  - default-credentials
  - initial-access
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
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:23:36.747Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Discover-and-Access-Temporary-POC-Site-with-Default-Credentials

## Summary

This procedure involves identifying temporary or staging environments like proof-of-concept sites and gaining access using unchanged default credentials, providing an initial foothold in the target infrastructure.

## Description

In scenarios where development or staging sites are deployed with default configurations, attackers can enumerate such sites through subdomain discovery or directory brute-forcing. For the Starbucks incident, the site alipoc.stg.starbucks.com.cn was accessible publicly with default login credentials, allowing entry without authentication barriers. This step sets the stage for deeper exploitation by establishing a legitimate-looking session.

## Requirements

1. Internet access to the target domain
2. Knowledge of common default credentials (e.g., admin/admin, root/root)
3. Web browser or HTTP client for testing logins

## Defense

Defensive measures and detection strategies:

- Change default credentials immediately upon deployment
- Restrict staging environments to internal networks or VPN
- Implement credential monitoring and rotation policies
- Log all authentication attempts and alert on defaults

## Objectives

1. Gain unauthorized access to the application
2. Establish an authenticated session
3. Identify the site's purpose and available features

## Instructions

### Step 1: Enumerate Staging Subdomains

**Context**: Use passive or active reconnaissance to find temporary sites. Tools like subdomain enumerators can help, but manual inspection of known patterns (e.g., stg, poc) is sufficient here.

Navigate to suspected URLs like alipoc.stg.starbucks.com.cn in a web browser.

### Step 2: Attempt Default Credential Login

**Context**: Test common default pairs on the login form to bypass authentication.

In the login interface, enter credentials such as username: admin, password: admin. Submit the form.

> If successful, the application redirects to a dashboard, confirming access. Failure indicates trying variants like guest/guest or checking source code for hints.

### Step 3: Verify Access

**Context**: Confirm the session is active and explore the interface.

After login, inspect cookies or session tokens and attempt to access admin panels or forms.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Default Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- [[default-credentials]]
- [[staging-environment]]
