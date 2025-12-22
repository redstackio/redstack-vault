---
id: ceb6fb83-bec4-44b2-9f53-cb101b7928bc
name: touch-create-empty-file
type: command
executor: bash
data: touch $_FILE_NAME
output: null
created_at: '2023-04-06T03:56:17.808437+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - file-creation
verified: true
validated: true
---

# touch-create-empty-file

## Command

```bash
touch $_FILE_NAME
```

## Description

Creates an empty file or updates the timestamps of an existing file to the current time. Useful for initial setup in timestomping workflows or creating placeholders for payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_NAME | Name of the file to create or update (e.g., "example.txt") | Yes |

## Examples

### Basic Usage

```bash
touch example.txt
```

### Usage with Quotes for Spaces

```bash
touch "my file.txt"
```

## Expected Output

No output on success. Verify with `ls -l $_FILE_NAME` to see the file with current timestamps (e.g., `-rw-r--r-- 1 user user 0 Oct 1 12:00 example.txt`). Error if no write permissions: `touch: cannot touch 'example.txt': Permission denied`.

## Related

- [[procedures/Linux-Timestomping-Evasion]]
