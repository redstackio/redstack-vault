---
tags:
  - url-crafting
  - auth-bypass
  - line-app
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Desktop (Windows/Mac)
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 50b5b7f7-bb84-4d8e-a7b3-6b5a1b86bc4f
created_at: '2025-12-14T17:24:48.144Z'
updated_at: '2025-12-14T17:24:48.144Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Craft-Malicious-2FA-Bypass-URL

## Summary

This procedure involves creating a specially crafted URL that exploits the absence of ownership checks in LINE's server-side 2FA verification, allowing it to masquerade as a legitimate completion step for the victim's session.

## Description

LINE's 2FA for secondary clients post-QR login lacks validation that the verification originates from the account owner. By inspecting the login flow, an attacker crafts a URL with manipulated parameters (e.g., session tokens from their own QR login) targeted at the victim's account, tricking the server into approving access without further checks. This is effective in desktop environments and requires understanding of LINE's API endpoints.

## Requirements

1. Captured session details from attacker's QR login (e.g., tokens, device IDs)
2. Knowledge of victim's LINE username or account identifier
3. Access to LINE's login URL structure (via reverse engineering or documentation)

## Defense

Defensive measures and detection strategies:

- Add device ownership binding (e.g., IP, device fingerprint) to 2FA endpoints
- Rate-limit and validate URL parameters server-side
- Log and alert on mismatched session origins during verification

## Objectives

1. Generate a URL that bypasses 2FA ownership validation
2. Ensure the URL integrates seamlessly with LINE's login flow
3. Enable unauthorized access upon victim interaction

## Instructions

### Step 1: Analyze Login Flow

**Context**: Identify the 2FA verification endpoint and required parameters.

Manually inspect network traffic during a test QR login using browser tools.

> Note endpoints like /api/v1/2fa/verify and parameters such as token, device_id, user_id.

### Step 2: Modify Parameters for Victim

**Context**: Replace attacker-specific values with victim-targeted ones while retaining exploitable session elements.

Construct the URL manually, e.g., https://line.me/api/2fa/verify?token=attacker_token&user_id=victim_id&device=secondary.

> The missing ownership check allows server approval.

### Step 3: Test URL Structure

**Context**: Validate the crafted URL in a controlled environment.

Send the URL to a test account and observe server response.

> Confirm it triggers 2FA completion without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[url-crafting]]
- [[auth-bypass]]
