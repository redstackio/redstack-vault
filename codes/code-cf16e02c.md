---
id: cf16e02c-cf84-415f-aeaa-1a633fefc6d6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:31.141107+00:00'
updated_at: '2023-04-10T20:37:59.144920+00:00'
---

# Code Snippet cf16e02c

**Language**: Powershell

```powershell
PS> Enter-PSSession -computerName DC01
[DC01]: PS>

# one-to-one execute scripts and commands
PS> $Session = New-PSSession -ComputerName CLIENT1
PS> Invoke-Command -Session $Session -scriptBlock { $test = 1 }
PS> Invoke-Command -Session $Session -scriptBlock { $test }
1
```
