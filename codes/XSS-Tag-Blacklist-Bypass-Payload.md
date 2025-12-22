---
id: 64170292-0b3b-42a6-9566-e3e4f5c852ea
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.340547+00:00'
updated_at: '2023-04-10T20:21:51.627920+00:00'
tags:
  - xss
  - bypass
  - payload
platforms:
  - Web
validated: true
---

# XSS-Tag-Blacklist-Bypass-Payload

## Code

```javascript
<script x>
<script x>alert('XSS')<script y>
```

## Description

This JavaScript payload uses malformed <script> tags with attributes like 'x' and 'y' to bypass filters that strictly blacklist complete <script> tags. When injected into a vulnerable web page, it executes the alert('XSS') function in the victim's browser, demonstrating successful XSS. It exploits parsers that may interpret unbalanced or extended tags leniently.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'XSS' | Message displayed in the alert box; replace with malicious code like document.cookie for exfiltration | 'XSS' |

## Usage

Inject this payload into user-controlled inputs on vulnerable web applications, such as search parameters or form fields. Test in a reflected XSS scenario by appending to a URL or submitting via POST. Once executed, it can be adapted for stealing session tokens or keylogging by replacing the alert with more sophisticated JavaScript.

## Detection

- Monitor for unusual script tag patterns in input logs using regex for malformed tags like <script\s+[a-z]+>.
- Enable browser CSP to block inline scripts and use client-side XSS auditors.
- WAF rules should detect and block unbalanced HTML tags and JavaScript keywords in inputs.

## Related

- [[procedures/Exotic-Payloads-for-Bypassing-Tag-Blacklist-in-XSS-Attacks]]
