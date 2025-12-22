---
id: proc-email-compromise-16696-1
tags:
  - email-compromise
  - initial-access
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
updated_at: '2025-12-14T17:24:45.422Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Compromise-Email-Account-for-Initial-Access

## Summary

This procedure involves breaching a target's email account to gain foundational access for further attacks on linked services, such as financial platforms, by monitoring inboxes and using recovery features.

## Description

In this attack scenario, attackers exploit previously compromised or phished email credentials to log in and perform reconnaissance. The email serves as a central hub for password resets and notifications from services like telecom providers and cryptocurrency exchanges. By reading emails over days, attackers stage the assault, identifying opportunities for account takeovers. This targets web-based email services and assumes external access without physical device compromise. Expected outcomes include full read/write access, enabling subsequent credential resets.

## Requirements

1. Valid credentials or recovery tokens for the target's email account (e.g., via phishing or data breach)
2. Internet access to email provider's web interface
3. Basic knowledge of the target's linked services for reconnaissance

## Defense

Defensive measures and detection strategies:

- Enable email account alerts for login attempts from new locations or devices
- Use hardware security keys for email 2FA to prevent SMS-based bypasses
- Monitor for unusual inbox access patterns via email provider logs

## Objectives

1. Establish persistent access to the target's communications
2. Gather intelligence on linked accounts for lateral movement
3. Enable password resets on dependent services

## Instructions

### Step 1: Log into Compromised Email

**Context**: Use stolen or guessed credentials to access the email account and begin reconnaissance.

Log in to the email provider's web portal using the target's credentials.

> Once logged in, navigate to the inbox and sent items to review historical data.

### Step 2: Monitor and Research

**Context**: Spend time reading emails to identify linked services and prepare for resets.

Review incoming and archived emails for several days, noting services like ATT and Coinbase.

> Focus on security-related emails, such as 2FA setup confirmations or password reset links.

### Step 3: Prepare for Escalation

**Context**: Use email access to initiate resets on linked accounts without triggering immediate alerts.

Compose or forward emails if needed to maintain cover, while collecting reset links.

> Expected output: List of target services with recovery options identified.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-compromise]]
- [[initial-access]]
