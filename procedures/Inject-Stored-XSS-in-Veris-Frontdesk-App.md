---
tags:
  - xss
  - stored-xss
  - android-app
  - injection
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bdc112cf-5218-431e-8c68-6ae8be510f10
created_at: '2025-12-14T03:15:26.753Z'
updated_at: '2025-12-14T03:15:26.753Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-Veris-Frontdesk-App

## Summary

This procedure demonstrates injecting JavaScript payloads into the Veris Frontdesk Android App's visitor check-in fields, exploiting lack of input sanitization to store malicious code that later executes in the web portal.

## Description

The Veris Frontdesk App allows visitor check-ins with fields like 'Who do you wish to meet?' and 'Additional Information' that accept user input without validation or escaping. Payloads such as `<img src=x onerror=alert(3)>` are stored in the backend and later reflected in the web portal's visitor log at https://sandbox.veris.in/portal/visitor-log/, leading to stored XSS. This affects any authenticated user viewing the log, potentially allowing session theft or phishing. Prerequisites include an Android device with the app installed and network connectivity to the backend.

## Requirements

1. Android device or emulator running the Veris Frontdesk App
2. Network access to the app's backend servers
3. No special app permissions beyond standard check-in access

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and HTML escaping for all user inputs using libraries like OWASP Java Encoder
- Use Content Security Policy (CSP) on the web portal to block inline JavaScript execution
- Monitor for anomalous JavaScript alerts or DOM manipulations in portal logs
- Validate and sanitize mobile app inputs before backend storage

## Objectives

1. Persist malicious JavaScript in the visitor database via app inputs
2. Ensure payloads bypass any client-side checks in the app
3. Set up for execution against web portal users

## Instructions

### Step 1: Launch and Navigate to Check-In

**Context**: Open the app and access the vulnerable check-in form to prepare for payload entry.

No specific command; manually launch the app and select Check In.

> The app interface should display the check-in options. Proceed if the form loads.

### Step 2: Fill Mandatory Fields

**Context**: Provide legitimate data to reach the vulnerable fields without triggering validation errors.

Enter test values: First Name "Test", Last Name "User", Phone "1234567890".

> Form advances to next screen upon tapping Next.

### Step 3: Inject Payloads

**Context**: Enter XSS payloads in the unsanitized fields to store executable code.

In 'Who do you wish to meet?': `<img src=x onerror=alert(3)>`

In 'Additional Information': `<img src=x onerror=alert(4)>`

> Payloads are accepted; tap Submit to store them server-side.

### Step 4: Submit Check-In

**Context**: Finalize the process to persist the payloads in the database.

Complete submission.

> Confirmation appears; the entry is now stored and ready for reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[stored-xss]]
- [[android-app]]
