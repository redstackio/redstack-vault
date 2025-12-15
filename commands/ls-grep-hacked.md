---
data: ls -la | grep HACKED
tags:
  - file-check
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.495Z'
id: bdd0252a-4633-46ad-ba89-dbe11cb1739b
verified: false
validated: true
submitted: true
---
# ls-grep-hacked

## Command

```bash
ls -la | grep HACKED
```

## Description

Lists all files in the current directory with detailed attributes and filters for any file named 'HACKED', used to verify presence or absence in exploitation workflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-la` | Long listing format with all attributes | Yes |
| `| grep HACKED` | Pipe to grep for 'HACKED' pattern | Yes |

## Examples

### Basic Usage

```bash
ls -la | grep HACKED
```

### Advanced Usage

```bash
ls -la /path/to/dir | grep HACKED
```

## Expected Output

If 'HACKED' exists: `-rw-r--r-- 1 user group 0 Oct 1 12:00 HACKED`
If absent: No output.

## Related

- [[Related Procedure]]
