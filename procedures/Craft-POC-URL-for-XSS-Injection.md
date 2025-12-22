---
tags:
  - xss
  - poc
  - url-crafting
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
  - '[[tools/Microsoft-Edge]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 958c2dfd-f238-4d14-ab1c-8aade5c8d1d9
created_at: '2025-12-13T23:56:20.496Z'
updated_at: '2025-12-13T23:56:20.496Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft POC URL for XSS Injection

## Summary

This procedure crafts a proof-of-concept URL to exploit a DOM-based XSS vulnerability by injecting a script tag via an unsanitized URL parameter.

## Description

The procedure creates a specially crafted URL that appends malicious HTML to the vulnerable parameter, allowing script injection into the DOM. It targets web pages using Lever services and Masonry JS, with outcomes including successful HTML injection on non-encoding browsers.

## Requirements
1. Knowledge of the vulnerable URL parameter (lever-)
2. Access to the target page
3. Browser for testing

## Defense

Defensive measures and detection strategies:
- Sanitize all URL parameters before DOM insertion
- Implement strict CSP to block external scripts
- Log and alert on suspicious URL patterns

## Objectives
1. Inject arbitrary HTML/script via URL
2. Demonstrate vulnerability exploitability
3. Prepare for browser verification

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL with the injection payload.

> Use: https://www.hackerone.com/careers?lever-#aaa"><script src="https://app-sj17.marketo.com/index.php/form/getForm?callback=alert"></script>

### Step 2: Test Initial Injection

**Context**: Load the URL to check for basic injection.

> Inspect the page source for the injected script tag.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[JavaScript]]

### Sub-Techniques

## Commands Used

## Tools Used
- [[tools/Internet-Explorer]]
- [[tools/Microsoft-Edge]]

## Tags
- xss
- poc
