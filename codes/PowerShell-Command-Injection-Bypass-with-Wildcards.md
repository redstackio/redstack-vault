---
id: 21f0238f-f2fc-46e2-8b70-cfc996ea4252
type: code
language: PowerShell
verified: true
created_at: '2023-04-06T03:55:57.394481+00:00'
updated_at: '2023-04-06T03:55:57.397461+00:00'
tags:
  - bypass-wildcards
  - command-injection
  - filter-bypass
platforms:
  - Windows
validated: true
---

# PowerShell-Command-Injection-Bypass-with-Wildcards

## Code

```powershell
powershell C:\*\*2\n??e*d.*? # notepad
@^p^o^w^e^r^shell c:\*\*32\c*?c.e?e # calc
```

## Description

This PowerShell code snippet demonstrates filter evasion for command injection by using wildcards to obfuscate executable paths and caret escaping for the PowerShell interpreter. The first line launches Notepad by matching its path with wildcards, while the second launches Calculator using escaped 'powershell' and wildcard path matching. It is designed for injection into vulnerable inputs that execute system commands on Windows.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This code has no runtime variables; wildcards are static obfuscation patterns. Customize wildcards based on target filter rules. | N/A |

## Usage

Inject this code into a vulnerable web form, API endpoint, or script input that passes data to a system command executor (e.g., via `system()` in PHP or similar). For example, if the app runs user input as a shell command, this will execute the obfuscated PowerShell to spawn Notepad or Calculator. Use in red team engagements to test input sanitization or as a precursor to more destructive payloads.

## Detection

- Monitor for wildcard usage in command logs or WAF alerts.
- Enable PowerShell execution logging to capture obfuscated invocations.
- Look for anomalous process spawns like notepad.exe or calc.exe from web processes.
- Regex patterns in logs for * or ? in paths, or escaped strings like ^p^o^w...

## Related

- [[procedures/Command-Injection-Filter-Bypass-with-PowerShell]]
