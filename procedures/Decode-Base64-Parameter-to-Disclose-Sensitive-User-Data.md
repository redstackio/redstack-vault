---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - sensitive-disclosure
  - base64-decode
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:11.076Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Decode-Base64-Parameter-to-Disclose-Sensitive-User-Data

## Summary

This procedure decodes the 'fbcid' Base64 parameter from the verification URL to extract sensitive details like user ID, verification code, and email, enabling further attacks.

## Description

The parameter is plainly transmitted in the GET URL, Base64-encoded but reversible, exposing data to logs, history, or interception. No encryption protects it, aiding phishing or hijacking.

## Requirements

1. Captured 'fbcid' value from URL
2. Base64 decoding capability (browser console, online tool, or CLI)
3. Knowledge of expected format (user ID|code|email)

## Defense

Defensive measures and detection strategies:

- Encrypt or hash sensitive params; avoid plain Base64
- Use POST instead of GET for verification
- Sanitize logs to exclude full URLs

## Objectives

1. Reveal embedded user data
2. Identify verification artifacts
3. Support targeted follow-on attacks

## Instructions

### Step 1: Extract Parameter

**Context**: Isolate the encoded value from the URL.

Copy 'fbcid=...' from the verification link.

> Example: fbcid=eyJ1aWQiOiIxMjM0NTYiLCJjb2RlIjoiMTIzNCIsImVtYWlsIjoic3VwcG9ydEBleGFtcGxlLmNvbSJ9

### Step 2: Perform Base64 Decode

**Context**: Decode to plaintext sensitive info.

Use a decoder: Paste into base64decode.org or browser console (atob('encoded'))

> Output: {"uid":"123456","code":"1234","email":"support@example.com"} or similar delimited string.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sensitive-disclosure]]
- [[base64-decode]]
