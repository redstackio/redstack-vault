---
id: proc-vk-2fa-bypass-001
tags:
  - 2fa-bypass
  - account-takeover
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.831Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass VK 2FA and Gain Account Access

## Summary

This procedure finalizes the VK.com account takeover by leveraging the unverified session reset to skip 2FA and obtain full control over the victim's account.

## Description

Following access to the login endpoint with reset_hash, VK.com's system logs in the associated user without enforcing 2FA or other checks due to insufficient verification. This web vulnerability allows attackers to impersonate the user fully. The scenario assumes prior hash and endpoint steps; outcomes include unrestricted access to private messages, profile data, and actions like changing settings or posting content.

## Requirements

1. Active session from previous reset_hash processing
2. Web browser session persistence
3. Target account with 2FA enabled (to confirm bypass)

## Defense

Defensive measures and detection strategies:

- Enforce 2FA re-verification post-reset
- Audit session logs for anomalous logins without 2FA
- Use device fingerprinting to detect unauthorized sessions

## Objectives

1. Complete login without 2FA intervention
2. Access and control the target account
3. Validate takeover by performing sensitive actions

## Instructions

### Step 1: Process the Session Reset

**Context**: Allow the endpoint to apply the reset and establish the login session.

After loading the reset URL, the system automatically associates the session with the target user. No further input is needed; the browser will redirect to the account dashboard.

> If prompted minimally, proceed without entering credentials—the hash handles authentication.

### Step 2: Verify and Utilize Access

**Context**: Confirm the bypass and explore the account.

Once logged in, navigate to account settings or messages. Attempt actions like viewing 2FA settings to ensure no prompts appear.

> Successful access without 2FA code indicates bypass; use the session to exfiltrate data or modify the account as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[account-takeover]]
