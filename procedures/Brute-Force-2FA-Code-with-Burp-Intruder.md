---
tags:
  - brute-force
  - burp-intruder
  - 2fa-bypass
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
updated_at: '2025-12-14T17:24:47.527Z'
sub_techniques:
  - '[[Password Spraying]]'
id: 12deea32-9547-45da-b74d-fb346b1d1566
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-2FA-Code-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder to automate brute-force attempts on the static 6-digit 2FA code, exploiting permissive rate limiting that allows ~1000 tries before success.

## Description

The 2FA code remains static during the session despite failed attempts. After initial 429 Too Many Requests responses, the endpoint resumes with 400 Invalid Code replies without regenerating the code or enforcing blocks. Configure Intruder with numeric payloads from 000000 to 999999, filtering for 200 OK responses indicating a hit.

## Requirements

1. Intercepted 2FA verification POST request
2. Burp Suite Professional or Community edition
3. Knowledge of the target's actual 2FA code (via email access in real attack)

## Defense

Defensive measures and detection strategies:

- Implement exponential backoff and code regeneration after failures
- Block IPs after X attempts, regardless of response type
- Monitor for high-volume requests to auth endpoints

## Objectives

1. Guess the 6-digit code to bypass 2FA
2. Achieve full account login and vault access
3. Demonstrate impact of weak rate limiting

## Instructions

### Step 1: Send to Intruder

**Context**: Prepare the captured request for automated attacks.

In Burp Proxy, right-click the request and select 'Send to Intruder'.

> Intruder tab opens with the request loaded.

### Step 2: Configure Positions

**Context**: Mark the 2FA code parameter for payload replacement.

In Positions tab, highlight the 6-digit code field (e.g., §code§) and click 'Add §'.

> Clear other positions if any; ensure only code is attacked.

### Step 3: Set Payloads

**Context**: Define numeric range for brute-forcing.

In Payloads tab, set type to 'Numbers', from 000000 to 999999, step 1, padded to 6 digits.

> Options: No encoding needed.

### Step 4: Launch Attack

**Context**: Execute and monitor for valid response.

Click 'Start Attack'; ignore initial 429s, continue until 200 response.

> Sort by status code; valid code yields 200 and login success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Spraying]] Password Spraying (adapted for 2FA codes)

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[burp-intruder]]
- [[2fa-bypass]]
