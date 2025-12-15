---
id: proc-001
tags:
  - credential-derivation
  - pbkdf2
  - hash-computation
type: procedure
tools:
  - '[[tools/calculate-authpw-ts]]'
  - '[[tools/playcode-io-typescript]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/compute-authpw-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:39.087Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Compute-AuthPW-from-Password

## Summary

This procedure computes the authPW hash required for Firefox account operations by applying PBKDF2 to the victim's email and plaintext password, leveraging publicly available client-side code from Mozilla's fxa-auth-client.

## Description

In Mozilla's Firefox Accounts system, the authPW is derived client-side using PBKDF2 with the email and password as inputs. An attacker with a leaked password can recompute this value to authenticate API requests without needing the full session or 2FA. This is possible because the derivation logic is exposed in the open-source fxa-auth-client repository. The procedure targets scenarios where passwords are available from breaches, enabling unauthorized actions like account deletion.

## Requirements

1. Victim's email address and plaintext password (e.g., from a data leak)
2. TypeScript or Node.js environment for script execution
3. Access to the fxa-auth-client source code or equivalent script

## Defense

Defensive measures and detection strategies:

- Implement server-side verification for sensitive operations like account deletion, requiring 2FA even for password-derived auth
- Monitor for unusual API calls to /v1/account/destroy from non-browser user agents
- Rate-limit authPW-based requests per IP and enforce CAPTCHA for high-volume attempts

## Objectives

1. Generate a valid authPW for use in API exploitation
2. Enable subsequent unauthorized account actions
3. Demonstrate credential reuse from leaks

## Instructions

### Step 1: Prepare the Script

**Context**: Obtain or create the TypeScript script based on public fxa-auth-client code to handle PBKDF2 derivation.

**Command** ([[commands/compute-authpw-script]]):
```bash
# In a Node.js or TypeScript environment
npm install crypto
node calculate_authpw.js --email victim@example.com --password leakedpassword
```

> This script uses PBKDF2 with 1000 iterations, SHA256, and a 32-byte salt derived from the email to produce a 32-byte authPW, base64-encoded. Expected output: a string like "v0+...==".

### Step 2: Execute Computation

**Context**: Run the script with victim credentials to obtain the authPW.

**Command** ([[commands/compute-authpw-script]]):
```bash
# Example execution in online playground
// Input: email = 'victim@example.com', password = 'password123'
// Output: authPW = 'computed_hash_here'
```

> Verify the output is a valid base64 string of 44 characters. If errors occur, check email normalization (lowercase).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/compute-authpw-script]]

## Tools Used

- [[tools/calculate-authpw-ts]]
- [[tools/playcode-io-typescript]]

## Tags

- credential-derivation
- pbkdf2
