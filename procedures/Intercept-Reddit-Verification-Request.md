---
tags:
  - intercept
  - traffic
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.528Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 3674d399-984e-463c-b801-11351f094490
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Reddit-Verification-Request

## Summary

This procedure captures the HTTP POST request to Reddit's coin verification endpoint after a purchase, extracting key parameters for replay.

## Description

Following a coin purchase, the Reddit Android app sends a POST to https://oauth.reddit.com/api/v2/gold/android/verify_purchase with Google Play details. Interception via a proxy reveals the request, including sensitive tokens. This targets mobile app traffic, requiring HTTPS decryption. Expected outcome: Full request details for exploitation.

## Requirements

1. Proxy tool like Burp Suite configured on device
2. CA certificate installed on Android for HTTPS interception
3. Recent purchase transaction

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning in app to block proxies
- Log anomalous request interception attempts

## Objectives

1. Capture POST request body and headers
2. Extract transaction_id, token, product_id, etc.
3. Validate request format for replay

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for app traffic.

No command; configure [[tools/Burp-Suite]]: Set device proxy to Burp listener (e.g., 127.0.0.1:8080), install Burp CA.

> Ensures all app traffic routes through proxy.

### Step 2: Trigger and Capture Request

**Context**: Perform purchase to generate traffic.

Monitor in Burp: Complete purchase in app, filter for /api/v2/gold/android/verify_purchase.

> Expected: Intercepted POST with Content-Type: application/x-www-form-urlencoded, body like transaction_id=GPA...&token=...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- proxy
