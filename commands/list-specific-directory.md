---
data: 'ls [redacted dir]'
tags:
  - discovery
  - filesystem
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.433Z'
id: 5e92c5ba-2487-4dc1-a60e-c798746fbbca
verified: false
validated: true
submitted: true
---
# List Specific Directory

## Command

```bash
ls [redacted dir]
```

## Description

Lists contents of a specific directory to verify application files on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [redacted dir] | Path to Semrush-specific directory | Yes |

## Examples

### Basic Usage

```bash
ls /path/to/redacted
```

## Expected Output

Files like [redacted].php, [redacted].js, confirming Semrush application files.

## Related

- [[Related Procedure]]
