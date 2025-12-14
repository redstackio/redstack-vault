---
id: proc-gratipay-attacker-login
tags:
  - authentication
  - gratipay
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
updated_at: '2025-12-14T17:32:57.826Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Gratipay-Attacker-Account

## Summary

This procedure authenticates the attacker to their own Gratipay account, providing access to features like email addition necessary for exploiting the business logic flaw.

## Description

Gratipay, as a web-based payment platform, requires user authentication to manage account settings. Logging in as the attacker sets the stage for submitting manipulated email additions. This step assumes the attacker has a pre-registered account and valid credentials.

## Requirements

1. Valid attacker credentials (username/email and password)
2. Web browser with cookies enabled
3. Access to the Gratipay website

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for logins
- Monitor for unusual login locations or patterns
- Rate-limit login attempts to prevent brute-force

## Objectives

1. Gain authenticated session as attacker
2. Access account dashboard and add-email action
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Navigate to Login

**Context**: Reach the authentication endpoint.

Open a web browser and go to the Gratipay login page (typically /login or similar).

### Step 2: Submit Credentials

**Context**: Provide attacker details to authenticate.

Enter the attacker's email/username and password, then submit the form.

### Step 3: Verify Access

**Context**: Confirm successful session establishment.

Check for redirection to the dashboard; inspect session cookies if needed via developer tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- login
- web-auth
