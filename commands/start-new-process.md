---
id: a20149db-5e77-43b8-8caa-7addc84a46a6
name: Start-New-Process
type: command
executor: powershell
data: Start-Process -FilePath $_FILE_PATH -ArgumentList $_ARGUMENTS -Verb $_VERB
output: null
created_at: '2023-04-06T03:56:26.428950+00:00'
updated_at: '2023-04-10T20:37:06.785363+00:00'
platforms:
  - Windows
tags:
  - powershell
  - execution
verified: true
validated: true
---

# Start-New-Process

## Command

```powershell
Start-Process -FilePath $_FILE_PATH -ArgumentList $_ARGUMENTS -Verb $_VERB
```

## Description

Starts one or more processes on the local machine, useful for launching applications in a controlled JEA environment without shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -FilePath | Path to the executable (e.g., 'notepad.exe') | Yes |
| -ArgumentList | Array of arguments to pass to the process | No |
| -Verb | Action like 'RunAs' for elevation (if allowed) | No |
| -WorkingDirectory | Starting directory for the process | No |

## Examples

### Basic Usage

```powershell
Start-Process notepad.exe
```

### Advanced Usage

```powershell
Start-Process -FilePath 'C:\Windows\System32\calc.exe' -ArgumentList '/?' -WorkingDirectory 'C:\'
```

## Expected Output

The process starts silently; no output unless -Wait or -PassThru is used (e.g., returns a Process object).

## Related

- [[procedures/implement-jea-to-limit-powershell-cmdlet-usage]]
