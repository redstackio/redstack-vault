---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Establish-Reddit-Sessions-and-Revoke-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:42.689Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - session-management
  - authorization
  - web-revocation
commands: []
platforms:
  - Web
  - Android
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Establish-Reddit-Sessions-and-Revoke-Access

## Summary

This procedure establishes active sessions on both Reddit's web and Android app platforms, then revokes app authorization via the web interface, simulating an attempt to terminate mobile access.

## Description

In the context of testing Reddit's session management, this procedure involves manual login to create sessions, navigation to the account activity page, and revocation of the 'Reddit on Android' app. It highlights the first-party OAuth-like authorization flow where revocation should invalidate tokens but fails to address stored keychain sessions. Prerequisites include valid credentials and access to an Android device running the Reddit app (e.g., version 2022.25.0). Expected outcomes include initial success in revocation but setup for observing persistence flaws.

## Requirements

1. Valid Reddit account credentials (username and password)
2. Android device with Reddit app installed (version 2022.24.1 or later)
3. Web browser with access to reddit.com (no VPN or proxy restrictions)
4. No existing revocations or password changes on the account

## Defense

Defensive measures and detection strategies:

- Implement full session invalidation on revocation, including keychain clearance on mobile clients
- Monitor for anomalous token refresh events post-revocation via server-side logging
- Enforce shorter token lifetimes and require re-authentication on sensitive actions

## Objectives

1. Create comparable sessions on web and mobile for testing revocation impact
2. Perform explicit app deauthorization to trigger token invalidation
3. Verify web-side success while setting up mobile persistence observation

## Instructions

### Step 1: Log In to Sessions

**Context**: Authenticate to establish active sessions on both platforms, ensuring the Android app is recognized as authorized.

No specific command; perform manual login:

- Open Reddit Android app and enter credentials.
- Visit reddit.com in browser and log in similarly.

> Successful login grants access to feeds, profile, and chats on both.

### Step 2: Navigate to Account Activity

**Context**: Access the web page listing authorized applications.

Manually navigate to https://www.reddit.com/account-activity.

> Page loads with sections including 'Apps you have authorized', listing 'Reddit on Android'.

### Step 3: Revoke Authorization

**Context**: Select and confirm revocation for the mobile app to invalidate its tokens.

In the apps section, click 'Reddit on Android' and confirm revocation.

> Revocation confirmation appears; web session remains active.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[session-management]]
- [[authorization]]
- [[web-revocation]]
