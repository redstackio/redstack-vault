---
type: command
executor: bash
data: export LD_PRELOAD=/tmp/shell.so
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - environment
  - ld_preload
verified: true
validated: true
---

# export-ld_preload-path

## Command

```bash
export LD_PRELOAD=/tmp/shell.so
```

## Description

Sets the LD_PRELOAD environment variable to specify a shared library path, which will be preloaded before others when executing programs. Use this to inject custom code into processes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `LD_PRELOAD` | Environment variable for preload path | Yes |
| `=/tmp/shell.so` | Path to the .so file (placeholder; substitute actual path) | Yes |

## Examples

### Basic Usage

```bash
export LD_PRELOAD=/tmp/shell.so
```

### Unset After Use

```bash
unset LD_PRELOAD
```

## Expected Output

Silent on success. Verify with 'echo $LD_PRELOAD' showing the path.

## Related

- [[procedures/linux-privilege-escalation-via-ld_preload-and-nopasswd]]
