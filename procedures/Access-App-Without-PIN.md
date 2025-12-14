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
updated_at: '2025-12-14T17:31:11.280Z'
skill_level: low
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-App-Without-PIN

## Summary

This final procedure reopens the Rocket.Chat app after time manipulation, confirming the PIN bypass and granting full access to the user's account and features.

## Description

With the system time reset, the app no longer recognizes the inactivity lock, allowing direct entry to the main interface. This completes the attack, providing unauthorized privileges. Physical access assumed; success yields complete session hijack locally.

## Requirements

1. System time successfully manipulated to pre-lock state
2. Physical access to relaunch app
3. No interference from auto-time sync

## Defense

Defensive measures and detection strategies:

- Validate time sources in apps with secure APIs (e.g., NTP with integrity checks)
- Implement session tokens that expire independently of clock
- Use endpoint detection to flag anomalous app behaviors post-time change

## Objectives

1. Verify bypass effectiveness by PIN absence
2. Achieve full account access and data exposure
3. Demonstrate impact of improper auth implementation

## Instructions

### Step 1: Relaunch App

**Context**: Test the unlocked state.

Open the Rocket.Chat app from the device.

### Step 2: Confirm Access

**Context**: Ensure no auth barrier remains.

Navigate through chats and settings; verify full functionality without PIN prompt.

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
