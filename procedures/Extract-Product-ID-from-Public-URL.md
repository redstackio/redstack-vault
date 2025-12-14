---
id: proc-uuid-1
name: Extract-Product-ID-from-Public-URL
tags:
  - reconnaissance
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.671Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Extract-Product-ID-from-Public-URL

## Summary

This procedure involves accessing a public product page on the target e-commerce site to extract the Base64-encoded public key from the URL, serving as the starting point for crafting malicious requests in a CSRF attack.

## Description

In the context of exploiting weak product ID validation on platforms like DigitalSellz, attackers first need the public product key exposed in URLs. This key is a Base64-encoded integer representing the product ID. By visiting the product page, the attacker obtains this key without authentication, enabling subsequent decoding and manipulation to target private endpoints.

## Requirements

1. Web browser with network inspection capabilities
2. Access to the target's public product URLs
3. No authentication required for this step

## Defense

Defensive measures and detection strategies:

- Monitor for unusual access patterns to product pages from suspicious IPs
- Implement URL obfuscation or short-lived keys to limit exposure

## Objectives

1. Obtain the public Base64-encoded product key
2. Identify the target product for manipulation
3. Prepare for ID decoding

## Instructions

### Step 1: Navigate to Product Page

**Context**: Use a browser to visit the rival's product page and inspect the URL.

No command required; manually enter or follow link to `https://www.digitalsellz.com/p/NDgxNQ`.

> The URL path after `/p/` contains the Base64 key (e.g., `NDgxNQ`). Copy this for decoding.

### Step 2: Inspect and Copy Key

**Context**: Verify the key format in the browser's address bar or developer tools.

No command; use browser dev tools (F12) to confirm network request if needed.

> Expected: Key like `NDgxNQ` ready for padding and decoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web]]
