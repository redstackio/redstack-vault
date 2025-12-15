---
tags:
  - ios
  - pin-bypass
  - auth-bypass
  - objective-c
  - runtime-manipulation
type: procedure
tools:
  - '[[tools/SnoopIt]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:28:20.211Z'
sub_techniques: []
id: ec0f2aee-df91-4bee-9e9c-b2f2e8b4d72f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Bypass-iOS-App-PIN-via-Runtime-Method-Invocation

## Summary

This procedure demonstrates bypassing PIN authentication in the Coinbase iOS app by using SnoopIt to invoke the internal userAuthenticated method in CBPINViewController, simulating successful login without entering the PIN. It targets apps vulnerable to runtime manipulation due to missing validation on method calls.

## Description

The attack requires the app to be running with a PIN prompt active. SnoopIt attaches to the process, exposes Objective-C classes, and allows direct method invocation. The root cause is the app's failure to validate authentication state or protect against debuggers, allowing arbitrary calls to internal APIs. This grants unauthorized access to sensitive features like account balances or transactions. Note: Requires jailbreak, making it out-of-scope for some bounties, but highlights design flaws.

## Requirements

1. Jailbroken iOS device with SnoopIt installed and configured
2. Coinbase app with PIN set and running
3. Access to SnoopIt web interface (local browser)
4. Basic knowledge of Objective-C class structure

## Defense

Defensive measures and detection strategies:

- Enforce jailbreak detection and disable app on rooted devices
- Add runtime integrity checks to detect debugger attachment (e.g., sysctl queries)
- Validate method calls with state checks before proceeding
- Obfuscate class and method names to hinder exploration
- Use certificate pinning and code signing to prevent tampering

## Objectives

1. Trigger and intercept the PIN authentication flow
2. Identify and invoke the bypass method to skip validation
3. Gain access to protected app areas without credentials

## Instructions

### Step 1: Set PIN and Launch App

**Context**: Prepare the authentication challenge.

Open Coinbase app settings to set a PIN, then relaunch to trigger the prompt.

> App UI interaction. Expected output: PIN screen blocks access.

### Step 2: Access SnoopIt Interface

**Context**: Connect to the tool for manipulation.

Browse to SnoopIt's local web panel (typically http://localhost:port).

> Browser access. Expected output: Dashboard shows attached process.

### Step 3: Explore Objective-C Classes

**Context**: Locate the authentication controller.

Navigate to the 'Objective-C Classes' section and search for coinbase.CBPINViewController.

> UI navigation in SnoopIt. Expected output: Class details visible, including methods.

### Step 4: Invoke userAuthenticated Method

**Context**: Directly call the method to fake authentication success.

Select the userAuthenticated method and invoke it without parameters.

> Tool button or script execution in interface. Expected output: PIN screen vanishes; app proceeds to dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SnoopIt]]

## Tags

- ios
- pin-bypass
- auth-bypass
