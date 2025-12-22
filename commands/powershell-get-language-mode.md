---
id: d09298eb-6548-457f-be21-47cf9b10208c
name: powershell-get-language-mode
type: command
executor: powershell
data: $ExecutionContext.SessionState.LanguageMode
output: null
created_at: '2023-04-06T03:56:23.987142+00:00'
updated_at: '2023-10-10T20:37:00.452402+00:00'
platforms:
  - Windows
tags:
  - powershell
  - discovery
verified: true
validated: true
---

# powershell-get-language-mode

## Command

```powershell
$ExecutionContext.SessionState.LanguageMode
```

## Description

This command queries the current PowerShell session's language mode, indicating whether it is in FullLanguage (unrestricted) or ConstrainedLanguage (restricted for security). Use this during initial assessment in a PowerShell session to detect defensive restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a variable query with no parameters. | No |

## Examples

### Basic Usage

```powershell
$ExecutionContext.SessionState.LanguageMode
```

### In a Script Context

```powershell
if ($ExecutionContext.SessionState.LanguageMode -eq 'ConstrainedLanguage') { Write-Output 'Restricted mode detected' }
```

## Expected Output

ConstrainedLanguage

(or FullLanguage if unrestricted)

## Related

- [[procedures/Check-and-Bypass-PowerShell-Constrained-Language-Mode]]
