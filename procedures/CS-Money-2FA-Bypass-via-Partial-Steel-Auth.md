---
tags:
  - auth-bypass
  - 2fa-bypass
  - steam-auth
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
updated_at: '2025-12-14T17:24:45.427Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 699ab1b5-5ac8-486e-847b-87097bed42ea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# CS-Money-2FA-Bypass-via-Partial-Steel-Auth

## Summary

This procedure exploits an improper authentication mechanism on the CS Money platform, allowing attackers to bypass two-factor authentication (2FA) after Steam login to access the 3d.cs.money subdomain and interact with custom background features without full verification. It demonstrates a low-risk vulnerability as the subdomain handles non-sensitive content, but enables unauthorized manipulation of user-specific assets.

## Description

The CS Money platform integrates Steam for authentication and enforces 2FA for main account security. However, the 3d.cs.money subdomain fails to validate full 2FA completion in partial sessions, permitting Prime subscribers to upload or view custom 3D backgrounds via simple browser actions like Ctrl+V. This occurs because session cookies from Steam login persist without 2FA checks on the subdomain, leading to unauthorized access. The attack requires a valid Steam-linked CS Money account but no advanced tools, making it accessible to beginners. Expected outcomes include successful content upload/viewing, though the company assessed impact as low due to lack of sensitive data exposure.

## Requirements

1. Valid Steam account linked to a CS Money profile
2. CS Money Prime subscription (for upload functionality; viewing may work without)
3. Web browser with cookie management capabilities (e.g., Chrome DevTools for clearing)
4. Network access to cs.money and 3d.cs.money

## Defense

Defensive measures and detection strategies:

- Enforce consistent 2FA validation across all subdomains via centralized auth tokens
- Implement session invalidation on logout and cookie clearance with strict same-site policies
- Monitor for anomalous access patterns, such as Steam logins without 2FA completion accessing subdomains
- Use browser fingerprinting or additional checks for partial sessions

## Objectives

1. Gain unauthorized access to 3d.cs.money without completing 2FA
2. Manipulate or view custom backgrounds as a Prime user
3. Demonstrate authentication bypass in a multi-subdomain web application

## Instructions

### Step 1: Login and Enable 2FA

**Context**: Set up the account with 2FA to establish the vulnerability baseline.

Navigate to https://cs.money, log in via Steam, and enable 2FA in account settings by following the on-screen prompts to generate and verify a code.

> Successful 2FA enablement confirms the feature is active for later bypass testing.

### Step 2: Logout and Clear Cookies

**Context**: Reset session state to allow partial re-authentication.

Click the logout button on CS Money, then open browser developer tools (F12), go to Application > Cookies, and delete all entries for cs.money, 3d.cs.money, and steamcommunity.com. Clear cache if needed.

> Browser reload of cs.money should show the login page without auto-auth.

### Step 3: Partial Login Skipping 2FA

**Context**: Exploit the gap in 2FA enforcement post-Steam auth.

Revisit https://cs.money and log in with Steam. When the 2FA prompt appears, ignore it and attempt to proceed to the dashboard.

> Partial session grants limited access without code entry, confirming bypass.

### Step 4: Navigate to 3D Subdomain

**Context**: Test subdomain access with incomplete authentication.

Enter https://3d.cs.money in the browser. The page should load the 3D interface without redirecting to 2FA.

> Interface loads, indicating session validity on subdomain.

### Step 5: Upload or View Custom Backgrounds

**Context**: Perform unauthorized actions on Prime features.

If Prime subscribed, copy an image (Ctrl+C) and paste (Ctrl+V) on the 3D page to upload. View any existing backgrounds.

> Upload succeeds or backgrounds display without auth challenges.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- 2fa-bypass
- steam-auth
- web-vulnerability
