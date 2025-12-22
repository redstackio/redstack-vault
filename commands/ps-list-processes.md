---
id: cmd-uuid-4
data: ps auxww
tags:
  - recon
  - process-enum
type: command
output: >-
  Detailed process list including puma workers, nginx, exiftool invocation, and
  the reverse shell ruby process
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.908Z'
verified: false
validated: true
submitted: true
---
# ps-list-processes

## Command

```bash
ps auxww
```

## Description

Lists all running processes with full command lines, used in reverse shell to enumerate GitLab environment including puma, nginx, and exiftool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| a | All users | Yes |
| u | User-oriented format | Yes |
| x | Processes without tty | Yes |
| ww | Wide output, no truncation | Yes |

## Examples

### Basic Usage

```bash
ps auxww
```

### Advanced Usage

```bash
ps aux | grep exiftool
```

## Expected Output

Detailed list showing processes like /opt/gitlab/embedded/bin/exiftool, puma workers, nginx.

## Related

- [[commands/id-display-user]]
- [[procedures/Verify-RCE-Impact-with-File-Write-or-Reverse-Shell]]
