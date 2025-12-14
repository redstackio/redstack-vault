---
id: proc-digits-examine-parsing-1
tags:
  - recon
  - javascript
  - parameter-parsing
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
updated_at: '2025-12-14T17:31:52.810Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Examine Client-Side Parameter Parsing in Digits popup.js

## Summary

This procedure involves inspecting the JavaScript code in Digits' popup.js to identify how query parameters are parsed, revealing a vulnerability where the client splits only on '&' while the server handles both '&' and ';', enabling bypass attacks.

## Description

In the Digits web authentication flow, the client-side code at https://cdn.digits.com/45ed91c4cf9b6bb7465c27574b16910df8a86d2e_1458327827406/javascripts/popup.js uses split('&') to parse query strings and unescapes values, assuming ampersand as the sole delimiter. This creates an inconsistency with the server, which accepts semicolons as well, allowing attackers to inject malicious content into parameters like 'host' without server detection. The procedure targets web browsers and requires access to the public JavaScript file. Expected outcome is confirmation of the parsing logic for crafting exploits.

## Requirements

1. Web browser with developer tools (e.g., Chrome)
2. Internet access to load the Digits CDN URL
3. Basic JavaScript knowledge for code inspection

## Defense

Defensive measures and detection strategies:

- Implement consistent parameter parsing across client and server (e.g., standardize on '&' only)
- Use URL validation libraries that handle multiple delimiters uniformly
- Monitor for anomalous redirects in authentication logs

## Objectives

1. Identify delimiter handling in client code
2. Confirm vulnerability for parameter injection
3. Document parsing behavior for exploit development

## Instructions

### Step 1: Load and Inspect popup.js

**Context**: Access the JavaScript file to locate the query parsing function.

Navigate to https://cdn.digits.com/45ed91c4cf9b6bb7465c27574b16910df8a86d2e_1458327827406/javascripts/popup.js in your browser or download it.

Search for 'split' functions related to query strings, focusing on URLSearchParams or manual splitting logic.

> Look for code like: var params = location.search.substring(1).split('&'); This confirms only '&' is used, ignoring ';'. Expected output: Code snippet showing split('&').

### Step 2: Test Parsing Behavior

**Context**: Simulate parsing to verify the mismatch.

In browser console, test: var test = 'host=https://example.com;@attacker.com'.split('&'); console.log(test);

> This treats the entire string as one parameter if no '&', allowing ';@attacker.com' to be appended undetected by client validation. Expected output: Array with full malicious host value.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[JavaScript]]
- [[parameter-parsing]]
