---
id: proc-uuid-3
tags:
  - ui-vulnerability
  - highlighting-failure
type: procedure
tools:
  - '[[tools/Google-Chrome-Mobile]]'
  - '[[tools/Microsoft-Edge-Mobile]]'
  - '[[tools/Firefox-Mobile]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:45.172Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Domain-Highlighting-Failure

## Summary

This procedure examines the External Link Warning page to confirm the absence of domain highlighting on mobile Chrome and Edge, validating the vulnerability that aids phishing.

## Description

The root cause is a rendering bug in the domain highlighting logic, likely due to CSS/JavaScript differences in mobile viewports. On affected browsers, the true domain (e.g., IP 73.150.2.210 or evil.com) is not visually distinguished from the trusted disguise (e.g., google.com). For comparison, Firefox mobile renders correctly. This step confirms the impact in an authenticated session after triggering a malicious link.

## Requirements

1. Triggered External Link Warning from previous step
2. Mobile device with Chrome or Edge
3. Optional: Firefox for comparison

## Defense

Defensive measures and detection strategies:

- Test UI features across all browsers and devices during development
- Use fallback highlighting methods (e.g., explicit text warnings)
- Monitor user feedback on link warnings

## Objectives

1. Verify lack of visual domain distinction
2. Assess phishing risk from misleading UI
3. Compare with working browsers

## Instructions

### Step 1: Inspect Warning Page

**Context**: Analyze the interstitial for highlighting issues.

Observe the URL display; no bolding, coloring, or separation for the malicious part.

> Expected output: True domain blends with trusted part, e.g., no highlight on @73.150.2.210.

### Step 2: Compare with Firefox

**Context**: Test on Firefox to confirm browser-specific failure.

Repeat link click in Firefox mobile.

> Expected output: Proper highlighting of malicious domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome-Mobile]]
- [[tools/Microsoft-Edge-Mobile]]
- [[tools/Firefox-Mobile]]

## Tags

- ui-vulnerability
- highlighting-failure
