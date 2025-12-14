---
id: '[UUID]'
tags:
  - authentication-bypass
  - pin-bypass
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
updated_at: '2025-12-14T17:31:11.292Z'
skill_level: low
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-Screen-Lock-in-Rocket.Chat-App

## Summary

This procedure configures the screen lock feature in the Rocket.Chat mobile app, setting a timeout period that relies on the device's system time, preparing the environment for a subsequent authentication bypass attack.

## Description

In the context of exploiting the Rocket.Chat mobile app's authentication weakness, this initial step enables the local PIN code protection with a defined inactivity timeout (e.g., 1 minute). The app's implementation uses the device's system clock rather than an internal timer, making it vulnerable to time manipulation. This procedure requires physical access to the device and assumes the app is installed. Expected outcome: The lock mechanism is active, prompting for PIN after inactivity.

## Requirements

1. Physical access to the target mobile device (iOS or Android)
2. Rocket.Chat app installed and logged in with a user account
3. Ability to navigate app settings without restrictions

## Defense

Defensive measures and detection strategies:

- Use apps with internal timers independent of system clock for lock enforcement
- Enable device-level protections like biometric auth over PIN
- Monitor for unusual device time changes via logging or MDM policies

## Objectives

1. Activate PIN-based screen lock to simulate normal security usage
2. Establish a timeout that can be exploited via system time alteration
3. Prepare for verification of lock dependency on external time source

## Instructions

### Step 1: Access App Settings

**Context**: Locate and enter the security configuration area to enable locking.

Navigate to the Rocket.Chat app menu, select Settings, then Security or Screen Lock options. Enable the feature and set a timeout period, such as 1 minute. If prompted, configure a 4-6 digit PIN.

### Step 2: Confirm Configuration

**Context**: Validate that the lock is set up correctly.

Exit settings and interact briefly with the app, then check that the timeout is acknowledged in the UI.

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
- [[rocket-chat]]
- [[mobile-security]]
