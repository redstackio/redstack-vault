---
tags:
  - session-persistence
  - bypass
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.465Z'
sub_techniques: []
id: 24d8c332-e787-412e-afb7-71a6ad7e6e75
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Session-Persistence-on-Second-Device

## Summary

This procedure tests whether an existing session on a second device remains valid after MFA activation on another device, confirming the bypass vulnerability.

## Description

On device B, with an active session at https://account.grammarly.com/, perform actions like page reloads or navigation to check for interruptions. The root cause is the failure to revoke session tokens during MFA setup, enabling unauthorized persistence. This step validates the impact without additional tools.

## Requirements

1. Active session on device B prior to MFA activation.
2. MFA already enabled on device A.
3. Web browser on device B.

## Defense

Defensive measures and detection strategies:

- Implement automatic session logout on security changes like MFA enablement.
- Use session monitoring to detect anomalous persistence post-auth changes.

## Objectives

1. Confirm no re-authentication is required on existing sessions.
2. Demonstrate potential for unauthorized access.
3. Highlight the need for session invalidation.

## Instructions

### Step 1: Reload the Page

**Context**: Trigger a potential session check by refreshing the current page.

On device B, press F5 or the reload button while on the account dashboard.

> The page reloads successfully without prompting for MFA or logging out.

### Step 2: Perform Account Actions

**Context**: Test deeper access to ensure full functionality persists.

Navigate to sensitive areas like settings or profile, or attempt a logout simulation by checking session-dependent features.

> All actions complete normally, indicating the session is fully valid and unaffected by MFA.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-persistence]]
- [[bypass]]
- [[verification]]
- [[web]]
