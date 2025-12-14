---
tags:
  - xss
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 974d0ffa-0130-4562-8794-3efd8a1784ac
created_at: '2025-12-14T03:16:30.800Z'
updated_at: '2025-12-14T03:16:30.800Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate Reflected XSS via Endpoint Parameter

## Summary

This procedure demonstrates a reflected Cross-Site Scripting (XSS) vulnerability in the 'endpoint' parameter of the Informatica Cloud Chat application by injecting a JavaScript payload that executes upon form submission, allowing arbitrary code execution in the victim's browser.

## Description

The vulnerability arises from insufficient input sanitization of the 'endpoint' parameter in https://parc.informatica.com/partners/apex/Cloud_chat. By appending a 'javascript:' scheme payload, such as javascript:alert(document.domain), to the URL, the payload is reflected into the page. Submitting the form triggers execution, potentially leading to session hijacking, cookie theft, or keylogging in the context of the trusted domain. This affects users who click a crafted link, making it suitable for social engineering attacks.

## Requirements

1. Web browser with JavaScript enabled
2. Access to the internet and the target URL
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, rejecting 'javascript:' schemes
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution in browser logs or WAF alerts

## Objectives

1. Confirm reflection and execution of JavaScript payload
2. Highlight risks of session hijacking or data exfiltration
3. Validate lack of output encoding in form handling

## Instructions

### Step 1: Inject XSS Payload into Endpoint

**Context**: Navigate to the target URL with the payload to reflect it in the page.

No specific command; use browser address bar:

Navigate to: https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=javascript:alert(document.domain)

> This loads the page with the payload reflected, visible in the form or page source.

### Step 2: Submit Form to Trigger Execution

**Context**: Interact with the form to execute the reflected script.

No specific command; manually submit the form on the page.

> Upon submission, an alert pops up showing the document domain, confirming XSS.

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
- [[reflected-xss]]
