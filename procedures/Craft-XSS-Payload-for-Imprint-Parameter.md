---
tags:
  - xss
  - payload-craft
  - url-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:43.749Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ff27625e-e9ad-45c1-acb5-67e9a55a377f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-XSS-Payload-for-Imprint-Parameter

## Summary

This procedure involves creating a malicious URL for the Drugs.com imprint search page by injecting a reflected XSS payload into the 'imprint' parameter, ensuring the input is long enough to generate search results and bypass empty result conditions that prevent reflection.

## Description

The Drugs.com imprint search at https://www.drugs.com/imprints.php reflects the 'imprint' parameter directly into the HTML without sanitization. By using a sufficiently long string (e.g., repeating characters to mimic a valid imprint search), attackers ensure results are displayed, allowing the payload to be rendered. The payload is an encoded JavaScript snippet that injects an <x> element with attributes (v1 to v7) and an onpointerover event handler to execute code like alerting document content or stealing cookies. This sets up the victim for execution upon interaction. Prerequisites include basic JavaScript knowledge and URL encoding tools.

## Requirements

1. Web browser for testing
2. URL encoder (built-in browser dev tools or online tool)
3. Knowledge of JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement output encoding for user inputs in HTML contexts (e.g., htmlspecialchars in PHP)
- Use Content Security Policy (CSP) to restrict inline scripts and event handlers
- Monitor for unusual search query lengths or patterns in logs

## Objectives

1. Deliver a reflected XSS payload via a phishing link or direct URL
2. Ensure payload reflection by generating valid search results
3. Prepare for JavaScript execution to steal session data or perform actions

## Instructions

### Step 1: Design the Payload

**Context**: Create a JavaScript payload that injects an element with a hover-triggered event, using attributes to store data for execution.

Encode the following example payload (adjust for specifics): <x v1=\"alert(1)\" onpointerover=\"eval(atob(v1+v2+...+v7))\">, split across attributes to evade simple filters, then base64-encode if needed.

### Step 2: Construct the URL

**Context**: Append the encoded payload to the imprint parameter, prefixing with a long string (e.g., 100+ 'a' characters) to ensure results.

Manually build: https://www.drugs.com/imprints.php?imprint=aaaaaaaaaaaaaaaa...[encoded_payload]

### Step 3: Verify Reflection

**Context**: Load the URL and inspect the page to confirm the payload is reflected unsanitized.

Open in browser, view source, search for 'imprint' – payload should appear in a <input> or text element without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-craft]]
