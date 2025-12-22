---
id: cmd-uuid-5
data: grep asan /proc/<Squid PID>/maps
tags:
  - verify
  - process
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.203Z'
verified: false
validated: true
submitted: true
---
# check-asan-with-proc-maps

## Command

```bash
grep asan /proc/<Squid PID>/maps
```

## Description

Searches the memory maps of a running Squid process for ASAN-related libraries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <Squid PID> | Process ID of Squid | Yes |

## Examples

### Basic Usage

```bash
grep asan /proc/1234/maps
```

### Advanced Usage

```bash
grep -i asan /proc/$(pgrep squid)/maps
```

## Expected Output

Lines containing 'asan' if dynamically loaded.

## Related

- [[Related Procedure: Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]
