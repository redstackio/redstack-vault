---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - auth-bypass
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.079Z'
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
# Bypass-Authentication-Using-Non-Expiring-Verification-Link

## Summary

This procedure reuses the verification link after activation to log in as the victim without credentials, achieving account takeover via persistent URL auth.

## Description

The link's validity does not end post-activation; accessing it again authenticates solely on URL params (user ID, code, email), bypassing password checks. Risks amplify on shared devices where URLs log in history.

## Requirements

1. Previously obtained verification URL
2. New browser session or incognito mode
3. Victim's account context

## Defense

Defensive measures and detection strategies:

- Invalidate links after single use
- Require additional auth factors post-link
- Monitor for anomalous logins from verification endpoints

## Objectives

1. Gain unauthorized session access
2. Demonstrate non-expiration flaw
3. Enable account takeover

## Instructions

### Step 1: Prepare New Session

**Context**: Ensure clean state to test bypass.

Open incognito window or clear cookies; log out if logged in.

> Simulates attacker accessing from another device.

### Step 2: Reuse Verification Link

**Context**: Trigger auth via the persistent link.

Paste and access the full URL (e.g., https://www.zomato.com/verify?fbcid=BASE64STRING).

> App authenticates directly, granting session access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[session-hijacking]]
