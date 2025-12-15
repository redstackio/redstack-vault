---
data: ls -la
tags:
  - explore
  - files
type: command
output: Detailed file listing
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.961Z'
id: 23163cc5-46a4-4013-bad9-a80830183f30
verified: false
validated: true
submitted: true
---
# ls-explore

## Command

```bash
ls -la
```

## Description

Lists directory contents in long format, including hidden files, to explore the root environment post-escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Long format | Yes |
| -a | All files (including .) | Yes |

## Examples

### Basic Usage

```bash
ls -la
```

### Advanced Usage

```bash
ls -la /etc/
```

## Expected Output

'total X
drwxr-xr-x 2 root root 4096 ... . .. file1 file2'

## Related

- [[commands/id-verify-root]]
- [[procedures/Capture-and-Verify-Root-Shell]]
