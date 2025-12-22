---
id: proc-uuid-2
tags:
  - xss
  - payload-injection
  - reflected-xss
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-13T23:55:20.486Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Search-Input

## Summary

This procedure demonstrates injecting a simple JavaScript payload into the search input of the MTN Investor website to exploit insufficient input sanitization, leading to reflection in the response.

## Description

Reflected XSS occurs when user-supplied input is immediately rendered in the browser without encoding, allowing malicious scripts to execute. In this scenario, the site's PHP search handler at `/mtn-cmd/search-results.php` echoes the `zoom_query` parameter directly. The payload `'-alert(1)-'` bypasses basic filters and triggers execution upon page load. This targets web browsers and requires no advanced setup, but impacts include phishing and data theft in real attacks.

## Requirements

1. Access to the target webpage from previous procedure
2. Browser with developer tools for inspection
3. Knowledge of basic JavaScript payloads from OWASP references

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs using HTML entity encoding (e.g., htmlspecialchars in PHP)
- Validate input length and characters in search queries
- Log and alert on suspicious payloads containing script tags or alerts

## Objectives

1. Deliver a malicious payload via the search parameter
2. Achieve reflection in the HTTP response
3. Set up for JavaScript execution in the browser context

## Instructions

### Step 1: Locate and Input Payload

**Context**: Identify the search field and enter the test payload to simulate an attack.

Manually enter `'-alert(1)-'` into the search input field on the page.

> This payload is designed to evade simple quote filters. Expected output: The form accepts the input without rejection.

### Step 2: Submit Search Query

**Context**: Trigger the server-side processing to reflect the payload.

Click the search button or submit the form, resulting in a URL like `https://mtn-investor.com/mtn-cmd/search-results.php?zoom_sort=0&zoom_query='-alert(1)-'`.

> The server reflects the query in the results page. Inspect the network tab in dev tools to confirm the parameter is passed unsanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss]]
- [[injection]]
- [[web]]
