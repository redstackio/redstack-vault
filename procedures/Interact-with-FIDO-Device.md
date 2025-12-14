---
tags:
  - fido
  - hardware
  - u2f
type: procedure
tools:
  - '[[tools/YubiKey-5Ci]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - iOS
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: caadbc4a-ebd4-4b1b-96e4-ed68305c63a4
created_at: '2025-12-14T03:47:12.887Z'
updated_at: '2025-12-14T03:47:12.887Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Interact-with-FIDO-Device

## Summary

This procedure completes the fake U2F registration by physically interacting with a FIDO hardware device in Brave iOS, advancing the exploit to the JavaScript injection phase.

## Description

After triggering u2f.register() from the subframe, the user is prompted to authenticate with a FIDO U2F device. Inserting and touching a device like YubiKey 5Ci confirms the process, causing Brave to handle the response and evaluate the injected payload. This step relies on user interaction in the attack scenario, simulating legitimate registration but enabling UXSS. Prerequisites: Active FIDO modal; outcomes: Payload processing without further checks.

## Requirements

1. Compatible FIDO U2F device (e.g., YubiKey 5Ci)
2. iOS device with USB/ Lightning support for the key
3. Triggered U2F modal in Brave

## Defense

Defensive measures and detection strategies:

- Prompt users to verify registration requests match expected sites
- Log FIDO interactions for anomaly detection
- Disable U2F in high-risk environments

## Objectives

1. Authenticate the fake registration to proceed
2. Trigger response handling in browser
3. Enable unescaped payload evaluation

## Instructions

### Step 1: Insert FIDO Device

**Context**: Connect the hardware key to iOS device.

Plug in YubiKey 5Ci via Lightning adapter.

> Ensure device is recognized by iOS.

### Step 2: Confirm Prompt

**Context**: Touch the device when prompted in the modal.

Physically touch the YubiKey sensor.

> Expected: Registration completes; browser processes response.

### Step 3: Validate Interaction

**Context**: Confirm no errors in authentication.

Observe modal dismissal without failure.

> Success: Process advances to JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/YubiKey-5Ci]]

## Tags

- [[fido]]
- [[Hardware]]
- [[u2f]]
