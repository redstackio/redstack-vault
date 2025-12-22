---
id: b1fb77e4-438a-4ef7-87a3-02adbb362ec5
name: cat-view-etc-passwd
type: command
executor: bash
data: cat /etc/passwd
output: null
created_at: '2023-04-06T03:56:44.361527+00:00'
updated_at: '2023-04-10T20:24:38.743796+00:00'
platforms:
  - Linux
tags:
  - file-read
  - discovery
verified: true
validated: true
---

# cat-view-etc-passwd

## Command

```bash
cat /etc/passwd
```

## Description

This command displays the contents of the /etc/passwd file, which contains user account information including usernames, user IDs (UIDs), group IDs (GIDs), home directories, and default shells. It is commonly used in post-exploitation or reconnaissance to enumerate local users on a Linux system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/passwd` | Path to the passwd file (standard location on Linux) | Yes |

## Examples

### Basic Usage

```bash
cat /etc/passwd
```

### Redirect to File

```bash
cat /etc/passwd > users.txt
```

## Expected Output

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...

Each line represents a user entry in the format: username:password:UID:GID:GECOS:home:shell.

## Related

- [[procedures/Blind-XXE-Out-of-Band-Data-Exfiltration]]
