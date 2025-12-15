---
data: cat /etc/passwd
tags:
  - file-disclosure
  - recon
type: command
executor: bash
platforms:
  - Linux
id: d42d0dd2-71cc-4b22-8751-180d874a8599
created_at: '2025-12-14T17:28:20.227Z'
updated_at: '2025-12-14T17:28:20.227Z'
verified: false
validated: true
submitted: true
---
# cat-etc-passwd

## Command

```bash
cat /etc/passwd
```

## Description

This Unix command reads and displays the contents of the /etc/passwd file, which lists user accounts and can be used in RCE scenarios to enumerate users on the target system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/passwd` | Path to the password file | Yes |

## Examples

### Basic Usage

```bash
cat /etc/passwd
```

### Advanced Usage

Pipe to grep for specific users:

```bash
cat /etc/passwd | grep root
```

## Expected Output

List of users and their home directories, e.g., root:x:0:0:root:/root:/bin/bash

## Related

- [[commands/php-injection-shell-exec-cat-passwd]]
- [[procedures/Crafting-Injection-Payloads-for-Rank-Creation-Exploitation]]
