---
id: 8c278673-acef-44eb-8908-dfa16096784f
name: PowerShell Show Current Language Mode
type: command
executor: powershell
data: $ExecutionContext.SessionState.LanguageMode
output: 'PS C:\> $ExecutionContext.SessionState.LanguageMode

  ConstrainedLanguage'
created_at: '2020-03-30T18:49:29.621558+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell Show Current Language Mode

```powershell
$ExecutionContext.SessionState.LanguageMode
```

## Expected Output

```
PS C:\> $ExecutionContext.SessionState.LanguageMode
ConstrainedLanguage
```


