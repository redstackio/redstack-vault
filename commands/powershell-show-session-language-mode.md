---
id: 8c278673-acef-44eb-8908-dfa16096784f
name: powershell-show-session-language-mode
type: command
executor: powershell
data: $ExecutionContext.SessionState.LanguageMode
output: |-
  PS C:\> $ExecutionContext.SessionState.LanguageMode
  ConstrainedLanguage
created_at: '2020-03-30T18:49:29.621558+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - Enumeration
  - Discovery
verified: true
validated: true
---

# powershell-show-session-language-mode

## Command

```powershell
$ExecutionContext.SessionState.LanguageMode
```

## Description

This command queries the current PowerShell session's language mode, revealing if restrictions like Constrained Language Mode are active. It is used during reconnaissance to determine scripting limitations in the target environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a parameterless variable query; no flags or arguments needed. | N/A |

## Examples

### Basic Usage

```powershell
$ExecutionContext.SessionState.LanguageMode
```

### Advanced Usage

Run in a script for logging:

```powershell
Write-Output "Language Mode: $($ExecutionContext.SessionState.LanguageMode)"
```

## Expected Output

When successful, the command outputs the language mode string directly in the console.

```
PS C:\> $ExecutionContext.SessionState.LanguageMode
ConstrainedLanguage
```

In FullLanguage mode, it would output 'FullLanguage'. If in a restricted context, it may error or show 'RestrictedLanguage'.

## Related

- [[procedures/Check-PowerShell-Session-Language-Mode]]
