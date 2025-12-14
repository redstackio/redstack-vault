---
tags:
  - login
  - multi-device
  - session-establishment
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
updated_at: '2025-12-14T17:24:47.462Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e9e0bb72-d86a-40d2-bd5c-81cd24011441
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-CS-Money-on-Multiple-Devices

## Summary

This procedure establishes active login sessions for the same CS Money account on two separate devices or browser instances, setting the stage for testing session management behaviors during 2FA activation.

## Description

In the context of exploiting session management flaws, this step simulates legitimate user access across multiple endpoints. By logging in simultaneously on Device A and Device B using the same credentials, active sessions (typically managed via cookies or tokens) are created. This is crucial for demonstrating vulnerabilities where security changes like 2FA enablement do not propagate to invalidate all sessions. The target environment is the CS Money web application, requiring only standard browser access and valid credentials. Expected outcome: Persistent access on both devices pre-2FA.

## Requirements

1. Valid CS Money account credentials (email/username and password)
2. Two physical devices or isolated browser profiles (e.g., incognito modes or different browsers)
3. Internet connectivity to https://cs.money/

## Defense

Defensive measures and detection strategies:

- Implement session monitoring for unusual multi-device logins
- Enforce IP or device fingerprinting to flag simultaneous accesses
- Use anomaly detection for login patterns indicating potential testing or attacks

## Objectives

1. Create authenticated sessions on multiple devices
2. Ensure sessions are fully functional for account actions
3. Prepare for 2FA testing without prior security triggers

## Instructions

### Step 1: Access CS Money on Device A

**Context**: Initiate login on the primary device to establish the first session.

Navigate to https://cs.money/ in a web browser on Device A. Click the login button, enter your username/email and password, and submit the form.

> Upon successful authentication, the dashboard loads, indicating an active session via cookies or local storage.

### Step 2: Repeat Login on Device B

**Context**: Mirror the login process on the secondary device to create a parallel session.

Open https://cs.money/ on Device B, enter the same credentials, and log in. Verify access to account features without conflicts.

> Both devices should now show logged-in status, with no 2FA prompts if not previously enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[multi-device]]
- [[session-establishment]]
