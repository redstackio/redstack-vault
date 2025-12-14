---
tags:
  - xss
  - protocol-bypass
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.723Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 32052d47-8a0d-4e53-bd14-6c11a5579bff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-isSafeHost-Validation-with-JavaScript-Protocol-Payload

## Summary

This procedure crafts a malicious javascript: URL payload that bypasses the flawed isSafeHost function in a DoD web application's client-side JavaScript, enabling reflected XSS by exploiting incomplete protocol validation.

## Description

The isSafeHost function in the target application's JavaScript validates redirect URLs by extracting the host portion after the first '://' without checking the protocol scheme. An attacker can prepend 'javascript:' to execute client-side code and append '//://████/' commented out with '//' to invalidate the host check without affecting execution. This allows injection into the /sec.html?redirect= parameter, where the raw value is assigned to window.location.href, leading to arbitrary JavaScript execution in the victim's browser context. Potential outcomes include stealing cookies, phishing, or account takeover on the sensitive DoD domain.

## Requirements

1. Access to inspect the target's client-side JavaScript source (via browser dev tools)
2. Knowledge of JavaScript URL schemes and comment syntax
3. A web browser for testing the payload

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for redirect parameters, rejecting non-http/https protocols
- Sanitize inputs by parsing URLs with libraries like URL() API and verifying schemes explicitly
- Use Content Security Policy (CSP) to restrict script execution from inline or data URLs
- Monitor for anomalous redirect patterns in access logs

## Objectives

1. Bypass host validation to inject executable JavaScript
2. Prepare payload for delivery to victims
3. Enable subsequent exploitation like data theft

## Instructions

### Step 1: Analyze the Validation Function

**Context**: Examine the isSafeHost function to confirm it only checks post-'://' without protocol verification.

Open the target's /sec.html in a browser, inspect the JavaScript, and locate isSafeHost. Note how it splits on '://' and validates the host, ignoring the 'javascript:' prefix.

### Step 2: Craft the Payload

**Context**: Build the bypass using protocol prefix and comment to neutralize the invalid host.

Construct the payload as `javascript:alert(document.cookie);//://████/`. Encode if necessary for URL parameters (e.g., using %3A for ':'). The full exploit URL is `https://█████████/sec.html?redirect=javascript:alert(document.cookie);//://████/`. Test in a local environment or dev tools to verify bypass.

### Step 3: Validate Bypass

**Context**: Confirm the payload passes validation but executes JS.

Paste the crafted redirect into a test form or directly access the URL. Observe if isSafeHost returns true and JS executes without errors.

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
- [[protocol-bypass]]
- [[JavaScript]]
