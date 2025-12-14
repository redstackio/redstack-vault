---
id: proc-test-browser-redirect
tags:
  - open-redirect
  - browser-testing
  - expedia
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-chrome-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:34.953Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Redirect-Across-Browsers

## Summary

This procedure tests the open redirect vulnerability in different browsers, highlighting inconsistencies like lack of encoding in Firefox versus Chrome's bypass via login flows.

## Description

Browser handling affects exploitation: Firefox allows direct redirects without encoding the rurl parameter, while Chrome encodes URLs but can be bypassed in direct login scenarios. Testing involves crafting the malicious URL and observing behavior, confirming the vuln's reliability for phishing across user bases.

## Requirements

1. Firefox and Chrome browsers installed
2. Curl for consistent testing
3. Malicious URL from prior steps

## Defense

Defensive measures and detection strategies:

- Standardize redirect handling across client-side and server-side
- Use Content Security Policy (CSP) to restrict navigation
- Detect cross-browser anomalies in user agent logs

## Objectives

1. Verify redirect in Firefox without encoding
2. Identify and bypass Chrome encoding
3. Ensure cross-browser exploitability

## Instructions

### Step 1: Test in Firefox

**Context**: Load the malicious logout URL in Firefox to check for immediate redirect.

**Command** ([[commands/curl-chrome-bypass]]):
```bash
curl -X GET "https://www.expedia.com/login?rurl=https://qx4lw1nsec.blogspot.com/" -v
```

> Use this for baseline; in browser, expect direct navigation to malicious site.

### Step 2: Test and Bypass in Chrome

**Context**: Attempt direct load in Chrome, then bypass via login interaction.

No command; interact with login page using the URL.

> Expected: Encoding blocks direct redirect, but login flow allows it.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-chrome-bypass]]

## Tools Used


## Tags

- [[open-redirect]]
- [[browser-testing]]
