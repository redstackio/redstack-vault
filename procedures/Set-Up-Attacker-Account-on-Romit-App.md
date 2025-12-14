---
id: proc-romit-setup-account-001
name: Set-Up-Attacker-Account-on-Romit-App
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.239Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[External Remote Services]]'
tags:
  - account-creation
  - api-credentials
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
commands: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---

# Set-Up-Attacker-Account-on-Romit-App

## Summary

This procedure creates a new attacker account on the Romit app to obtain essential API credentials (apiKey, apiSecret, Location-ID) needed for generating authorization signatures in subsequent brute-force steps.

## Description

In the Romit app vulnerability scenario, an attacker must first register an account at app.romit.io to access API credentials stored client-side. These credentials enable the generation of signed requests for the login endpoint. The process targets the web platform and requires no prior access, making it a low-barrier initial step. Expected outcome: Attacker gains credentials for PIN brute-forcing without alerting defenses.

## Requirements

1. Internet access to app.romit.io
2. Valid email and phone number for registration (disposable if needed)
3. Browser with dev tools or [[tools/Burp-Suite]] for inspecting credentials post-registration

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on account creation to deter bulk registrations
- Monitor for anomalous API credential usage from new accounts
- Log and rate-limit account creation attempts

## Objectives

1. Obtain apiKey, apiSecret, and Location-ID
2. Establish attacker foothold in the app ecosystem
3. Prepare for signature-based API interactions

## Instructions

### Step 1: Navigate and Register

**Context**: Access the Romit app registration page to create a new account.

No specific command; use browser to visit https://app.romit.io and complete the sign-up form with email and phone.

> Upon submission, the app returns a confirmation and stores credentials in localStorage or session.

### Step 2: Extract Credentials

**Context**: Inspect the app to retrieve API details for signature generation.

Use browser dev tools or [[tools/Burp-Suite]] to capture requests during login/dashboard access.

> Expected output: apiKey (string), apiSecret (string), Location-ID (UUID-like) visible in network requests or storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-creation]]
- [[api-credentials]]
