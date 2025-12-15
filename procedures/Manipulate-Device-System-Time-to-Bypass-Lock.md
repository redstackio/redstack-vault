---
id: '[UUID]'
tags:
  - authentication-bypass
  - pin-bypass
  - time-manipulation
  - rocket-chat
  - mobile-security
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
  - iOS
  - Android
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.282Z'
skill_level: low
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Manipulate-Device-System-Time-to-Bypass-Lock

## Summary

This procedure adjusts the mobile device's system clock to a time before the PIN lock trigger, exploiting the Rocket.Chat app's use of external time for timeouts to disable the authentication prompt.

## Description

By setting the clock backward (e.g., from 00:02 to 00:01), the app perceives no inactivity timeout has occurred, bypassing the PIN. This targets the root cause: lack of internal timing. Requires physical access and possibly disabling auto-sync; outcomes include reset lock state without re-auth.

## Requirements

1. Device unlocked with access to settings
2. Noted lock trigger time from earlier step
3. Knowledge of how to manually set time on iOS/Android (may need airplane mode)

## Defense

Defensive measures and detection strategies:

- Apps should use relative/internal timers (e.g., monotonic clocks) for security timeouts
- OS-level protections against time changes, like requiring auth for clock adjustments
- Monitor system logs for time modifications and app access patterns

## Objectives

1. Roll back system time to invalidate the lock timeout
2. Exploit the app's improper authentication mechanism
3. Enable seamless re-access without PIN

## Instructions

### Step 1: Access System Settings

**Context**: Prepare to alter the clock.

Open device Settings > General (iOS) or System (Android) > Date & Time. Disable automatic set time if enabled.

### Step 2: Set Backward Time

**Context**: Adjust to pre-lock era.

Manually select a time earlier than the noted lock trigger (e.g., 00:01), then save changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[pin-bypass]]
- [[time-manipulation]]
- [[rocket-chat]]
- [[mobile-security]]
