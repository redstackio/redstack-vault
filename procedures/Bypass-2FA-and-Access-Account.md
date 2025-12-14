---
tags:
  - 2fa-bypass
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 31d53226-2905-4ebb-ae8c-6d43a8c9640f
created_at: '2025-12-14T17:24:48.022Z'
updated_at: '2025-12-14T17:24:48.022Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-2FA-and-Access-Account

## Summary

This procedure finalizes the attack by completing the authentication flow, bypassing Cloudflare's 2FA requirements and granting full access to the victim's account dashboard.

## Description

Due to the integration flaw, Cloudflare's system treats the Apple authentication as valid for the existing account without invoking 2FA, as it assumes the email match suffices. This leads to direct session issuance, enabling account takeover. The procedure builds on successful prior steps and is most effective against accounts with enabled 2FA but no Apple linkage.

## Requirements

1. Successful completion of Apple sign-in flow
2. Active session redirect to Cloudflare
3. No additional security prompts interrupting the flow

## Defense

Defensive measures and detection strategies:

- Require 2FA on all alternative authentication paths
- Implement anomaly detection for logins from new identity providers
- Audit and revoke sessions on detected bypass attempts

## Objectives

1. Circumvent 2FA without victim interaction
2. Obtain full unauthorized access to the account
3. Enable further exploitation (e.g., data exfiltration, changes)

## Instructions

### Step 1: Complete Authentication Redirect

**Context**: Allow the OAuth callback to process without interruption.

After Apple authorization, the browser redirects back to Cloudflare's callback URL, where the session is established based on the shared email.

### Step 2: Verify No 2FA Prompt

**Context**: Confirm the bypass by observing the login outcome.

Monitor the page for any 2FA code request; in a successful exploit, none appears, and the dashboard loads directly.

**Expected Output**: Cloudflare dashboard accessible with victim's account privileges.

### Step 3: Validate Account Access

**Context**: Test control by performing account actions.

Navigate to account settings or domain management sections to confirm full access.

**Expected Output**: Ability to view and modify account resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[account-takeover]]
