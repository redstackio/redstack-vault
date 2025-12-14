---
tags:
  - xss
  - stored-xss
  - android
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Android
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 965c9f4c-c41b-414f-834b-f71c55846236
created_at: '2025-12-14T17:24:39.224Z'
updated_at: '2025-12-14T17:24:39.224Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payloads-via-Veris-Frontdesk-App

## Summary

This procedure exploits insufficient input validation in the Veris Frontdesk Android App's check-in form by injecting JavaScript payloads into fields like 'Who do you wish to meet?' and 'Additional Information', which are stored unsanitized and later reflected in the web portal.

## Description

The Veris Frontdesk App allows visitor check-ins without sanitizing user inputs, enabling attackers to store malicious JavaScript. Payloads such as `<img src=x onerror=alert(3)>` are entered during the check-in process and persisted to the backend. When these entries appear in the web portal's visitor log, they execute in the viewer's browser, allowing theft of session data or further exploitation. This targets environments using the Veris system for visitor management, requiring only app access.

## Requirements

1. Installed Veris Frontdesk Android App on a device or emulator
2. Network connectivity to the app's backend
3. No authentication required for check-in

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and output encoding (e.g., HTML entity escaping) for all user inputs
- Use Content Security Policy (CSP) headers in the web portal to restrict inline JavaScript execution
- Monitor for anomalous JavaScript alerts or DOM manipulations in browser logs

## Objectives

1. Persist malicious JavaScript in the backend via app inputs
2. Ensure payloads evade any client-side validation
3. Set up for execution in the web portal context

## Instructions

### Step 1: Launch and Navigate to Check-In

**Context**: Open the app and access the vulnerable form to begin the injection process.

Launch the Veris Frontdesk Android App and select the 'Check In' section from the main menu.

### Step 2: Enter Legitimate Details

**Context**: Provide basic information to reach the vulnerable fields without triggering errors.

Fill in required fields: first name (e.g., 'Test'), last name (e.g., 'User'), and phone number (e.g., '1234567890'). Tap 'Next' or 'Proceed' to advance.

### Step 3: Inject XSS Payloads

**Context**: Enter malicious payloads in the target input fields to store executable JavaScript.

In the 'Who do you wish to meet?' field, enter: `<img src=x onerror=alert(3)>`

In the 'Additional Information' field, enter: `<img src=x onerror=alert(4)>`

### Step 4: Submit and Complete Check-In

**Context**: Finalize the process to store the payloads server-side.

Tap 'Submit' or 'Complete Check-In' to process the form. Confirm the check-in succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- android
