---
data: touch HACKED
tags:
  - file-creation
  - rce-proof
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.916Z'
id: 083ac488-6ef1-4787-a694-f6bc3b232fe7
verified: false
validated: true
submitted: true
---
# touch-create-file

## Command

```bash
touch HACKED
```

## Description

Creates an empty file named 'HACKED' in the current directory, used as proof of command injection execution in the arpping exploit.

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
touch /tmp/HACKED
```

## Expected Output

No stdout output; file is created silently if successful.

## Related

- [[commands/ls-check]]
