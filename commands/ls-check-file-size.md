---
data: ls -al etc-hosts
tags:
  - file-inspection
type: command
output: 'Shows file details, e.g., size 104857600 bytes'
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.592Z'
id: 581f1bc5-de4d-4d9f-a6b8-196eb5894f2e
verified: false
validated: true
submitted: true
---
# ls-check-file-size

## Command

```bash
ls -al etc-hosts
```

## Description

Lists file details in long format to verify size growth after writes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Include all files | No |
| -l | Long format with sizes | Yes |

## Examples

### Basic Usage

```bash
ls -al etc-hosts
```

### Advanced Usage

```bash
ls -alh etc-hosts
```

## Expected Output

File permissions, owner, size in bytes, timestamp.

## Related

- [[procedures/Verify-Host-File-Size-Growth]]
