---
id: c76332c9-2a47-45b0-9a34-f9efdee38c96
name: HTML-Img-OnError-DocumentWrite-Iframe
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:38.129859+00:00'
updated_at: '2023-04-10T20:23:57.596521+00:00'
platforms:
  - Web
tags:
  - html-injection
  - iframe
  - ssrf-payload
validated: true
---

# HTML-Img-OnError-DocumentWrite-Iframe

## Code

```html
<img src="echopwn" onerror="document.write('<iframe src=file:///etc/passwd></iframe>')"/>
```

## Description

This HTML code snippet creates an invalid image element with src="echopwn" to intentionally trigger the onerror event. Upon error, it uses document.write to inject an iframe element into the page, loading content from the specified src attribute. Originally shown for local file access, it can be adapted for SSRF by changing the iframe src to an internal or remote URL (e.g., http://localhost/internal or cloud metadata endpoints), forcing resource loads when the HTML is processed in a vulnerable context.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| src in iframe | URL to load in the iframe; modify for target endpoint (e.g., internal service or metadata) | http://169.254.169.254/latest/meta-data/ |

## Usage

Embed this snippet in a file (e.g., payload.html) and inject via upload or input field in a web app that renders HTML without sanitization. Trigger by loading the page containing the injected content. For SSRF, ensure the application fetches or proxies the iframe src server-side; otherwise, it results in client-side loading. Useful in HTML injection vulns leading to resource fetching.

## Detection

- Scan rendered HTML for suspicious img tags with onerror handlers or dynamic document.write calls.
- Monitor for unexpected iframe insertions or requests to internal/localhost from web processes.
- Enable CSP to block unsafe-inline and frame-src; log JavaScript errors and DOM mutations.
- WAF rules to detect patterns like onerror="document.write('<iframe' in user input.

## Related

- [[procedures/SSRF-via-Injected-HTML-File-as-Image-or-Text]]
- [[commands/curl-inject-html-payload]]
