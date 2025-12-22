---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - oauth
  - login
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.115Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Login-to-Existing-Reddit-Account-via-Gmail-OAuth

## Summary

This procedure exploits Reddit's OAuth misconfiguration by logging in with the same Gmail credentials post-logout, granting access to the pre-existing account without verification and achieving takeover.

## Description

Reddit's system fails to distinguish between new and existing accounts during OAuth login if the email is already associated, allowing the attacker to impersonate the legitimate owner. This bypasses traditional password or 2FA checks, relying solely on OAuth provider authentication.

## Requirements

1. Pre-existing Reddit account linked to the target Gmail
2. Access to the Gmail OAuth flow
3. No active session

## Defense

Defensive measures and detection strategies:

- Require explicit account selection or verification during OAuth login for existing emails
- Audit OAuth login events for email collisions and enforce OTP
- Rate-limit OAuth attempts per email

## Objectives

1. Gain unauthorized access to the victim's account
2. Access private data, posts, and settings
3. Demonstrate full takeover impact

## Instructions

### Step 1: Initiate Login

**Context**: Start the login process using OAuth.

Go to https://www.reddit.com/login/ and select "Continue with Google".

> Use the same Gmail account as in signup.

### Step 2: Complete Authentication

**Context**: Observe the misconfiguration in action.

Authorize with Google; Reddit logs you into the existing account without prompting for verification.

> Success: Direct access to the original account dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- login
- account-takeover

---
