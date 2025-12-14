---
tags:
  - login-intercept
  - 2fa
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:47.531Z'
sub_techniques: []
id: 883a72c5-c6a5-426d-a16a-f3ccd2634b13
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Initiate-Login-and-Intercept-2FA-Request

## Summary

This procedure starts the Bitwarden login process with a random 2FA code to trigger and capture the verification request for subsequent brute-forcing.

## Description

After entering valid email and password, the login flow prompts for the 2FA code. Submitting an invalid code sends a POST request to the verification endpoint (e.g., /identity/accounts/verify-2fa), which returns 400 for invalid or 200 for valid. Intercepting this with a proxy like Burp Suite allows modification for attacks.

## Requirements

1. Burp Suite configured as browser proxy
2. Valid Bitwarden email/password
3. Access to recent 2FA code via email (but use random for interception)

## Defense

Defensive measures and detection strategies:

- Proxy detection via TLS fingerprinting
- Rate limit pre-2FA login attempts

## Objectives

1. Reach 2FA verification stage
2. Capture the exact POST request structure
3. Identify the code parameter for payload insertion

## Instructions

### Step 1: Start Login Flow

**Context**: Enter credentials to trigger 2FA.

In browser, go to https://vault.bitwarden.com, enter email/password, and proceed.

> Receive 2FA code email but ignore; enter random 6-digit code.

### Step 2: Intercept Request

**Context**: Capture the verification POST in Burp.

With Burp proxy active, submit the form; intercept the request in Proxy tab.

> Observe 400 response; forward to Intruder for next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[login-intercept]]
- [[2fa]]
