---
id: proc-uuid-3
tags:
  - xss
  - stored-xss
  - javascript
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:25.010Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-HTML-JS-for-Stored-XSS

## Summary

This procedure uploads HTML/JavaScript content via the unrestricted file upload to create a stored XSS vulnerability, executing malicious scripts in the browsers of users who access the file.

## Description

Even after partial fixes to the ownCloud upload vulnerability, insufficient content filtering allows HTML/JS uploads that render when accessed. A script like alert(document.cookie) steals cookies from viewers, enabling session hijacking. This stored XSS persists as the file is served directly, affecting authenticated users. The attack targets web platforms without proper output encoding or content sanitization.

## Requirements

1. Access to the upload feature post-initial fix.
2. Web browser for upload and testing.
3. JavaScript payload ready for cookie exfiltration.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all uploaded content before storage or rendering.
- Use Content Security Policy (CSP) to block inline scripts.
- Validate MIME types and strip executable tags from uploads.
- Monitor for XSS payloads in uploads via pattern matching in logs.

## Objectives

1. Upload executable HTML/JS content.
2. Confirm rendering and script execution on access.
3. Enable client-side attacks like cookie theft.

## Instructions

### Step 1: Prepare XSS Payload

**Context**: Craft a JavaScript snippet to test XSS, focusing on cookie access.

Create a file with:

```html
<script type="text/javascript">alert(document.cookie);</script>
```

> This script alerts cookies when executed, demonstrating data theft potential.

### Step 2: Upload and Access for Execution

**Context**: Submit the file and verify XSS by accessing the URL.

Use the content upload form on https://apps.owncloud.com to upload the file (e.g., stored as 171177-1.php5). Then, visit the direct URL to trigger rendering.

> The browser executes the script, popping an alert with cookies, confirming stored XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[JavaScript]]
