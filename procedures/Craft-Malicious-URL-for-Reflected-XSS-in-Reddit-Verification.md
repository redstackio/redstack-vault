---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - url-injection
  - payload-crafting
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
updated_at: '2025-12-14T17:26:28.047Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-URL-for-Reflected-XSS-in-Reddit-Verification

## Summary

This procedure involves constructing a malicious URL targeting Reddit's /verification/ endpoint by injecting a JavaScript payload into the path parameter, exploiting the lack of sanitization to enable reflected XSS on the email verification interstitial page.

## Description

In the context of Reddit's email verification flow, the server reflects the token from the URL path directly into the HTML of the verification page without proper escaping or validation. An attacker crafts a URL where the path after /verification/ includes a payload like 'asd', alert(document.location), ' which, when URL-encoded, injects and executes JavaScript upon page load or interaction. This allows arbitrary code execution in the victim's browser, leading to impacts such as session theft or page modification. Prerequisites include understanding URL encoding and basic JavaScript for payloads.

## Requirements

1. Access to a URL encoder/decoder tool or manual knowledge of encoding (e.g., %20 for spaces)
2. Knowledge of the target endpoint (/verification/ on reddit.com)
3. Web browser for testing (optional, for attacker verification)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user-controlled inputs reflected in pages
- Validate URL path parameters against expected formats (e.g., alphanumeric tokens only)
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous URLs in logs with injected scripts

## Objectives

1. Create a functional malicious link that mimics a legitimate verification URL
2. Ensure payload survives URL parsing and reflection
3. Enable subsequent JavaScript execution for exploitation

## Instructions

### Step 1: Identify Base Endpoint

**Context**: Start with the legitimate Reddit email verification URL structure: https://www.reddit.com/verification/{token}.

No command required; note the path format.

> This establishes the injection point in the token parameter.

### Step 2: Design and Encode Payload

**Context**: Craft a simple JavaScript payload to test reflection, such as alert(document.location) to pop up the current URL, confirming execution.

Manually construct: Insert payload into path as /verification/asd', alert(document.location), '.

URL-encode: https://www.reddit.com/verification/asd%27%2C%20alert(document.location)%2C%20%27

> Encoding ensures the payload is transmitted correctly; test in browser dev tools if needed.

### Step 3: Validate Payload

**Context**: Optionally test the URL in a controlled environment to confirm reflection without execution.

Open the URL in a browser and inspect the page source for the reflected token.

> Expected: Unsanitized string appears in HTML, ready for execution on interaction.

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
- [[url-injection]]
- [[payload-crafting]]
