---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - auth-bypass
  - account-takeover
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.283Z'
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
# Account-Takeover-via-Email-Validation-Bypass

## Summary

This procedure exploits a regex logic error in email validation during registration to takeover an existing customer account by appending special characters to the email, allowing QR code-based login as the original user.

## Description

The target application prevents registration with existing emails but fails to properly validate modified variants due to trimming in QR code generation. By intercepting the registration request and appending '<' to an existing email like jobert@mydocz.cosmic, a QR code is generated that authenticates as the original account. This grants full access to the customer's session without credentials. Prerequisites include access to the public registration endpoint and knowledge of an existing email from source code inspection.

## Requirements

1. Public access to https://h1-415.h1ctf.com/register
2. Existing customer email (e.g., from source code)
3. [[tools/Burp-Suite]] for request interception
4. QR code scanner capability in browser

## Defense

Defensive measures and detection strategies:

- Implement strict email canonicalization and validation before QR generation
- Use server-side checks to prevent variant registrations
- Monitor for anomalous QR scans or registration patterns
- Rate-limit registration attempts

## Objectives

1. Gain unauthorized access to an existing customer account
2. Establish persistence via QR login
3. Enable further escalation in support portal

## Instructions

### Step 1: Identify Target Email

**Context**: Locate an existing email to target for takeover.

Inspect source code for leaked emails like jobert@mydocz.cosmic. Verify registration is blocked for the exact email.

### Step 2: Intercept and Modify Registration

**Context**: Bypass validation by modifying the email parameter.

Configure [[tools/Burp-Suite]] to intercept POST to /register. Change email to 'jobert@mydocz.cosmic <'.

```http
POST /register HTTP/1.1
Host: h1-415.h1ctf.com

email=jobert%40mydocz.cosmic%20%3C
```

> The server trims < in QR generation, creating a code for the original email. Expected output: 200 OK with QR data.

### Step 3: Execute Takeover

**Context**: Use the QR to login as the target.

Save QR, logout, go to /recover, and scan.

> Successful login grants customer access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- auth-bypass
- account-takeover
