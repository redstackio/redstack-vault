---
id: cmd-ps-auxww
data: ps auxww
tags:
  - process-enumeration
type: command
output: >-
  USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND

  root         1  0.0  0.1  22588  4044 ?        Ss   10:00   0:00 /usr/bin/puma
  ...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.998Z'
verified: false
validated: true
submitted: true
---
# ps-auxww

## Command

```bash
ps auxww
```

## Description

Lists all running processes with full command lines (a=all, u=user, x=no TTY, ww=wide) to enumerate server state post-compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| auxww | Flags for full process list | Yes |

## Examples

### Basic Usage

```bash
ps auxww
```

## Expected Output

Detailed process list including GitLab services like puma workers and nginx.

## Related

- [[procedures/Verify-Payload-Execution-and-Command-Injection]]
