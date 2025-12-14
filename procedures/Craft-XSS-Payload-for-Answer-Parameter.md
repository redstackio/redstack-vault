---
id: proc-uuid-2
tags:
  - xss
  - payload-crafting
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.939Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-for-Answer-Parameter

## Summary

This procedure involves injecting a reflected XSS payload into an unsanitized 'answer' parameter of a POST request, exploiting lack of input escaping to execute JavaScript.

## Description

The attack targets web forms where user input is reflected back without HTML/JS sanitization. By closing HTML tags and injecting a script tag or event handler, arbitrary code runs in the victim's browser. Prerequisites include a vulnerable endpoint identified previously, leading to outcomes like alert execution or data exfiltration.

## Requirements

1. Vulnerable POST endpoint confirmed
2. Burp Suite for request manipulation
3. Knowledge of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user input using HTML entity encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Log and monitor for suspicious payloads in request parameters

## Objectives

1. Break out of input context to inject HTML/JS
2. Verify execution in the response
3. Enable further exploitation like session theft

## Instructions

### Step 1: Select and Encode Payload

**Context**: Choose a simple XSS payload that closes any open attributes and injects an onerror event.

Craft the payload in Burp:

Use 'A"><img src=x onerror=alert(document.domain)>' and encode as 'A%22%3E%3Cimg+src%3Dx+onerror%3Dalert%28document.domain%29%3E'.

> Expected output: Encoded string ready for POST body insertion.

### Step 2: Inject and Test

**Context**: Insert the payload into the 'answer' parameter and send the request.

In Burp Repeater, update the POST body and forward:

POST /redacted with answer=A%22%3E%3Cimg+src%3Dx+onerror%3Dalert%28document.domain%29%3E

> Expected output: Response renders the payload, triggering an alert with the domain name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[xss]]
- [[web]]
- [[payload]]
