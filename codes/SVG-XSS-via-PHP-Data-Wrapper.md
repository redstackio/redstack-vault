---
type: code
language: html
verified: true
tags:
  - xss
  - payload
  - data-wrapper
  - lfi
platforms:
  - Web
  - PHP
validated: true
---

# SVG-XSS-via-PHP-Data-Wrapper

## Code

```url
http://example.com/index.php?page=data:application/x-httpd-php;base64,PHN2ZyBvbmxvYWQ9YWxlcnQoMSk+
```

## Description

This code snippet is a URL embedding a base64-encoded SVG element with an onload JavaScript alert using the data:// wrapper and application/x-httpd-php MIME type. In a vulnerable PHP inclusion context, it forces the server to parse the data as PHP, but since it's SVG, it renders as HTML in the browser, executing the JS. This technique bypasses PHP-only filters and tools like Chrome's XSS Auditor by disguising XSS as a PHP payload.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example.com | Target domain with vulnerable inclusion | vulnerable-site.com |

## Usage

Access the URL in a browser targeting a page that includes the parameter. The SVG renders and triggers alert(1) if successful. Customize the onload payload for more advanced XSS (e.g., stealing cookies). Use when direct <script> tags are filtered but file inclusion allows HTML rendering.

## Detection

- Browser developer tools showing unexpected SVG inclusions from PHP endpoints.
- WAF signatures for base64-decoded SVG with onload handlers.
- XSS scanners detecting alert() in responses from data:// requests.
- Audit logs for MIME type mismatches (PHP parsing non-PHP content).

## Related

- [[procedures/Exploit-Data-Wrapper-for-LFI-RFI]]
