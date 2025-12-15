---
tags:
  - qr-login
  - auth-bypass
  - line-app
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Desktop (Windows/Mac)
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 95d8ec26-d7a2-4959-aa84-a0c9aec118fb
created_at: '2025-12-14T17:24:48.147Z'
updated_at: '2025-12-14T17:24:48.147Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-QR-Login-as-Attacker

## Summary

This procedure initiates the QR code login process for LINE's secondary client on Windows or Mac, setting up the vulnerable 2FA verification stage without completing it, to enable subsequent bypass exploitation.

## Description

In the context of LINE's login flow for desktop apps, QR login authenticates the primary device but relies on server-side 2FA for secondary verification. By starting this as an attacker, the session exposes flaws in ownership checks, allowing crafted URLs to hijack the process. This targets environments where users enable 2FA, leading to unauthorized access if combined with phishing.

## Requirements

1. Attacker LINE account with 2FA enabled
2. LINE desktop app (Windows/Mac) installed
3. Primary mobile device for QR scanning

## Defense

Defensive measures and detection strategies:

- Implement strict ownership checks in 2FA logic (e.g., bind verification to device fingerprints)
- Monitor for anomalous login attempts from secondary clients
- Educate users on phishing risks during login

## Objectives

1. Establish a partial login session vulnerable to bypass
2. Generate necessary session artifacts for URL crafting
3. Position for unauthorized access without alerting the victim

## Instructions

### Step 1: Launch LINE Desktop App

**Context**: Open the app to begin the login process and display the QR code.

No specific command; manually launch the LINE application on Windows or Mac.

> The QR code appears for scanning.

### Step 2: Scan QR with Primary Device

**Context**: Authenticate the initial QR scan to proceed to 2FA, but halt before completion.

Manually scan the QR using the attacker's LINE mobile app.

> Session advances to 2FA prompt; do not enter code or click verify.

### Step 3: Inspect Network for Session Details

**Context**: Capture session tokens or endpoints for later URL crafting (using browser dev tools or proxy if needed).

No command; observe the network tab for requests to LINE's auth servers.

> Identify parameters like device_id or token for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[qr-login]]
- [[auth-bypass]]
