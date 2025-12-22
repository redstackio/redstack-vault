---
id: 4e6abbd5-11f4-473f-af47-a116751dc5bb
name: make-findomain-linux-executable
type: command
executor: bash
data: chmod +x findomain-linux
output: null
created_at: '2023-04-06T03:56:25.542001+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - permissions
verified: true
validated: true
---

# make-findomain-linux-executable

## Command

```bash
chmod +x findomain-linux
```

## Description

This command sets execute permissions on the Findomain Linux binary, enabling it to be run directly from the command line.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +x | Adds execute permission for owner | Built-in |
| findomain-linux | Path to the binary file | Yes |

## Examples

### Basic Usage

```bash
chmod +x findomain-linux
```

### Recursive for Directory

```bash
chmod +x /opt/tools/findomain-linux
```

## Expected Output

No output on success. Use 'ls -la findomain-linux' to confirm: the permissions should show '-rwxr-xr-x' instead of '-rw-r--r--'.

## Related

- [[procedures/Subdomain-Enumeration-with-Findomain]]
- [[commands/download-findomain-linux-binary]]
