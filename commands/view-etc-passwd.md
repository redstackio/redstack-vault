---
type: command
executor: bash
data: cat /etc/passwd
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - discovery
verified: true
validated: true
---

# view-etc-passwd

## Command

```bash
cat /etc/passwd
```

## Description

Displays the contents of /etc/passwd to enumerate users and verify modifications during privesc.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cat | Display file contents | Yes |
| /etc/passwd | Path to user database | Yes |

## Examples

### Basic Usage

```bash
cat /etc/passwd
```

### Advanced Usage (grep for new user)

```bash
grep 'hacker' /etc/passwd
```

## Expected Output

```
root:x:0:0:root:/root:/bin/bash
...
hacker:$1$hacker$...:0:0:Hacker:/root:/bin/bash
```
List of colon-separated user entries.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/check-etc-passwd-permissions]]
