---
data: cmd.exe /c " + cmd
tags:
  - rce
  - webshell
type: command
output: Output of the executed command
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.145Z'
id: 4e7ee76d-4128-466f-a501-94ef7ee637ec
verified: false
validated: true
submitted: true
---
# webshell-execute-arbitrary

## Command

```cmd
cmd.exe /c " + cmd
```

## Description

Core execution logic in the ASPX webshell: runs arbitrary 'cmd' from query string via CMD.exe /c, capturing and returning stdout; 'cmd' is dynamically substituted (e.g., from Request.QueryString).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /c | Carry out the command and terminate | Yes |
| cmd | Arbitrary command string from query param | Yes |

## Examples

### Basic Usage

```cmd
cmd.exe /c dir
```

### Advanced Usage

```cmd
cmd.exe /c "net user"
```

## Expected Output

Stdout of the command, e.g., directory contents or user list, written to HTTP response.

## Related

- [[Related Procedure: Execute-Commands-via-Uploaded-Webshell]]
