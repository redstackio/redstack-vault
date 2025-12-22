---
id: 723984eb-cc66-4f8e-8528-b4f364de5d5d
name: cat-display-etc-passwd
type: command
executor: bash
data: cat /etc/passwd
output: null
created_at: '2023-04-06T03:55:57.024525+00:00'
updated_at: '2023-04-06T03:55:57.030604+00:00'
platforms:
  - Linux
tags:
  - recon
  - file-read
verified: true
validated: true
---

# cat-display-etc-passwd

## Command

```bash
cat /etc/passwd
```

## Description

This command reads and displays the contents of the /etc/passwd file, which contains user account information including usernames, UIDs, GIDs, home directories, and default shells on Unix/Linux systems. Use it during reconnaissance to enumerate users after gaining command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /etc/passwd | Path to the password file (standard location) | Yes |

## Examples

### Basic Usage

```bash
cat /etc/passwd
```

### Advanced Usage

```bash
cat /etc/passwd | grep root
```

Filter for root or admin users.

## Expected Output

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
```

Success is indicated by listing user entries without permission errors. If access denied, the process lacks read privileges on the file.

## Related

- [[procedures/Basic-Command-Injection-Exploitation]]
