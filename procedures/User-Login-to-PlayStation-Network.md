---
tags:
  - psn
  - authentication
  - login
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
updated_at: '2025-12-14T17:30:35.049Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: d712a00e-2323-49d5-a310-c38a6908cf2c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# User-Login-to-PlayStation-Network

## Summary

This procedure establishes an authenticated session on the PlayStation Network, a prerequisite for exploiting the OAuth token leakage vulnerability by ensuring the authorization flow can proceed with valid credentials.

## Description

The attack scenario begins with the victim logging into PSN via official portals like my.playstation.com or store.playstation.com. This creates a session that the subsequent OAuth implicit grant flow relies on. Without this, the authorize endpoint would prompt for login, potentially alerting the user. The procedure targets web browsers accessing PSN services and assumes no prior session exists.

## Requirements

1. Web browser with internet access
2. Valid PSN credentials (phished or socially engineered from victim)
3. No two-factor authentication blocks (if enabled, additional bypass needed)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on PSN accounts
- Monitor for unusual login locations or devices via PSN security alerts
- Use browser extensions to block third-party popups and trackers

## Objectives

1. Create authenticated session for OAuth exploitation
2. Position victim for seamless token leakage
3. Avoid detection by mimicking legitimate login

## Instructions

### Step 1: Direct Victim to PSN Login

**Context**: Guide the victim to the official PSN login page to establish a session without suspicion.

No specific command; use social engineering (e.g., phishing link) to navigate to https://my.playstation.com or https://store.playstation.com and enter credentials.

> Expected output: Successful login, redirect to PSN dashboard with session cookie set.

### Step 2: Verify Session

**Context**: Confirm the session is active by accessing a protected PSN resource.

Navigate to a authenticated-only page like the user's profile.

> Expected output: Profile loads without re-prompting for login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[psn]]
- [[login]]
- [[authentication]]
