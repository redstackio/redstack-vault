---
tags:
  - mfa-setup
  - prerequisite
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
updated_at: '2025-12-14T17:24:48.304Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9629ceda-5000-46eb-877a-8681d5537add
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-and-Configure-MFA-on-Target-Account

## Summary

This procedure sets up multi-factor authentication (MFA) on a Grammarly account to enable the vulnerable MFA challenge flow, which is a prerequisite for exploiting the authentication bypass.

## Description

In the context of testing Grammarly's login system, enabling MFA (in SMS or email mode) via the account settings prepares the environment for the MFA bypass attack. This step assumes prior access to the victim's credentials and is typically performed by the victim or an attacker with initial account compromise. The procedure involves navigating to the security settings and toggling MFA on, confirming the setup. Expected outcome: The account now requires MFA for logins, triggering the exploitable POST request.

## Requirements

1. Valid victim credentials (email and password)
2. Access to Grammarly web interface (auth.grammarly.com)
3. Browser or direct web access

## Defense

Defensive measures and detection strategies:

- Monitor account settings changes for unauthorized MFA enablement
- Use anomaly detection on login attempts from unfamiliar IPs

## Objectives

1. Activate MFA to simulate real-world secure login
2. Ensure the target is in a state vulnerable to mode-switching bypass
3. Validate MFA functionality before exploitation

## Instructions

### Step 1: Access Account Settings

**Context**: Log in to the victim's Grammarly account using known credentials to reach the settings page.

Submit login form with email and password to authenticate.

> Expected: Dashboard loads; navigate to 'Settings' > 'Security'.

### Step 2: Enable MFA

**Context**: Locate and activate the MFA option to set the mode (SMS or email).

Toggle MFA on and select mode; follow prompts to verify phone/email.

> Expected: MFA enabled confirmation; future logins will prompt for code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mfa-setup]]
- [[prerequisite]]
