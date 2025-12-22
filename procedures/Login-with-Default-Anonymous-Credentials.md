---
tags:
  - default-credentials
  - anonymous-access
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-login-nexus-anonymous]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:29:20.504Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
id: 5f9f6db6-0d07-4642-9fa8-463d56e869e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
---
# Login-with-Default-Anonymous-Credentials

## Summary

This procedure authenticates to Nexus Repository Manager using the unchanged default anonymous credentials, granting unauthorized access to repository functions without custom configuration.

## Description

Nexus instances often ship with an enabled anonymous user (username: anonymous, password: anonymous) for testing, but in production, this should be disabled or secured. Attackers exploit this by submitting these credentials via the login form or API, gaining read/write permissions on repositories. The scenario targets misconfigured deployments, leading to outcomes like viewing artifacts, proxying dependencies, and deleting components.

## Requirements

1. Accessible Nexus login endpoint
2. Default anonymous role enabled
3. No CAPTCHA or additional auth layers

## Defense

Defensive measures and detection strategies:

- Disable anonymous access in Nexus settings (Security > Anonymous)
- Change or remove default credentials immediately post-install
- Log failed and successful logins; alert on anonymous usage

## Objectives

1. Bypass authentication using defaults
2. Gain session access to the dashboard
3. Enable repository interactions

## Instructions

### Step 1: Submit Credentials via UI

**Context**: Use the browser to enter defaults and authenticate.

**Command** (Manual UI, simulated with [[commands/curl-login-nexus-anonymous]]):
```bash
curl -u anonymous:anonymous -c cookies.txt https://nexus.imgur.com/static/javascript/nexus/init.js
```

> This authenticates and saves session cookies; success shows JavaScript assets loading without 401 errors.

### Step 2: Verify Authentication

**Context**: Test access to protected resources post-login.

**Command** ([[commands/curl-login-nexus-anonymous]]):
```bash
curl -u anonymous:anonymous https://nexus.imgur.com/service/rest/v1/status
```

> Expected output: JSON with Nexus version and status 'OK', confirming authenticated access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Default Accounts]] Default Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used

- [[commands/curl-login-nexus-anonymous]]

## Tools Used


## Tags

- [[default-credentials]]
- [[anonymous-access]]
- [[auth-bypass]]
