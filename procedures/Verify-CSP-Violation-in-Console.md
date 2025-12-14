---
tags:
  - csp-verification
  - console-log
  - error-analysis
type: procedure
tools:
  - '[[tools/Browser-Developer-Console]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Software Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ecd6bf56-5275-4923-980e-63c1968aec79
created_at: '2025-12-13T23:56:03.566Z'
updated_at: '2025-12-13T23:56:03.566Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Software Discovery]]'
---
# Verify-CSP-Violation-in-Console

## Summary

This procedure uses the browser console to inspect and confirm the CSP block on the XSS attempt in Stripe dashboard.

## Description

Post-trigger, the developer console reveals detailed CSP errors, such as refusals for 'unsafe-inline' scripts or javascript: schemes. This validates the vulnerability's existence despite mitigation, aiding in reporting or bypass research. It involves opening dev tools after the click, focusing on console tab for security policy violations. Requires browser dev tools and prior trigger step.

## Requirements

1. Triggered the malicious link
2. Modern browser with developer tools (Chrome, Firefox, etc.)
3. Basic knowledge of reading console errors

## Defense

Defensive measures and detection strategies:

- Monitor CSP violation reports server-side
- Integrate console logging with SIEM for anomaly detection
- Regularly audit browser console during security testing

## Objectives

1. Capture evidence of CSP blocking the payload
2. Analyze error details for potential weaknesses
3. Document the protection mechanism

## Instructions

### Step 1: Open Developer Console

**Context**: Access the browser's debugging interface.

No command required; right-click page and select 'Inspect' or press F12, then switch to Console tab.

> Console opens, ready to display errors from the trigger.

### Step 2: Review CSP Error

**Context**: Examine logs for the refusal message.

No command required; look for red error entries mentioning CSP and 'refused to execute inline script' or similar.

> Error details confirm the block, e.g., 'Content-Security-Policy: The page’s settings blocked the loading of a resource...'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Software Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Console]]

## Tags

- [[csp-verification]]
- [[console-log]]
- [[error-analysis]]
