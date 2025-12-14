---
data: 'php -S 0.0.0.0:80'
tags:
  - hosting
  - server
  - php
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: ba07afb9-faf5-4425-915a-e735574cf43e
created_at: '2025-12-14T04:08:55.327Z'
updated_at: '2025-12-14T04:08:55.327Z'
verified: false
validated: true
submitted: true
---
# php-built-in-server-host

## Command

```bash
php -S 0.0.0.0:80
```

## Description

Starts the built-in PHP development server to host files and scripts, binding to all network interfaces on port 80. Used in SSRF attacks to serve redirection scripts and PoC files for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-S` | Start server mode | Yes |
| `0.0.0.0` | Bind address (all interfaces) | Yes |
| `80` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
php -S 0.0.0.0:80
```

### Advanced Usage

```bash
php -S 0.0.0.0:8080 -t /path/to/files
```

## Expected Output

PHP 7.x.x Development Server (http://0.0.0.0:80) started

## Related

- [[Related Procedure]]
