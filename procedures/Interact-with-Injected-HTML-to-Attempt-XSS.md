---
id: proc-uuid-1010132-3
tags:
  - xss-execution
  - csp-violation
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.570Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Interact-with-Injected-HTML-to-Attempt-XSS

## Summary

This procedure involves interacting with the reflected HTML in search results to attempt JavaScript execution, highlighting the XSS potential blocked only by CSP in Hey.com.

## Description

After reflection, clicking the injected link triggers a javascript:alert(1) handler, but CSP blocks it. This tests execution in the web browser context during an authenticated session. Outcomes confirm HTML injection success and CSP as the sole mitigator, with risks of account takeover if bypassed.

## Requirements

1. Reflected malicious email visible in search results
2. Browser console open for monitoring
3. Understanding of CSP policies

## Defense

Defensive measures and detection strategies:

- Strengthen CSP with 'unsafe-inline' restrictions and nonce usage
- Block javascript: URLs in link parsing
- Detect and alert on CSP violation events in client-side logs

## Objectives

1. Trigger interaction with injected element to execute script
2. Observe CSP blocking and policy details
3. Assess impact if CSP were absent or bypassed

## Instructions

### Step 1: Locate Injected Element

**Context**: Identify the rendered malicious link in results.

In the search results, find the 'ClickHere' link from the injected <a> tag.

### Step 2: Interact with the Link

**Context**: Attempt to execute the JavaScript payload.

Click on the 'ClickHere' link.

### Step 3: Monitor Console for Violations

**Context**: Verify blocking and inspect policy.

Open browser developer tools console; expect CSP error showing policy: script-src 'self' https://production.haystack-assets.com stats.hey.com *.braintreegateway.com *.braintree-api.com hcaptcha.com *.hcaptcha.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[csp-violation]]
- [[JavaScript]]
