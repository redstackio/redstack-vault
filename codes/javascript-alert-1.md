---
id: a9b5368b-2db0-4d85-9aea-69f37d30609f
name: javascript-alert-1
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:41.758886+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - testing
validated: true
---

# javascript-alert-1

## Code

```javascript
alert(1)
```

## Description

Basic JavaScript payload that triggers an alert with '1' to confirm XSS execution capability in the victim's browser.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Fixed numeric alert; no variables | N/A |

## Usage

Wrap in <script> tags for HTML injection: <script>alert(1)</script>. Test in forms or URLs. If alert appears, vulnerability confirmed; escalate to data exfiltration.

## Detection

- User reports unexpected popups.
- WAF logs for 'alert(' patterns.
- Browser extensions blocking inline scripts.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
