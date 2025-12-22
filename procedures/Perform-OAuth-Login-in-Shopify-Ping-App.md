---
tags:
  - oauth
  - android
  - login
type: procedure
tools:
  - '[[tools/okhttp]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/oauth-browser-redirect]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:45.107Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8eb83f2d-19f2-4481-b443-2fc99e301f8c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-OAuth-Login-in-Shopify-Ping-App

## Summary

This procedure simulates the login flow in the Shopify Ping Android app, initiating an OAuth authorization code grant via browser redirect to obtain an authorization code for subsequent token exchange.

## Description

In the Shopify Ping app, login is triggered by creating an Android intent to open the default browser at https://accounts.shopify.com/. After user authentication, the server redirects to the app's custom URI scheme with an authorization code. This step is prerequisite for token acquisition and exploits the app's reliance on PKCE for mobile OAuth. Expected outcome is receipt of a valid code, observable via app debugging or proxy interception.

## Requirements

1. Android device with Shopify Ping app installed (version 2.10.0 or similar)
2. Network access to accounts.shopify.com
3. Ability to intercept app-browser interactions (e.g., via ADB or proxy)

## Defense

Defensive measures and detection strategies:

- Enforce PKCE in all mobile OAuth flows to prevent code interception
- Monitor for unusual browser launches from apps
- Use certificate pinning to block proxy interception

## Objectives

1. Obtain authorization code for token exchange
2. Establish initial authenticated session
3. Prepare for token-based API access

## Instructions

### Step 1: Trigger Login Intent

**Context**: Launch the app's login activity to open the browser for Shopify authentication.

**Command** ([[commands/oauth-browser-redirect]]):
```bash
# Simulate via ADB or app trigger: am start -a android.intent.action.VIEW -d https://accounts.shopify.com/ com.shopify.ping
```

> This opens the browser; complete login to receive redirect: com.shopify.ping://auth/callback?code=ABCDEFG&state=**************. Expected output: App handles callback and extracts code.

### Step 2: Capture Callback

**Context**: Intercept the redirect to retrieve the authorization code.

**Command** (Manual observation):
```bash
# Via logcat or proxy: adb logcat | grep callback
```

> Expected output: Code parameter visible in URI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/oauth-browser-redirect]]

## Tools Used

- [[tools/okhttp]]

## Tags

- oauth
- android
- login
