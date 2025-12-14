---
id: cmd-uuid-2
data: ls
name: ls
tags:
  - recon
  - filesystem
type: command
output: List of files and directories
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.639Z'
verified: false
validated: true
submitted: true
---
# ls

## Command

```bash
ls
```

## Description

Lists the contents of the current directory, commonly used in post-exploitation to explore the filesystem after gaining access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Long format listing | No |
| -a | Include hidden files | No |

## Examples

### Basic Usage

```bash
ls
```

### Advanced Usage

```bash
ls -la /etc
```
(Shows detailed listing including hidden files in /etc)

## Expected Output

A list of files and directories in the current working directory, e.g., `file1.txt dir1 config.conf`.

## Related

- [[Related Procedure]]
