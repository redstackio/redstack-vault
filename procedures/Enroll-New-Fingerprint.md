---
tags:
  - android
  - biometric
  - fingerprint
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.203Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e3c5983f-e97b-4c45-a5f0-83e88e0bf52a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enroll-New-Fingerprint

## Summary

This procedure adds a new fingerprint to the Android device, invalidating the Bitwarden app's biometric integrity check as exploited in the vulnerability.

## Description

In the attack scenario, enrolling a new biometric triggers the BiometricIntegrityValid flag to false (per GH-1026), forcing re-authentication. This step requires device settings access and sets up the disable message. Expected outcome: Integrity check invalidated without app access.

## Requirements

1. Android device with fingerprint sensor
2. Existing biometric setup
3. Physical access to enroll new print

## Defense

Defensive measures and detection strategies:

- Limit biometric enrollment changes via policy
- Alert on biometric modifications in enterprise environments
- Update Bitwarden to fix integrity enforcement

## Objectives

1. Add new fingerprint to device
2. Invalidate app's biometric flag
3. Prepare for re-auth prompt

## Instructions

### Step 1: Access Biometric Settings

**Context**: Navigate to add a new fingerprint.

Open Settings > Security (or Biometrics and security) > Fingerprint. Tap 'Add fingerprint' and follow on-screen prompts to scan a new print multiple times.

> New fingerprint enrolled; device recognizes it.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[biometric]]
