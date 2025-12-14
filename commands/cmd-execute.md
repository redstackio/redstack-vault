---
data: cmd.exe /c <cmd>
tags:
  - execution
  - rce
type: command
output: 'Output of the specified <cmd>, redirected to HTTP response.'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.388Z'
id: 7fdab7e0-0b82-4060-aeee-513db0aba6c3
verified: false
validated: true
submitted: true
---
# cmd-execute

## Command

```cmd
cmd.exe /c <cmd>
```

## Description

Executes a specified command on Windows via cmd.exe and terminates after completion. Used in deserialization payloads to run arbitrary commands passed from HTTP headers during RCE exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /c | Carries out the command specified by <cmd> and then terminates | Yes |
| <cmd> | The command to execute (e.g., systeminfo) | Yes |

## Examples

### Basic Usage

```cmd
cmd.exe /c systeminfo
```

### Advanced Usage

```cmd
cmd.exe /c dir C:\
```

## Expected Output

The stdout of the <cmd>, such as system information or directory listing, captured and potentially redirected in exploit contexts.

## Related

- [[Related Procedure|procedures/Exploit-Liferay-Deserialization-RCE]]
