---
tags:
  - cookie-theft
  - exfiltration
  - android
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1416]]'
updated_at: '2025-12-14T03:46:31.923Z'
sub_techniques: []
id: aba41cd0-6d81-48b4-a9ca-bf0ea82cce4c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1416]]'
---
# Exfiltrate-User-Cookies-via-WebView

## Summary

This procedure captures the exposed cookies from the XSS execution, enabling theft of JWT tokens for account takeover and unauthorized financial actions.

## Description

The WebView's document.cookie reveals tokens from my.exness.asia and other sites due to shared storage, allowing replay for viewing positions, modifying portfolios, and initiating withdrawals.

## Requirements

1. XSS payload executed successfully
2. User logged in with active session
3. Mechanism to capture WebView output (e.g., via accessibility or screenshot)

## Defense

Defensive measures and detection strategies:

- Isolate WebView cookies per domain/app
- Monitor for anomalous WebView loads
- Implement token binding to device

## Objectives

1. Collect sensitive session data
2. Compromise user account
3. Perform high-impact actions like withdrawals

## Instructions

### Step 1: Observe WebView Output

**Context**: The payload writes cookies to the visible WebView.

View the SMFeedbackActivity screen for displayed cookie string.

> Expected output: String like "jwt_token=abc123; session_id=xyz".

### Step 2: Capture and Use Cookies

**Context**: Exfiltrate via network (modify payload to fetch) or manual copy for replay.

Use stolen JWT in requests to https://my.exness.asia API.

> Expected output: Successful API calls as authenticated user.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1416]] Cross-site Scripting (XSS)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cookie-theft
- exfiltration
- android
