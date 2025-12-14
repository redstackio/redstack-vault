---
id: cmd-base64-encode
data: echo -n 'pwd' | base64
tags:
  - encoding
  - rce
type: command
output: cHdk
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.381Z'
verified: false
validated: true
submitted: true
---
# base64-encode-cmd

## Command

```bash
echo -n 'pwd' | base64
```

## Description

Encodes a command string to base64 for safe transmission via URL parameters in webshell execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | No trailing newline | Yes |
| `'pwd'` | Command to encode | Yes |

## Examples

### Basic Usage

```bash
echo -n 'pwd' | base64
```

### Advanced Usage

```bash
echo -n 'ls -la /etc' | base64
```

## Expected Output

Base64 string, e.g., "cHdk" for 'pwd'.

## Related

- [[procedures/Execute-Commands-via-Shell]]
