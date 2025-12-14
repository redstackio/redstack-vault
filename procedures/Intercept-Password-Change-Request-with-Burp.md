---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - intercept
  - proxy
  - brute-force
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:31:42.743Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Intercept Password Change Request with Burp

## Summary

Capture the password change POST request using Burp Suite proxy to inspect and modify fields for brute-forcing.

## Description

With Burp proxy active, submit a password change to intercept the request containing old_password and new_password. This allows sending to Intruder for automation. The lack of rate limiting enables high-volume attacks.

## Requirements

1. Burp Suite running as proxy (e.g., 127.0.0.1:8080)
2. Browser traffic routed through proxy
3. Hijacked session active

## Defense

Defensive measures and detection strategies:

- Rate limit password verification attempts per session/IP
- Use CAPTCHA or secondary auth for changes
- Monitor proxy-like traffic patterns

## Objectives

1. Capture vulnerable request
2. Identify fields for brute-force
3. Enable automated attacks

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept HTTPS traffic.

In Burp > Proxy > Options, ensure Intercept is on. Configure browser to use proxy.

> Expected output: Traffic visible in Proxy history.

### Step 2: Submit and Intercept

**Context**: Trigger the request to capture it.

Enter random old/new passwords and submit; drop the request in Burp for inspection.

> Expected output: POST with form-data: old_password=..., new_password=....

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Password Guessing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
