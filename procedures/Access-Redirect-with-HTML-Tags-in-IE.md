---
id: proc-ie-html-redirect
tags:
  - xss
  - html-injection
  - ie-bypass
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ie-html-injection-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.803Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Redirect-with-HTML-Tags-in-IE

## Summary

This procedure uses Internet Explorer 11 or lower to access the PHP redirect script with a target URL containing unencoded HTML tags, exploiting the lack of path sanitization in the Twitter 404 page for initial injection testing.

## Description

Modern browsers encode special characters in URLs, but a 302 redirect from PHP sends the raw string. In IE, this allows tags like <h1>TEST</h1> to reach the server unencoded. Target: https://sms-be-vip.twitter.com/. Expected: HTML renders in 404 response.

## Requirements

1. Hosted PHP redirect script
2. Internet Explorer 11 or lower
3. Public access to target domain

## Defense

Defensive measures and detection strategies:

- URL path sanitization/encoding on server
- WAF rules for HTML in paths
- Log and block suspicious redirects

## Objectives

1. Deliver unencoded HTML to 404 page
2. Confirm injection without padding
3. Prepare for XSS escalation

## Instructions

### Step 1: Construct the Redirect URL

**Context**: Build the parameter with injected HTML in the target path.

**Command** ([[commands/ie-html-injection-url]]):
```url
http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>
```

> Enter this in IE's address bar. The PHP script redirects to the Twitter URL with raw tags. Expected output: 404 page shows 'TEST' as a heading.

### Step 2: Observe Injection

**Context**: Inspect the resulting page for rendered HTML.

**Command** (View source in IE):
```html
<!-- Check for <h1>TEST</h1> in response -->
```

> Right-click and view page source. Expected output: Tags present and parsed as HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/ie-html-injection-url]]

## Tools Used

- [[tools/Internet-Explorer-11]]

## Tags

- xss
- html-injection
- ie-bypass
