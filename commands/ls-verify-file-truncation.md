---
id: cmd-ls-verify-truncation
data: ls -asl /tmp/written
tags:
  - verification
  - file-system
type: command
output: '-rw-r--r-- 1 git git 0 Jul 22 14:56 /tmp/written (empty file created)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.763Z'
verified: false
validated: true
submitted: true
---
# ls-verify-file-truncation

## Command

```bash
ls -asl /tmp/written
```

## Description

Lists details of the file /tmp/written, showing its size and permissions to verify creation and truncation after the API request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Show all files | Yes |
| -s | Display size | Yes |
| -l | Long format | Yes |
| /tmp/written | Target file path | Yes |

## Examples

### Basic Usage

```bash
ls -asl /tmp/written
```

### Advanced Usage

Use for any truncated file: ls -asl /path/to/file.

## Expected Output

-rw-r--r-- 1 git git 0 Jul 22 14:56 /tmp/written, confirming empty file.

## Related

- [[procedures/Verify-File-Truncation-with-Ls]]
