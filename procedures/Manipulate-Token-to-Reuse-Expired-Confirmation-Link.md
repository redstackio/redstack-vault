---
tags:
  - auth-bypass
  - token-manipulation
  - account-takeover
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: de5f80f2-ba32-4831-8676-c9f5aec3b9be
created_at: '2025-12-14T17:33:24.369Z'
updated_at: '2025-12-14T17:33:24.369Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Manipulate Token to Reuse Expired Confirmation Link

## Summary

This procedure alters specific characters in an expired confirmation token to bypass validation checks, enabling reuse and unauthorized account access.

## Description

Tokens in Sorare use predictable patterns with isolated numbers (e.g., after underscores) that, when incremented, generate valid variants due to flawed hashing or validation. Editing the URL in the browser circumvents client-side protections, leading to successful confirmation and profile access. This exploits the lack of reuse prevention and edit resistance.

## Requirements

1. An expired confirmation URL with visible token
2. Browser allowing address bar edits (e.g., Chrome)
3. Understanding of token structure from observation

## Defense

Defensive measures and detection strategies:

- Validate token integrity with cryptographic signatures
- Bind tokens to IP/user-agent to detect edits
- Server-side checks for sequential patterns in tokens

## Objectives

1. Bypass single-use enforcement
2. Achieve unauthorized confirmation
3. Gain full account control

## Instructions

### Step 1: Identify Manipulation Point

**Context**: Locate the editable numeric segment in the token.

Examine the URL token, e.g., 'Jt7S7WS_4EphEyiDn6z_', noting the '4' after the underscore.

> Expected output: Identified digit for change (isolated numbers post-underscore).

### Step 2: Edit and Reload Token

**Context**: Increment the digit to create a valid variant.

In the browser address bar, change to 'Jt7S7WS_6EphEyiDn6z_' (4 to 6), then press Enter to reload.

> Expected output: No error; successful redirect to account dashboard, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[auth-bypass]]
- [[token-leak]]
