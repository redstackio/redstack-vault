---
data: |-
  @echo off
  START C:\Windows\NOTEPAD.EXE
tags:
  - rce
  - batch
  - execution
type: command
output: Notepad application launches without console output.
executor: cmd
platforms:
  - Windows
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T03:46:31.993Z'
id: 6181f358-f0da-4052-b65e-ee2221d048c8
verified: false
validated: true
submitted: true
---
# Launch Notepad via Batch Script

## Command

```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

## Description

This Windows batch command suppresses command echoing and launches the Notepad executable, demonstrating basic remote code execution in an attack context where the script is disguised and executed by the user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `@echo off` | Disables command echoing to the console for stealth | Yes |
| `START` | Initiates the launch of the specified program | Yes |
| `C:\Windows\NOTEPAD.EXE` | Path to the Notepad executable | Yes |

## Examples

### Basic Usage

```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

### Advanced Usage

```batch
@echo off
START "" "C:\Windows\System32\calc.exe"
```

> Launches Calculator instead; replace path for different RCE payloads.

## Expected Output

The Notepad application opens in a new window with no visible console output, confirming successful execution. In a file context, the batch runs silently upon opening.

## Related

- [[Related Procedure: Execute Downloaded Malicious Batch File]]
