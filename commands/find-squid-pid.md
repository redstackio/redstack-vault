---
id: cmd-uuid-6
data: pgrep squid | tail -n 1
tags:
  - pid
  - process
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.198Z'
verified: false
validated: true
submitted: true
---
# find-squid-pid

## Command

```bash
pgrep squid | tail -n 1
```

## Description

Finds the PID of the Squid child process (last one in list).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| squid | Process name | Yes |

## Examples

### Basic Usage

```bash
pgrep squid | tail -n 1
```

### Advanced Usage

```bash
pgrep -f squid | tail -n 1
```

## Expected Output

Single PID number.

## Related

- [[Related Procedure: Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]
