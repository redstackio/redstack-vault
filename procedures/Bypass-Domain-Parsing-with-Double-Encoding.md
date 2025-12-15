---
id: proc-bypass-domain-parsing-double-encoding
tags:
  - double-encoding
  - bypass
  - phishing
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.318Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Domain Parsing with Double Encoding

## Summary

This procedure bypasses URL parsing truncation on hackerone.com by double-encoding the dot (.) as %252E, allowing full domain redirects like google.com via %2Fgoogle%252Ecom, enhancing phishing capabilities.

## Description

Building on partial redirects, double encoding (%252E decodes stepwise to .) fools the parser into accepting the full domain. Performed in Chrome on hackerone.com, it requires browser access and confirms high-impact redirects without auth, leading to arbitrary site navigation.

## Requirements

1. Chrome or compatible browser
2. Knowledge of URL encoding
3. Access to target and external sites

## Defense

Defensive measures and detection strategies:

- Decode URLs multiple times before validation
- Block double-encoded characters in paths
- Alert on %25 sequences in redirect requests

## Objectives

1. Achieve full domain redirect via encoding bypass
2. Overcome single-encoding limitations
3. Enable complete arbitrary redirection

## Instructions

### Step 1: Construct Double-Encoded URL

**Context**: Encode the dot twice to evade truncation.

Navigate to: `https://hackerone.com/%2Fgoogle%252Ecom`

> %252E becomes %2E then ., allowing full google.com redirect. Expected output: Browser goes to https://google.com.

### Step 2: Test in Browser

**Context**: Verify in Chrome to ensure compatibility.

Load the URL and inspect redirect.

> Success: Seamless full redirect, bypassing prior flaws.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- double-encoding
- bypass
