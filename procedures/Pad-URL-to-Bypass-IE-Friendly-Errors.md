---
id: proc-ie-url-padding
tags:
  - xss
  - ie-bypass
  - padding
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ie-padded-html-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.800Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Pad-URL-to-Bypass-IE-Friendly-Errors

## Summary

This procedure adds excessive padding (dots) to the URL path in the redirect to exceed IE's threshold for displaying custom error pages, forcing the raw vulnerable 404 response to show injected HTML.

## Description

IE shows its own 'friendly' error for short 404 responses (<512 bytes); padding the path makes the response longer, displaying the server's output with unsanitized path reflection. Used after basic injection to visualize effects.

## Requirements

1. Working PHP redirect with HTML injection
2. IE 11 or lower
3. Long string for padding (e.g., 300+ dots)

## Defense

Defensive measures and detection strategies:

- Limit path length or sanitize long inputs
- Disable friendly errors or use strict content-length checks
- Detect padded or anomalous paths in logs

## Objectives

1. Force raw server response in IE
2. Visualize HTML injection clearly
3. Enable POC validation

## Instructions

### Step 1: Append Padding to URL

**Context**: Extend the path beyond 512 bytes to trigger raw display.

**Command** ([[commands/ie-padded-html-url]]):
```url
http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
```

> Paste into IE. The dots pad the path. Expected output: Full 404 page with 'TEST' heading visible.

### Step 2: Verify Raw Response

**Context**: Confirm no IE overlay interferes.

**Command** (Inspect in IE):
```html
<!-- Look for unfiltered path echo -->
```

> View source or rendered page. Expected output: Injected HTML parsed and displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/ie-padded-html-url]]

## Tools Used

- [[tools/Internet-Explorer-11]]

## Tags

- xss
- ie-bypass
- padding
