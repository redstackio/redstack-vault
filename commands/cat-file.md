---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: cat-file
type: command
executor: bash
data: cat /etc/hosts
output: null
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:12.507Z'
platforms:
  - Linux
tags:
  - verification
  - file-read
verified: false
validated: true
submitted: true
---

# cat-file

## Command

```bash
cat /etc/hosts
```

## Description

This command displays the contents of a file, used here to verify if an arbitrary write via path traversal has modified a sensitive system file like /etc/hosts on Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/hosts` | Path to the target file to read | Yes |

## Examples

### Basic Usage

```bash
cat /etc/hosts
```

### Advanced Usage

```bash
cat /var/log/app.log | grep "injected"
```

## Expected Output

Contents of the file, including any injected lines (e.g., "127.0.0.1 attacker-controlled") if the exploitation succeeded.

## Related

- [[Related Procedure|procedures/Exploit-Path-Traversal-for-Arbitrary-File-Write-in-Java-App]]
