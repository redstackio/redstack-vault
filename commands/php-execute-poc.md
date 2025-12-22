---
id: cmd-php-execute-poc-001
data: php poc.php
tags:
  - php
  - poc
  - exploit
type: command
output: string(XXX) "HTTP/1.1 200 OK\r\n..." (partial response before crash)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:09.943Z'
verified: false
validated: true
submitted: true
---
# php-execute-poc

## Command

```bash
php poc.php
```

## Description

Executes a PHP PoC script (poc.php) that uses fsockopen to send a crafted multipart POST request to the vulnerable server, triggering the null pointer dereference and crashing the PHP process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `php` | PHP interpreter | Yes |
| `poc.php` | Path to the PoC script file | Yes |

## Examples

### Basic Usage

```bash
php poc.php
```

### Advanced Usage

```bash
php -d display_errors=1 poc.php
```

## Expected Output

Dumps the server response (possibly partial or error), and the server process crashes remotely due to segmentation fault, visible in logs as null pointer dereference.

## Related

- [[Related Procedure|procedures/Trigger-PHP-Crash-with-PoC]]
