---
data: ls -la /tmp
tags:
  - list
  - tmp
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.191Z'
id: 7b07fbf9-2017-485c-a3e8-c0b45f61e0c2
verified: false
validated: true
submitted: true
---
# ls-list-tmp-files

## Command

```bash
ls -la /tmp
```

## Description

Lists all files in /tmp with long format details, including permissions, to verify clean state or check for created artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -la | Long format with all files, including hidden | Yes |
| /tmp | Target directory | Yes |

## Examples

### Basic Usage

```bash
ls -la /tmp
```

### Advanced Usage

```bash
ls -la /tmp | grep evilbash
```

## Expected Output

Directory listing; no /tmp/evilbash pre-exploit, or SUID post-exploit.

## Related

- [[procedures/Verify-Clean-System-State]]
- [[procedures/Execute-SUID-Bash-for-Root-Access]]
