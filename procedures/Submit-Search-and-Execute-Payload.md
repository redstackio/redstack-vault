---
tags:
  - xss-execution
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2025-12-14T03:15:30.631Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.631Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 27c9cd9a-78d4-4051-8a13-7926e82bc74b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Submit Search and Execute Payload

## Summary

This procedure covers submitting the search query to trigger the reflection and execution of the injected XSS payload, confirming arbitrary JavaScript execution.

## Description

Upon submission, the Kartpay platform reflects the search input directly into the HTML response without escaping, causing the browser to parse and execute the malicious JavaScript. The payload '"><img src=x onerror=alert(domain)>' leverages an onerror event to run alert(domain), proving execution in the site's context. This enables attackers to steal session cookies, hijack accounts, or perform other client-side attacks. The procedure assumes the payload is already injected and focuses on triggering the vulnerability, with outcomes including visible code execution and potential data exfiltration.

## Requirements

1. Payload already entered in the search field
2. Functional search submission mechanism on the page
3. Victim's browser session (attacker's or targeted)

## Defense

Defensive measures and detection strategies:

- Use output encoding (e.g., HTML entity encoding) for all reflected inputs
- Implement client-side and server-side validation to strip dangerous characters
- Deploy runtime application self-protection (RASP) to detect and block XSS attempts

## Objectives

1. Trigger the reflection of unsanitized input
2. Achieve JavaScript execution in the browser
3. Demonstrate impact such as session theft or phishing

## Instructions

### Step 1: Trigger the Search Submission

**Context**: Submit the form to send the payload to the server and receive the reflected response.

Click the search button or press Enter to submit the query.

> The server processes the input and returns a response where the payload is echoed back into the page.

### Step 2: Observe Execution

**Context**: Monitor the browser for signs of JavaScript execution.

Watch for the alert dialog box appearing with the domain name.

> Successful execution shows the alert, confirming the XSS vulnerability and the ability to run arbitrary code.

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
- [[javascript-execution]]
