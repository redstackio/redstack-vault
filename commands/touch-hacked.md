---
data: touch HACKED
tags:
  - shell
  - file-creation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.777Z'
id: 1b788db0-808f-47bc-be6a-96c84d8cd2c1
verified: false
validated: true
submitted: true
---
# touch-hacked

## Command

```bash
touch HACKED
```

## Description

Creates an empty file named 'HACKED' on the filesystem, used as an injected command to demonstrate RCE in the blamer vulnerability.

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
touch HACKED && echo "Proof" > HACKED
```

## Expected Output

No output if successful; 'HACKED' file created in current directory.

## Related

- [[commands/node-execute-poc]]
