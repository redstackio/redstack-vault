---
id: cmd-11
data: cd keys
tags:
  - nav
  - setup
type: command
output: Directory changed
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.525Z'
verified: false
validated: true
submitted: true
---
# cd-keys

## Command

```bash
cd keys
```

## Description

Changes working directory to the keys folder for certificate operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `keys` | Target directory | Yes |

## Examples

### Basic Usage

```bash
cd keys
```

### Advanced Usage

```bash
cd /path/to/keys
```

## Expected Output

Shell prompt updates to keys/.

## Related

- [[commands/cfssl-gencert]]
