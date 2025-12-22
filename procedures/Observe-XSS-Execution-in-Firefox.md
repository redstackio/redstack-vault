---
tags:
  - xss
  - execution
  - csp-bypass
  - firefox
  - html-injection
type: procedure
tools:
  - '[[tools/Firefox-69]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:24.172Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 742836e8-ba8d-4d33-97d1-a4fb25931eb6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
---

# Observe-XSS-Execution-in-Firefox

## Summary

This procedure loads the vulnerable page in Firefox version 69 or below to execute the injected JavaScript via CSP bypass, or observes HTML injection in any browser for phishing potential.

## Description

In Firefox <70, the CSP does not block javascript: URLs in <object> data attributes, allowing alert(document.cookie) to fire and steal session data. In newer browsers, CSP prevents JS but permits HTML rendering, e.g., fake <input> elements for phishing. Inspect dev tools to confirm impact.

## Requirements

1. Firefox 69 installed for JS execution demo
2. Loaded vulnerable URL from previous step
3. Dev tools enabled for inspection

## Defense

Defensive measures and detection strategies:

- Update browsers to patch CSP bypasses (Firefox 70+)
- Implement client-side CSP with strict policies
- Detect cookie access anomalies or unexpected alerts

## Objectives

1. Execute JS to exfiltrate cookies in vulnerable browsers
2. Demonstrate HTML injection for phishing
3. Validate attack success

## Instructions

### Step 1: Load in Vulnerable Browser

**Context**: Use Firefox 69 to trigger full XSS.

Open the URL in Firefox 69.

> Expect an alert box displaying document.cookie contents.

### Step 2: Inspect in Modern Browser

**Context**: Test HTML injection resilience.

Load in Chrome/Firefox 70+ and inspect element.

> Verify <object> renders but JS is blocked; test with payload like <input type='text' placeholder='Enter your password'> for fake forms.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-69]]

## Tags

- [[xss]]
- [[Execution]]
- [[csp-bypass]]
- [[firefox]]
- [[html-injection]]

