---
tags:
  - account-takeover
  - email-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:39:10.024Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6f1d2d90-3d10-4f71-92ec-e459c089bb30
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Account-Takeover-via-QR-Code-Email-Manipulation

## Summary

This procedure exploits insufficient input validation in a QR code recovery feature by manipulating the email field with angle brackets, which are stripped, allowing registration under another user's email to obtain their recovery QR code and achieve account takeover.

## Description

In the target web application, the QR code generator for account recovery strips angle brackets (<>) from the email input without proper validation. By registering with an email like "jobert@mydocz.cosmic <><>", the brackets are removed, resulting in the legitimate user's email. This returns the target's recovery QR code, enabling takeover upon scanning. This targets applications with email-based recovery without duplicate checks or sanitization.

## Requirements

1. Access to the registration endpoint with QR code generation
2. Knowledge of a target user's email (e.g., jobert@mydocz.cosmic)
3. Ability to scan QR codes for recovery

## Defense

Defensive measures and detection strategies:

- Implement strict email validation and duplicate checks before QR generation
- Use hashing or tokenization for recovery codes instead of direct email exposure
- Log and monitor unusual registration patterns with manipulated inputs

## Objectives

1. Obtain recovery QR code for a target account
2. Achieve unauthorized access to the account
3. Enable further exploitation from the compromised account

## Instructions

### Step 1: Prepare Manipulated Email

**Context**: Craft an email that includes the target's email followed by angle brackets to trigger stripping.

No command needed; input during registration form: jobert@mydocz.cosmic <><>

> The application processes this as jobert@mydocz.cosmic, generating the QR for the target.

### Step 2: Register and Retrieve QR

**Context**: Submit the registration to receive the QR code.

Submit the form via browser or API to the registration endpoint.

> Expected output: QR code image or data for the target account.

### Step 3: Scan QR for Takeover

**Context**: Use the QR to recover and access the account.

Scan the QR using the app's recovery feature.

> Successful takeover grants session access to the target account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-takeover
- qr-code
- email-injection
