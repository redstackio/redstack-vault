---
id: uuid-cat-whoami
data: cat whoamreallyare
tags:
  - verification
  - rce
type: command
output: Username 'bl4de'
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.545Z'
verified: false
validated: true
submitted: true
---
# cat-whoamreallyare

## Command

```bash
cat whoamreallyare
```

## Description

Displays the contents of the file created by redirected 'whoami' output from the injection payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `whoamreallyare` | File name containing whoami result | Yes |

## Examples

### Basic Usage

```bash
cat whoamreallyare
```

### Advanced Usage

```bash
cat whoamreallyare | grep user
```

## Expected Output

Single line with username, e.g., 'bl4de'.

## Related

- [[procedures/Verify-Exploitation-Results]]
- [[commands/ll-list-files]]
