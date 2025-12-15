---
id: cmd-uuid-4
data: ls -la hacked
tags:
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.115Z'
verified: false
validated: true
submitted: true
---
# ls-verify-hacked

## Command

```bash
ls -la hacked
```

## Description

Lists detailed information about the 'hacked' file to verify its creation as a result of the injected touch command in the bunyan exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-la` | Long format with all attributes | Yes |
| `hacked` | Target file name | Yes |

## Examples

### Basic Usage

```bash
ls -la hacked
```

### Advanced Usage

```bash
ls -la | grep hacked
```

## Expected Output

Output like "-rw-r--r-- 1 user user 0 Oct 1 12:00 hacked", confirming the empty file's existence and timestamp.

## Related

- [[Related Procedure|procedures/Verify-Bunyan-Exploitation]]
