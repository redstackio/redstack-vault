---
id: proc-tealium-reset-ato-001
tags:
  - auth-bypass
  - account-takeover
  - mfa-bypass
  - tealium
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-13T23:55:38.367Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Account-Takeover-via-Tealium-Password-and-MFA-Reset

## Summary

This procedure exploits vulnerabilities in Tealium's password and MFA reset features, allowing any user to reset credentials for arbitrary accounts, leading to unauthorized takeovers and subsequent code modifications.

## Description

Tealium's reset endpoints lack authorization, permitting any authenticated user to target others' accounts by specifying emails or IDs. This facilitates account takeover without phishing or guessing, enabling attackers to act on behalf of victims (e.g., editing tags). Impact shown on Uber's setup. Prerequisites: Any valid Tealium login. Outcomes: Control over target accounts for persistence.

## Requirements

1. Any valid Tealium user account.
2. Target user emails or IDs (from enumeration).
3. Email access if resets send notifications (bypass via social engineering if needed).

## Defense

Defensive measures and detection strategies:

- Require ownership verification (e.g., security questions or 2FA) for resets.
- Rate-limit and log reset attempts, alerting on suspicious patterns.
- Enforce strict auth checks on reset APIs.

## Objectives

1. Reset passwords/MFA for target accounts.
2. Achieve login as the compromised user.
3. Perform actions like tag edits on their behalf.

## Instructions

### Step 1: Identify Target

**Context**: Enumerate potential targets via user lists or public info.

Use existing access to query user details, noting emails for Uber-related accounts.

### Step 2: Initiate Password Reset

**Context**: Submit a reset request without auth barriers.

Access `/reset-password` and provide the target email (e.g., admin@uber.com). The system processes without checks, sending a reset link or token.

For example:

```http
POST /reset-password HTTP/1.1
Host: platform.tealium.com
Content-Type: application/json

{"email": "target@uber.com"}
```

> Response includes a reset token; use it to set a new password.

### Step 3: Reset MFA and Login

**Context**: Similarly bypass MFA reset to fully control the account.

Target the MFA disable endpoint (e.g., `/disable-mfa?user={id}`) with the same lack of checks. Login with new credentials.

**Expected Output**: Successful login and access to account features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[account-takeover]]
- [[mfa-bypass]]
- [[tealium]]
