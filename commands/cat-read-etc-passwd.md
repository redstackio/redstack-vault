---
id: cmd-cat-etc-passwd
data: cat /etc/passwd
tags:
  - recon
  - file-read
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.480Z'
verified: false
validated: true
submitted: true
---
# cat-read-etc-passwd

## Command

```bash
cat /etc/passwd
```

## Description

This command reads and displays the contents of the /etc/passwd file, which lists user accounts on Unix-like systems. Use it in RCE scenarios to enumerate users, UIDs, home directories, and shells for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/passwd` | Path to the system user database file | Yes |

## Examples

### Basic Usage

```bash
cat /etc/passwd
```

### Advanced Usage

```bash
grep 'confluence' /etc/passwd
```

## Expected Output

List of user accounts with details: root:x:0:0:root:/root:/bin/bash, daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin, bin:x:2:2:bin:/bin:/usr/sbin/nologin, confluence:x:2002:2002::/var/atlassian/application-data/confluence:/bin/bash.

## Related

- [[procedures/Exploit-OGNL-Injection-in-Confluence-for-RCE]]
- [[commands/curl-post-ognl-payload]]
