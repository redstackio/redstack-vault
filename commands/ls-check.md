---
data: ls -la HACKED
tags:
  - verify
  - file-check
type: command
output: '-rw-r--r-- 1 user user 0 date HACKED'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.911Z'
id: 70bcf6cb-6db6-4162-9048-cca5c5fc461d
verified: false
validated: true
submitted: true
---
# ls-check

## Command

```bash
ls -la HACKED
```

## Description

Lists detailed information about the 'HACKED' file to verify successful command execution from the injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-la` | Long format with all attributes | Yes |
| `HACKED` | Target filename | Yes |

## Examples

### Basic Usage

```bash
ls -la HACKED
```

### Advanced Usage

```bash
ls -la /tmp/HACKED
```

## Expected Output

File permissions, owner, size (0 bytes), and timestamp if file exists; 'No such file' error if failed.

## Related

- [[commands/touch-create-file]]
