---
type: command
executor: bash
data: tar -T $_LIST_FILE -xf $_ARCHIVE_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - injection
  - file-list
  - tar
verified: true
validated: true
---

# tar-files-from-injection

## Command

```bash
tar -T $_LIST_FILE -xf $_ARCHIVE_FILE
```

## Description

Extracts files specified in a list file, injectable by appending commands to the list for execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -T | Read file list from file | Yes |
| $_LIST_FILE | Path to list (e.g., list.txt with 'file; id') | Yes |
| -x | Extract | Yes |
| -f | Archive | Yes |
| $_ARCHIVE_FILE | TAR file path | Yes |

## Examples

### Basic Usage

```bash
tar -T files.txt -xf archive.tar
```

### Advanced Usage

```bash
tar -T 'injected_list.txt' -xf archive.tar
```

## Expected Output

Extracts listed files; injected commands run, potentially writing output files.

## Related

- [[procedures/TAR-Argument-Injection]]
