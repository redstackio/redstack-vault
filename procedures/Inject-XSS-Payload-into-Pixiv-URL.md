---
id: proc-pixiv-url-xss-001
tags:
  - xss
  - reflected-xss
  - url-injection
type: procedure
tools:
  - '[[tools/Chrome-iOS-13-1]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.886Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Pixiv-URL

## Summary

This procedure exploits a reflected XSS vulnerability in pixiv.net's mobile URL parameters by injecting JavaScript payloads, allowing arbitrary code execution on page load to confirm the issue or steal data like cookies.

## Description

The attack targets the mobile web version of pixiv.net accessed via Chrome on iOS 13.1, where user input in URL paths is not properly sanitized or encoded. By appending payloads like confirm(3) or alert(document.cookie) to the /en/ path, the JavaScript executes immediately upon loading, potentially leading to session hijacking through cookie theft. This is effective in a drive-by scenario where victims click malicious links.

## Requirements

1. iOS 13.1 device with Chrome browser configured for mobile user agent.
2. Access to pixiv.net without authentication.
3. Basic knowledge of JavaScript payloads for testing.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for URL parameters using libraries like DOMPurify.
- Deploy Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous JavaScript alerts or network requests from user agents indicating mobile iOS access.

## Objectives

1. Verify XSS vulnerability in URL handling.
2. Demonstrate potential for data exfiltration like cookies.
3. Enable session hijacking by capturing authentication tokens.

## Instructions

### Step 1: Craft and Access Basic Payload URL

**Context**: Test for XSS by injecting a simple confirm dialog to verify execution without data theft.

Using [[tools/Chrome-iOS-13-1]], navigate to:

```url
https://www.pixiv.net/en/['-confirm(3)-']
```

> This payload breaks out of any string context and executes confirm(3), popping a dialog if vulnerable.

### Step 2: Inject Cookie-Stealing Payload

**Context**: Escalate to capture session cookies for hijacking.

Using [[tools/Chrome-iOS-13-1]], navigate to:

```url
https://www.pixiv.net/en/['-alert(document.cookie)-']
```

> The alert displays cookies; in a real attack, replace with exfiltration to an attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-iOS-13-1]]

## Tags

- [[xss]]
- [[reflected-xss]]
