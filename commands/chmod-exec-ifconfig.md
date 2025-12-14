---
id: cmd-uuid-005
data: chmod +x /tmp/ifconfig
tags:
  - preparation
  - executable
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.852Z'
verified: false
validated: true
submitted: true
---
# chmod-exec-ifconfig

## Command

```bash
chmod +x /tmp/ifconfig
```

## Description

Adds execute permissions to the malicious /tmp/ifconfig script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+x` | Add execute permission | Yes |
| `/tmp/ifconfig` | Target file | Yes |

## Examples

### Basic Usage

```bash
chmod +x /tmp/ifconfig
```

### Advanced Usage

```bash
chmod 755 /tmp/ifconfig
```

## Expected Output

No output if successful.

## Related

- [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]
