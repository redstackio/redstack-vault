---
id: cmd-windows-calc-launch
data: cmd /C calc
tags:
  - rce
  - execution
type: command
output: Launches calc.exe calculator application
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.285Z'
verified: false
validated: true
submitted: true
---
# cmd-execute-calc

## Command

```cmd
cmd /C calc
```

## Description

This Windows command launches the calculator application (calc.exe) via the command shell, used here in a CSV formula injection to demonstrate client-side RCE when triggered by Excel.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /C | Carries out the command and then terminates the shell | Yes |
| calc | Executes calc.exe, the Windows calculator | Yes |

## Examples

### Basic Usage

```cmd
cmd /C calc
```

### Advanced Usage

```cmd
cmd /C calc & echo "Executed"
```

## Expected Output

The calculator window opens on the Windows desktop. No console output; visual application launch confirms success. In formula context, it runs silently on CSV open.

## Related

- [[Related Procedure: Exploiting-CSV-Injection-for-Client-Side-RCE-in-Excel]]
