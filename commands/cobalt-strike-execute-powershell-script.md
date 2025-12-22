---
id: 3a8053cf-3396-4a12-ae53-256667f14c90
name: cobalt-strike-execute-powershell-script
type: command
executor: bash
data: powershell function_name arguments
output: null
created_at: '2023-04-06T03:56:26.779943+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - cobalt-strike
  - powershell
verified: true
validated: true
---

# Cobalt Strike Execute PowerShell Script

## Command

```bash
powershell function_name arguments
```

## Description

Executes a previously imported PowerShell function via managed PowerShell in a Beacon session. Beacon sets up a temporary local TCP server to download and run the script, capturing output for the attacker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `function_name` | Name of the function to execute from the imported script | Yes |
| `arguments` | Optional parameters passed to the function | No |

## Examples

### Basic Usage

```bash
powershell Get-SystemInfo
```

Runs `Get-SystemInfo` without arguments.

### Advanced Usage

```bash
powershell Invoke-Discovery -Path C:\Users
```

Passes a path argument to the function.

## Expected Output

Function results streamed back to Beacon, e.g., "OS: Windows 10, Users: admin, guest". Errors like "Function not found" if import failed.

## Related

- [[commands/cobalt-strike-import-powershell-script-into-beacon-memory]]
- [[procedures/powershell-script-execution-with-cobalt-strike]]
