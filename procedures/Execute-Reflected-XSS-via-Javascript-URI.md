---
tags:
  - xss
  - reflected-xss
  - javascript-uri
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
updated_at: '2025-12-13T23:52:33.805Z'
sub_techniques: []
id: a19f84bf-9deb-4d21-b408-1c816639763c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Reflected XSS via Javascript URI

## Summary

This procedure injects a javascript: URI into the 'path' parameter to execute arbitrary JavaScript, such as domain alerts, exploiting the lack of URI scheme sanitization for reflected XSS attacks.

## Description

The vulnerable 'path' parameter directly processes javascript: schemes, leading to immediate script execution in the user's browser. This reflected XSS allows attackers to steal cookies, session data, or perform keylogging via popups or inline scripts. It requires no persistence and triggers on URL visit, making it suitable for phishing links. The attack succeeds due to absent validation, impacting users across browsers.

## Requirements

1. Vulnerable endpoint with 'path' parameter.
2. Basic JavaScript payload knowledge.
3. Browser for testing execution.

## Defense

Defensive measures and detection strategies:

- Reject or strip non-http/https URI schemes in parameters.
- Content Security Policy (CSP) to block inline scripts.
- Input validation to escape or whitelist allowed schemes.

## Objectives

1. Trigger JavaScript execution via URI injection.
2. Demonstrate data exfiltration potential (e.g., alert domain).
3. Validate XSS impact on user sessions.

## Instructions

### Step 1: Prepare Payload

**Context**: Create a simple alert to test execution.

Use javascript:alert(document.domain) as the path value.

> Expected output: Payload string for URL append.

### Step 2: Inject and Execute

**Context**: Visit the modified URL to trigger the script.

Full URL: https://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge?&path=javascript:alert(document.domain).

> Expected output: Alert box showing 'supporthiring.shopify.com'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[reflected-xss]]
- [[javascript-uri]]
