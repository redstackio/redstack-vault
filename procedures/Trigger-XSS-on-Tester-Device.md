---
tags:
  - xss
  - execution
  - android
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:39.667Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fa168e1c-5c8e-4726-a65c-7f2482d6836a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Tester-Device

## Summary

This procedure describes the victim-side interaction that triggers the XSS payload in the Crashlytics Android app, resulting in JavaScript execution when viewing the beta invitation details.

## Description

Once the invitation is accepted, the Crashlytics app fetches and renders the app name from fabric.io without HTML escaping, typically in a WebView or text view that interprets HTML. The malicious payload executes client-side, allowing actions like displaying alerts, stealing local data, or launching Android intents (e.g., <a href="intent:#Intent;action=my_action;end">Open App</a>). This is a reflected XSS variant tied to the invitation context, affecting invited users' devices.

## Requirements

1. Victim has Crashlytics Android app installed (or prompted to install)
2. Valid beta invitation received
3. Android device (version compatible with Crashlytics)

## Defense

Defensive measures and detection strategies:

- Patch Crashlytics app to sanitize app name rendering
- Enable WebView restrictions (e.g., no JavaScript) in app code
- Monitor app logs for unexpected script execution or intent launches
- User training to avoid untrusted beta apps

## Objectives

1. Cause payload rendering and execution
2. Achieve arbitrary JS in app context
3. Enable follow-on attacks like data exfiltration

## Instructions

### Step 1: Receive and Open Invitation

**Context**: Victim interacts with the email to initiate the process.

The tester clicks the invitation link in the email, which opens or redirects to the Crashlytics app.

### Step 2: View Beta Details in App

**Context**: Navigate to the invitation within the app to trigger rendering.

In the Crashlytics app, go to the 'Invites' or 'Beta' section and select the malicious app invitation. The app name is fetched and displayed, executing the payload (e.g., onerror event on a bogus image src).

> Example payload effect: An alert box appears with "03", confirming execution. Advanced payloads could send device info to an attacker server.

### Step 3: Validate Execution

**Context**: Confirm the attack success from attacker perspective.

If monitoring a C2 or exfil endpoint, check for incoming data. Otherwise, ask the victim if an alert or unexpected behavior occurred.

**Expected Output**: JavaScript runs; visible effects like alerts or intent-launched apps.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- javascript-execution
- webview-exploit
