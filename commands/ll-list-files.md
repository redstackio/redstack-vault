---
id: uuid-ll-list
data: ll
tags:
  - verification
type: command
output: >-
  Directory listing showing new files 'here' and 'whoamreallyare' after
  exploitation
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.547Z'
verified: false
validated: true
submitted: true
---
# ll-list-files

## Command

```bash
ll
```

## Description

Lists directory contents in long format (alias for ls -l) to verify files created by exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
ll
```

### Advanced Usage

```bash
ll *.txt
```

## Expected Output

Long listing with permissions, sizes, and timestamps for files like 'here' (executable) and 'whoamreallyare'.

## Related

- [[procedures/Verify-Exploitation-Results]]
- [[commands/cat-whoamreallyare]]
