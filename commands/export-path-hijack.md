---
id: cmd-uuid-006
data: 'export PATH=/tmp:$PATH'
tags:
  - hijacking
  - path
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.849Z'
verified: false
validated: true
submitted: true
---
# export-path-hijack

## Command

```bash
export PATH=/tmp:$PATH
```

## Description

Prepends /tmp to the PATH environment variable to hijack command resolution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `PATH=/tmp:$PATH` | New PATH value | Yes |

## Examples

### Basic Usage

```bash
export PATH=/tmp:$PATH
```

### Advanced Usage

```bash
export PATH=/custom/dir:$PATH
```

## Expected Output

No output; verify with echo $PATH.

## Related

- [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]
