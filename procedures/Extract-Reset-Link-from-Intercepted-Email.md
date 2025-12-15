---
id: proc-extract-link-001
tags:
  - email-parsing
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:06.223Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract Reset Link from Intercepted Email

## Summary

This procedure parses the captured clear-text email to retrieve the password reset link for use in account takeover.

## Description

Once the email is intercepted, the body contains the reset link in plain text, along with metadata like sender (help@rubygems.org), recipient (victim@gmail.com), and subject (Change your password). No decryption is needed due to missing TLS. This step focuses on identifying and copying the URL, which includes a unique token. Expected outcome: Isolated reset link ready for exploitation.

## Requirements

1. Access to the intercepted email content (e.g., from packet capture)
2. Basic text parsing skills or email viewer
3. Awareness of RubyGems link format (e.g., https://rubygems.org/account/password/reset?token=...)

## Defense

Defensive measures and detection strategies:

- Obfuscate or shorten reset links in emails
- Implement token expiration and one-time use
- Log access to reset links for anomaly detection

## Objectives

1. Locate the reset URL in the email body
2. Verify link validity by format
3. Prepare link for immediate use

## Instructions

### Step 1: Open Intercepted Email

**Context**: View the full email content from the capture.

No command required; load the packet or email file in a viewer.

> Scan for the body section containing the reset instructions.

### Step 2: Copy Reset Link

**Context**: Extract the clickable or text-based URL.

No command required; highlight and copy the link.

> Ensure it includes the token parameter; test in a browser if needed (but avoid premature use to prevent expiration).

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[link-extraction]]
- [[email-analysis]]
