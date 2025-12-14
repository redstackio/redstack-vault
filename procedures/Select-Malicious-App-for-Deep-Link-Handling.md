---
tags:
  - deep-link-hijack
type: procedure
tools:
  - '[[tools/Shop-PRO-Malicious-App]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Android
  - iOS
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ddc52940-11ac-4771-9948-b0b49743b31c
created_at: '2025-12-14T17:31:31.006Z'
updated_at: '2025-12-14T17:31:31.006Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Select-Malicious-App-for-Deep-Link-Handling

## Summary

This procedure exploits the OS app selection modal to route the OAuth deep link to the malicious app, enabling code interception.

## Description

After authorization, the OS prompts for which app handles the shopapp:// URI. Selecting (or auto-selecting on iOS) the malicious app delivers the auth code directly to the attacker-controlled app.

## Requirements

1. Both apps installed, malicious one registered for scheme
2. User interaction to select app (or iOS first-come-first-served)
3. No prior scheme exclusivity enforced

## Defense

Defensive measures and detection strategies:

- Use secure redirect methods like ASWebAuthenticationSession on iOS
- Prompt users to confirm app handling for custom schemes
- Detect and block duplicate scheme registrations

## Objectives

1. Divert the deep link from official app
2. Launch malicious app with URI payload
3. Avoid user suspicion during selection

## Instructions

### Step 1: Trigger Modal

**Context**: Complete authorization to invoke the deep link.

The OS displays the app chooser after redirect.

**Expected Output**: Modal with 'Shop' and 'Shop PRO' options.

### Step 2: Select Malicious App

**Context**: Choose the attacker's app.

Tap 'Shop PRO' (always) or set as default.

**Expected Output**: Malicious app launches.

### Step 3: Confirm Handling

**Context**: Verify the link is processed.

App should parse without errors.

**Expected Output**: No fallback to official app.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Shop-PRO-Malicious-App]]

## Tags

- [[deep-link-hijack]]
