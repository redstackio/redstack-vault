---
tags:
  - authentication
  - multi-device
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
created_at: '[TIMESTAMP]'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.470Z'
sub_techniques: []
id: fd442c4b-874c-4fb6-ac70-4281ab9d5955
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Account-on-Multiple-Devices

## Summary

This procedure establishes active sessions for the same account on two separate devices, setting up the conditions to test session invalidation during MFA changes.

## Description

In the context of testing Grammarly's account security at https://account.grammarly.com/, this step logs in using identical credentials on device A and device B. It leverages standard web authentication to create concurrent sessions, which is typical for user behavior but highlights the lack of session limits in the target environment. Expected outcome is unrestricted access on both devices without interference.

## Requirements

1. Valid username and password for the target Grammarly account.
2. Two devices with web browsers and internet access.
3. No prior MFA enabled on the account.

## Defense

Defensive measures and detection strategies:

- Implement session limits per account to prevent multi-device sprawl.
- Monitor for unusual login patterns across IP addresses or user agents.

## Objectives

1. Create baseline concurrent sessions for testing.
2. Verify multi-device access without automatic logout.
3. Prepare for MFA activation test.

## Instructions

### Step 1: Login on Device A

**Context**: Initiate the first session to establish account access.

Open a web browser on device A and navigate to the login page.

Enter credentials and submit the login form.

> Successful login redirects to the account dashboard, confirming an active session.

### Step 2: Login on Device B

**Context**: Create a second concurrent session to simulate multi-device usage.

Repeat the login process on device B using the same credentials.

> The session on device A should remain active; no logout or warning should occur on either device.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[multi-device]]
- [[web]]
