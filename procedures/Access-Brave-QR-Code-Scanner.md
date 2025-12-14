---
id: proc-brave-scanner-access-001
tags:
  - qr-code
  - brave-browser
type: procedure
tools:
  - '[[tools/Brave-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:34.866Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Access-Brave-QR-Code-Scanner

## Summary

This procedure covers navigating to the QR code scanning feature in Brave Browser, enabling the exploitation of its automatic redirect behavior.

## Description

Within Brave's interface, the QR scanner is accessed via menu options, activating the device's camera. This feature lacks URL previews, making it vulnerable. Applicable to Android and iOS; no commands needed. Successful access leads directly to scanning capability, heightening phishing risks.

## Requirements

1. Brave Browser launched and active
2. Camera permissions enabled for the app
3. Stable device orientation for scanning

## Defense

Defensive measures and detection strategies:

- Disable or restrict QR scanning in browser settings if available
- Implement app-level policies to block auto-navigations from scans
- Log camera and scanner activations for behavioral analysis

## Objectives

1. Activate the vulnerable scanning interface
2. Prepare for QR code input
3. Exploit the absence of safeguards

## Instructions

### Step 1: Navigate to Scanner Option

**Context**: Locate the QR feature in the UI.

Tap the menu (three dots) or address bar icon and select 'Scan a QR code'.

> Expected: Camera viewfinder opens.

### Step 2: Grant Permissions if Prompted

**Context**: Allow camera access.

Approve any permission requests.

> No command; system dialog.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Brave-Browser]]

## Tags

- qr-code
- brave-browser
