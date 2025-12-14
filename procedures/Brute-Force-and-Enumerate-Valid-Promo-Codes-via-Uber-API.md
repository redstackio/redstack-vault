---
id: proc-uuid-3
tags:
  - brute-force
  - enumeration
  - api-abuse
  - metadata-leak
  - mobile
  - uber
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:42.816Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Brute Force]]'
---
# Brute Force and Enumerate Valid Promo Codes via Uber API

## Summary

This procedure exploits the lack of rate limiting on the Uber promo code redemption endpoint by repeatedly submitting test codes through the iOS app, enabling enumeration of valid promotions and extraction of leaked user metadata from API responses.

## Description

The Uber iOS app's redemption endpoint accepts unlimited submissions without throttling, allowing brute force attacks. Attackers input various codes (e.g., alphanumeric combinations) via the UI, triggering API calls that return detailed responses for valid codes, including the promo value, user's country, inviter's name, and profile picture URL. This leads to information disclosure and potential abuse of promotions. Prerequisites include app access; outcomes are lists of valid codes and associated data.

## Requirements

1. Access to promo code input field from previous procedure
2. List of candidate promo codes (e.g., 1000+ generated strings like 'UBER10', 'WELCOME50')
3. Optional: Network proxy tool (e.g., Charles Proxy) to inspect API responses on iOS

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per minute per account/IP)
- Validate and sanitize API responses to exclude sensitive metadata
- Monitor for high-volume failed redemption attempts and block accounts
- Use CAPTCHA on repeated submissions

## Objectives

1. Identify valid promo codes through trial-and-error
2. Extract leaked user metadata from successful responses
3. Demonstrate impact of absent protections on endpoint

## Instructions

### Step 1: Prepare Test Codes

**Context**: Generate or load a list of potential promo codes for systematic testing.

No specific command; manual preparation:

- Create a text file or mental list of codes (e.g., UBERNEW, DISCOUNT20).
- Ensure variety to cover patterns.

> Expected output: Ready list for input.

### Step 2: Submit Codes Rapidly

**Context**: Enter and submit codes via app UI to trigger API calls.

No specific command; interact via UI:

- Paste or type a code into the input field.
- Tap "Apply" or submit.
- Immediately repeat with next code, ignoring errors for invalids.

> For invalid: Error message like "Invalid code". For valid: Success with metadata in response (inspect via proxy: JSON with country, name, picture).

### Step 3: Log and Analyze Responses

**Context**: Capture and review outputs to identify successes and leaks.

No specific command; manual or tool-assisted:

- Note valid codes and any visible details.
- If using proxy, filter for /promo/redeem endpoint responses.

> Expected output: Valid codes list; e.g., {"valid": true, "country": "US", "inviter": "Alice Smith", "picture": "https://..."}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- brute-force
- enumeration
- api-abuse
