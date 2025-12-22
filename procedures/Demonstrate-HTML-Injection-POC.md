---
id: proc-html-injection-poc
tags:
  - xss
  - html-injection
  - poc
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/twitter-html-poc-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.798Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-HTML-Injection-POC

## Summary

This procedure runs a proof-of-concept URL that combines redirect and padding to inject and render HTML in the Twitter 404 page, confirming the vulnerability.

## Description

The POC script automates the redirect and injection, targeting the unsanitized path reflection. Run in IE to see effects. Expected: Custom HTML elements appear on the error page.

## Requirements

1. IE 11 or lower
2. Access to POC hosting (e.g., secgeek.net)
3. Prior confirmation of redirect setup

## Defense

Defensive measures and detection strategies:

- HTML entity encoding in error templates
- CSP headers to block inline HTML
- Rate-limit error page requests

## Objectives

1. Prove HTML injection feasibility
2. Validate server reflection
3. Bridge to XSS testing

## Instructions

### Step 1: Load the POC URL

**Context**: Access the pre-configured POC that handles injection.

**Command** ([[commands/twitter-html-poc-url]]):
```url
http://secgeek.net/POC/Twitter-HTML-POC.php
```

> Open in IE. Expected output: 404 page with injected HTML rendered.

### Step 2: Inspect Results

**Context**: Check for successful parsing.

**Command** (View source):
```html
<!-- Verify <tags> in output -->
```

> Expected output: Tags not escaped, HTML active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/twitter-html-poc-url]]

## Tools Used

- [[tools/Internet-Explorer-11]]

## Tags

- xss
- html-injection
- poc
