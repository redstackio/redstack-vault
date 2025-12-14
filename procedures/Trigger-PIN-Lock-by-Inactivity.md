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
updated_at: '2025-12-14T17:31:11.289Z'
skill_level: low
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Trigger-PIN-Lock-by-Inactivity

## Summary

This procedure induces an inactivity period in the Rocket.Chat app to activate the PIN lock, relying on the system time to calculate the timeout and setting the stage for bypass exploitation.

## Description

With the screen lock enabled, this step involves closing the active chat session, recording the current system time, and allowing the timeout to pass. The app's design flaw—using system time instead of an internal counter—means the lock state is tied to absolute time, enabling reversal. Requires physical access; outcomes include the app entering a locked state upon attempted reopen.

## Requirements

1. Screen lock already enabled with timeout (from prior procedure)
2. Physical access to close and wait on the device
3. Ability to observe system clock

## Defense

Defensive measures and detection strategies:

- Implement internal monotonic timers for timeouts to resist clock changes
- Log app inactivity events and correlate with system time anomalies
- Use device security features that lock at OS level independently

## Objectives

1. Force the app into PIN-locked state via simulated inactivity
2. Note the exact system time of lock trigger for later manipulation
3. Confirm the timeout mechanism's dependency on external clock

## Instructions

### Step 1: Close App Activity

**Context**: End user interaction to start the inactivity timer.

Exit the chat window or minimize the app, ensuring no background activity. Note the current device time (e.g., 00:02).

### Step 2: Wait for Timeout

**Context**: Allow the predefined period to elapse.

Do not interact with the app for the set duration (e.g., 1 minute), letting the system time advance to trigger the lock.

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
