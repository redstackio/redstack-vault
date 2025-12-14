---
id: cmd-uuid-3
data: touch HACKED
tags:
  - shell
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.159Z'
verified: false
validated: true
submitted: true
---
# touch-hacked-file

## Command

```bash
touch HACKED
```

## Description

Creates an empty file named 'HACKED' on the filesystem, used here as an injected shell command to prove remote code execution via command injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `HACKED` | Filename to create | Yes |

## Examples

### Basic Usage

```bash
touch HACKED
```

### Advanced Usage

```bash
touch HACKED && echo "Compromised" > HACKED
```

## Expected Output

No stdout output if successful; the file 'HACKED' is created in the current directory (verify with ls).

## Related

- [[Related Procedure: Execute-imagickal-Command-Injection-Exploit]]
