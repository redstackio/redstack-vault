---
id: proc-configure-credentials
name: Configure-Credentials-for-Claimed-Service
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.655Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques:
  - '[[Default Accounts]]'
tags:
  - authentication
  - configuration
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Configure-Credentials-for-Claimed-Service

## Summary

This procedure sets up authentication credentials via the web panel of the claimed service on icn.bg, securing exclusive access to the hijacked mail subdomain.

## Description

Once claimed, configure login details in the provider's control panel to prevent others from accessing the profile. This includes setting passwords, API keys, or email auth. It solidifies control in the takeover chain, targeting web-based admin interfaces of mail providers.

## Requirements

1. Access to the claimed profile dashboard
2. Strong password generation
3. Two-factor if available

## Defense

Defensive measures and detection strategies:

- Providers: Require verification beyond DNS for claims
- Organizations: Alert on config changes to subdomains
- Use MFA on all service accounts

## Objectives

1. Establish secure authentication
2. Lock out potential competitors
3. Prepare for service setup

## Instructions

### Step 1: Access Control Panel

**Context**: Log in to icn.bg panel with temporary creds.

Navigate to settings.

> Expected output: Dashboard loaded.

### Step 2: Set Credentials

**Context**: Update password and auth settings.

Enter new credentials in form.

> Expected output: Credentials saved, logout/login test successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[configuration]]
