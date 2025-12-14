---
data: 'cmd /c {szCMD}'
tags:
  - execution
  - rce
type: command
output: Output of the executed command
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.300Z'
id: d09c7c94-602d-4e74-8de5-6a37559a55f4
verified: false
validated: true
submitted: true
---
# windows-cmd-c

## Command

```cmd
cmd /c {szCMD}
```

## Description

Runs an arbitrary command in the Windows command prompt and captures its output, used within the ASP shell's getCommandOutput function where {szCMD} is user input from the 'cmd' request parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /c | Carries out the command and terminates | Yes |
| {szCMD} | The command to execute (e.g., 'dir') | Yes |

## Examples

### Basic Usage

```cmd
cmd /c dir
```

### Advanced Usage

```cmd
cmd /c whoami
```

## Expected Output

Stdout from the specified command, e.g., for 'dir', a listing of files and directories.

## Related

- [[commands/windows-dir]]
- [[procedures/Execute-Commands-via-Uploaded-ASPShell]]
