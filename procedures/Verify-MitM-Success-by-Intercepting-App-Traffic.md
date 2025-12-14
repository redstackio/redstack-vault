---
id: proc-uuid-003
tags:
  - mitm
  - traffic-verification
  - decryption
  - ios
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:39.439Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Verify-MitM-Success-by-Intercepting-App-Traffic

## Summary

This procedure confirms the MitM attack by observing decrypted traffic from the Shopify iOS POS app in the proxy tool, proving the app trusts the malicious certificate and exposing sensitive data like CHD.

## Description

Once proxied, the app's traffic to Shopify endpoints (e.g., payment processing) should decrypt fully in the proxy, showing no pinning enforcement. The attacker can inspect requests for CHD, API keys, or session tokens. Success is indicated by cleartext visibility without errors, highlighting the vulnerability's impact on secure communications.

## Requirements

1. Malicious certificate trusted and proxy configured
2. Shopify POS app installed and active
3. Proxy tool running with CA for re-signing responses

## Defense

Defensive measures and detection strategies:

- Audit app traffic for pinning implementation and enforce it
- Detect proxy usage via app telemetry or device logs
- Use endpoint protection to flag decrypted sensitive data in transit

## Objectives

1. Validate lack of pinning by successful decryption
2. Identify interceptable sensitive data
3. Demonstrate full MitM control over app communications

## Instructions

### Step 1: Monitor Proxy Logs

**Context**: Watch for app-initiated connections.

In Burp Proxy, navigate to Proxy > HTTP history.

**Expected Output**: Entries showing Shopify domains (e.g., api.shopify.com) from iOS IP.

In mitmproxy:

```bash
mitmproxy -s script.py  # Or default console
```

> Expected output: Flow list with HTTPS requests.

### Step 2: Interact with App

**Context**: Trigger sensitive traffic.

In POS app, simulate a transaction (e.g., add item, process card scan).

**Expected Output**: Decrypted POST requests with CHD payloads visible.

### Step 3: Confirm Decryption

**Context**: Ensure no errors and full visibility.

Check for unencrypted body containing JSON with card data; verify certificate in proxy is the malicious one.

**Expected Output**: Cleartext CHD (e.g., card number in request body).

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]
- [[tools/mitmproxy]]

## Tags

- mitm
- verification
- decryption
