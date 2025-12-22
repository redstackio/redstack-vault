---
id: proc-verify-xss-network
tags:
  - xss
  - network-inspection
  - impact-verification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Chrome-DevTools]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.641Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-Impact-via-Network-Inspection

## Summary

This procedure inspects network requests triggered by the exploited <base> tag to confirm the potential for XSS, observing failed loads from the attacker-controlled origin that could deliver malicious scripts.

## Description

After URL manipulation, the page attempts to load resources relative to the protocol-relative base, resulting in requests to the external domain (e.g., assessmentbase). Tools like Chrome DevTools reveal these cross-origin fetches, which fail without attacker control but demonstrate the vector for injecting JS payloads, leading to medium-impact arbitrary execution.

## Requirements

1. Manipulated URL already loaded in browser
2. Chrome DevTools or Burp Suite for network monitoring
3. Understanding of browser resource resolution

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected cross-origin resource requests
- Enforce strict CSP to block unsigned scripts
- Audit JS for location-based DOM modifications

## Objectives

1. Capture anomalous network requests
2. Validate exploit success criteria
3. Quantify XSS risk

## Instructions

### Step 1: Open Network Tab

**Context**: Prepare to monitor requests during page load.

In Chrome, press F12 to open DevTools and switch to the Network tab; clear any existing logs.

> Ensure Burp Suite proxy is active to capture full traffic.

### Step 2: Reload and Analyze

**Context**: Trigger the page load to observe impacted requests.

Reload the manipulated URL and filter for JS resources.

> Look for GET requests like https://assessmentbase/etc/designs/informatica-com/assessmentform/js/angular.min.js; a 404 or failure indicates hijack potential for XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Chrome-DevTools]]

## Tags

- [[xss]]
- [[network-inspection]]
- [[impact-verification]]
