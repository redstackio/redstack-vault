---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - auth-bypass
  - default-credentials
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Network Device
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:31:19.075Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Authenticate-with-Default-Credentials

## Summary

This procedure exploits unchanged default admin credentials on the Cisco TelePresence SX80 web interface to bypass authentication and gain immediate administrative access, allowing control over video conferencing functions.

## Description

The SX80 ships with default 'admin:admin' credentials that, if not changed, permit unauthenticated access from the internet. Attackers access the HTTPS login page and submit these credentials to enter the dashboard. This is common in misconfigured enterprise devices, especially in legacy setups like DoD environments with infrequent updates. Success grants full control without further exploits.

## Requirements

1. Exposed web interface at https://[IP]
2. Default credentials unchanged
3. Standard web browser for access

## Defense

Defensive measures and detection strategies:

- Enforce credential changes on device provisioning
- Implement multi-factor authentication (MFA) or IP whitelisting
- Monitor login attempts via syslog or SIEM for brute-force patterns

## Objectives

1. Achieve authenticated session as admin
2. Access core device management features
3. Enable subsequent control and exploitation

## Instructions

### Step 1: Access Web Interface

**Context**: Navigate to the device's login page to prepare authentication.

Open a browser and go to https://████████.

> Ignore any self-signed certificate warnings; the login form should appear.

### Step 2: Submit Default Credentials

**Context**: Enter the known defaults to bypass auth.

In the login form, input username: admin, password: admin, then submit.

> Successful login redirects to the admin dashboard with device controls visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Default Accounts]] Default Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- default-credentials
