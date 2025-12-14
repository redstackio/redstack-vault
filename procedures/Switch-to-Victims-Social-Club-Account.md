---
id: proc-003
name: Switch-to-Victims-Social-Club-Account
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.411Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Reversible Encryption]]'
sub_techniques: []
tags:
  - account-takeover
  - mfa-bypass
commands: []
platforms:
  - Gaming
  - Desktop Application
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Reversible Encryption]]'
---

# Switch to Victim's Social Club Account

## Summary

This procedure exploits the Rockstar Games Launcher's failure to re-authenticate during account switching, allowing full takeover of the victim's Social Club account and bypassing MFA.

## Description

Once a game is launched under a linked third-party account, the Launcher provides an interface to switch to the associated Social Club account. Due to improper validation, it assumes the third-party session confirms identity, granting access without passwords or MFA. This leads to complete control over the victim's profile, including game saves, purchases, and linked services. The attack targets the desktop Launcher application in a gaming context.

## Requirements

1. Active session in the Rockstar Games Launcher via the compromised linked account
2. Game launched that integrates with Social Club
3. Victim's Social Club account previously linked to the third-party account
4. No additional tools needed beyond the Launcher

## Defense

Defensive measures and detection strategies:

- Enforce re-authentication and MFA challenges for all account switches in the Launcher
- Implement session token validation tied to device fingerprints
- Monitor for anomalous access patterns, such as switches from linked accounts without prior direct logins

## Objectives

1. Perform the account switch without authentication barriers
2. Gain full privileges on the Social Club account
3. Access all victim data and features post-takeover

## Instructions

### Step 1: Access Account Switching Interface

**Context**: During game launch or in the Launcher menu, locate the Social Club integration prompt.

The Launcher will display an option to 'Sign in to Social Club' or switch accounts based on the detected linkage.

> No credentials are requested due to the vulnerability.

### Step 2: Complete the Switch

**Context**: Select the victim's linked Social Club account to activate it.

Click to switch; the system grants access immediately, even if MFA is enabled on Social Club.

> Full profile loads, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Reversible Encryption]] Multi-Factor Authentication Instrument (Browser-Based)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[account-takeover]]
- [[mfa-bypass]]
