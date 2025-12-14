---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Observe-App-Error-and-Token-Refresh
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:42.685Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Application Access Token]]'
sub_techniques:
  - '[[T1528.001]]'
tags:
  - token-refresh
  - session-persistence
  - mobile-bypass
commands: []
platforms:
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
  - '[[Steal Application Access Token]]'
---

# Observe-App-Error-and-Token-Refresh

## Summary

This procedure tests the Android app's response to revocation by observing initial errors and subsequent automatic token refresh, revealing persistent access via stored keychain sessions.

## Description

Following revocation, the app initially fails due to invalid tokens, but after 20-24 hours (or triggered by notifications), it remints new tokens using a persistent session stored in the device's keychain. This bypasses revocation without needing re-authentication, allowing unauthorized access if an attacker has device access. Tested on Reddit app versions 2022.24.1 to 2022.25.1, it exploits first-party client trust in local storage over server-side invalidation.

## Requirements

1. Recently revoked Reddit Android app access via web
2. Android device with the app installed and session established prior
3. Ability to wait 20-24 hours or simulate triggers like notifications
4. No app reinstallation or device reset

## Defense

Defensive measures and detection strategies:

- Clear keychain sessions on revocation signals from server
- Implement client-side checks for revocation status before refresh
- Log and alert on unexpected token remints post-revocation
- Advise users to log out from app and change passwords for full security

## Objectives

1. Confirm initial access denial after revocation
2. Demonstrate automatic recovery via token refresh
3. Highlight persistence risk without additional authentication

## Instructions

### Step 1: Test Post-Revocation Access

**Context**: Verify the app's immediate failure to access account features.

Reopen the Reddit Android app and attempt actions like loading the feed or profile.

> Errors appear: 'Let's try that again' or 'uh oh something went wrong but we're not sure what'. No user data accessible.

### Step 2: Wait for Automatic Refresh

**Context**: Allow time for the app's background refresh mechanism to activate.

Close the app and wait 20-24 hours. Optionally, trigger via external events like a chat invite notification.

> After delay, reopen app; it performs token refresh using keychain session.

### Step 3: Verify Restored Access

**Context**: Confirm full functionality returns without login.

Interact with app features post-refresh.

> Full access to account, posts, and chats restored seamlessly.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques

- [[T1528.001]] Steal Application Access Token

## Commands Used

- None

## Tools Used

- None

## Tags

- [[token-refresh]]
- [[session-persistence]]
- [[mobile-bypass]]
