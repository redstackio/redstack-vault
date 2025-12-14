---
data: cmd /c <command>
tags:
  - execution
  - rce
type: command
output: Output of the executed command
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.431Z'
id: 50e7ccbd-d73e-4210-9483-77f4a8b3b53b
verified: false
validated: true
submitted: true
---
# windows-cmd-c

## Command

```cmd
cmd /c <command>
```

## Description

The 'cmd /c' runs a command in the Windows command interpreter and terminates after execution, capturing output. In the ASP shell, it's used to execute user-provided commands like 'dir' for RCE demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /c | Carries out the command and terminates | Yes |
| <command> | The command to execute (e.g., dir) | Yes |

## Examples

### Basic Usage

```cmd
cmd /c dir
```

### Advanced Usage

```cmd
cmd /c whoami /all
```

## Expected Output

Results of the inner command, such as directory contents or user info, piped back to the shell output.

## Related

- [[commands/windows-dir]]
