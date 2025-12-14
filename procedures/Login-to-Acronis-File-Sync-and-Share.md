---
id: login-acronis-fss
tags:
  - initial-access
  - authentication
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
updated_at: '2025-12-14T17:33:12.072Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Acronis-File-Sync-and-Share

## Summary

This procedure authenticates an attacker to the Acronis File Sync & Share application, providing initial access required for subsequent exploitation steps in an account takeover attack.

## Description

The attack begins with legitimate login using attacker credentials to the web-based File Sync & Share service. This establishes a session that can be used to access profile settings and trigger vulnerable API calls. The target environment is the Acronis cloud service at https://mc-beta-cloud.acronis.com, typically used for file sharing and synchronization. Prerequisites include valid attacker credentials and network connectivity. Expected outcomes include a valid session token for dashboard access.

## Requirements

1. Valid attacker username and password for Acronis File Sync & Share
2. Web browser or HTTP client with access to https://mc-beta-cloud.acronis.com
3. No prior session or cookies from victim accounts

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all logins to prevent unauthorized access
- Monitor login attempts from unusual IP addresses or locations using SIEM tools
- Rate-limit login attempts to detect brute-force or anomalous activity

## Objectives

1. Establish authenticated session as attacker
2. Gain access to dashboard and profile features
3. Prepare for API interception in subsequent steps

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the entry point for authentication to the File Sync & Share application.

No specific command; use a web browser to visit https://mc-beta-cloud.acronis.com/fc/access.

> Enter username and password in the provided fields and submit the login form. Successful authentication redirects to the dashboard.

### Step 2: Confirm Session

**Context**: Verify that the login grants access to protected areas.

No specific command; after login, confirm the URL changes to https://mc-beta-cloud.acronis.com/fc/access#/nodes and profile options are visible.

> Look for the dashboard loading with file nodes listed and a profile button in the top right corner.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- web-login
