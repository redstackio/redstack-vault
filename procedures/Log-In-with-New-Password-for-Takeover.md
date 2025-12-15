---
tags:
  - takeover
  - authentication
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.312Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
id: acb13a1d-7395-4177-8bef-08c5cbeefa6e
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-In-with-New-Password-for-Takeover

## Summary

This final procedure logs in using the attacker-controlled password set via CSRF, achieving full account takeover and access to the victim's resources.

## Description

After CSRF-induced password reset to '████', use the victim's username with the new password at the login endpoint. Success grants control over the account, allowing data exfiltration or further actions. This confirms the vulnerability's exploitability.

## Requirements

1. Victim's username
2. The new password set in the payload (e.g., '████')
3. Confirmed failure of original login

## Defense

Defensive measures and detection strategies:

- Require email/SMS confirmation for password changes
- Anomaly detection on logins post-profile updates
- Session invalidation on sensitive changes

## Objectives

1. Gain authenticated access to the account
2. Demonstrate takeover completeness
3. Access victim-specific data

## Instructions

### Step 1: Submit New Credentials

**Context**: Authenticate with the controlled password.

Go to http://██████████/████████/default.asp and enter:

- Username: [victim_username]
- Password: ████

Submit.

> Expected output: Successful login, redirection to dashboard. Profile now shows updated fields from CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[takeover]]
- [[authentication]]
