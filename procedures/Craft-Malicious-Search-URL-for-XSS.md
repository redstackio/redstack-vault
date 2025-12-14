---
tags:
  - xss
  - url-crafting
  - payload-injection
type: procedure
tools:
  - '[[tools/Web-Browser]]'
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
updated_at: '2025-12-14T00:11:16.142Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 412e14fb-3b33-4c77-92ac-a0e7bcc46ae4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Search-URL-for-XSS

## Summary

This procedure involves constructing a malicious URL for the Mail.ru search endpoint by injecting a URL-encoded XSS payload into the 'q' parameter, setting up the foundation for reflected XSS exploitation.

## Description

In the context of testing the go.mail.ru/search vulnerability, user input in the 'q' parameter is reflected without full sanitization. By crafting a URL with an encoded payload like `<script>alert(1)</script>`, attackers can prepare links for phishing. This targets the Yandex-powered search backend, where reflection occurs in HTML and JSON. Prerequisites include basic URL encoding knowledge and access to a text editor or browser dev tools.

## Requirements

1. Internet access to form the URL
2. Knowledge of URL encoding (e.g., via browser or online tools)
3. Target endpoint: https://go.mail.ru/search?fr=mn&q=

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML entity encoding on all reflected parameters
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for unusual query parameters in access logs

## Objectives

1. Create a shareable link that injects unsanitized input
2. Set up for observation of reflection in victim browsers
3. Enable phishing campaigns via email/social sharing

## Instructions

### Step 1: Select and Encode Payload

**Context**: Choose a basic XSS payload and URL-encode it to bypass basic filters.

No command required; manually encode `<script>alert(1)</script>` to `%3Cscript%3Ealert(1)%3C%2Fscript%3E` using browser dev tools or an online encoder.

> Expected output: Encoded string ready for URL insertion.

### Step 2: Construct Full URL

**Context**: Append the encoded payload to the base search URL.

No command; build `https://go.mail.ru/search?fr=mn&q=%3Cscript%3Ealert(1)%3C%2Fscript%3E`.

> Expected output: Complete, clickable URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[url-crafting]]
