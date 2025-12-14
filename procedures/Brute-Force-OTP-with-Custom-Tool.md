---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - brute-force
  - otp
  - 2fa-bypass
type: procedure
tools:
  - '[[tools/Custom-C-Sharp-Bruteforcer]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/Put-Profile-Edit-OTP]]'
verified: false
platforms:
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:42.913Z'
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-OTP-with-Custom-Tool

## Summary

This procedure uses a custom C# tool to brute-force the 4-digit OTP by sending PUT requests to the profile edit endpoint, exploiting no rate limits to try codes 1000-9999 until a 204 response.

## Description

With the session ID, the tool automates requests to https://p.grabtaxi.com/api/passenger/v2/profiles/edit, varying the profileActivationCode parameter. Incorrect attempts return 400, correct ones 204, allowing profile confirmation without the real code.

## Requirements

1. x-mts-ssid from proxy
2. Custom C# tool compiled on Windows .NET 4.0
3. Network access to Grab API

## Defense

Defensive measures and detection strategies:

- Rate limit API attempts (e.g., 5 per minute)
- Expire OTP after failed tries or time
- Monitor for rapid sequential requests

## Objectives

1. Guess correct OTP via brute-force
2. Submit to bypass 2FA
3. Enable profile change

## Instructions

### Step 1: Input Session to Tool

**Context**: Prepare the bruteforcer.

Launch the C# executable and enter x-mts-ssid.

### Step 2: Execute Brute-Force

**Context**: Send requests for codes 1000-9999.

Run the tool; it uses [[commands/Put-Profile-Edit-OTP]] pattern:

The tool handles the loop, stopping on 204.

**Expected Output**: Correct code identified, profile updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/Put-Profile-Edit-OTP]]

## Tools Used

- [[tools/Custom-C-Sharp-Bruteforcer]]

## Tags

- brute-force
- otp
- 2fa-bypass
