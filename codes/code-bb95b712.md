---
id: bb95b712-ec69-432a-b3e0-f0aa31e8f9cc
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:26.573022+00:00'
updated_at: '2023-04-10T20:37:05.283623+00:00'
---

# Code Snippet bb95b712

**Language**: ps1

```ps1
function Enable-PSScriptBlockLogging
{
    $basePath = 'HKLM:\Software\Policies\Microsoft\Windows' +
      '\PowerShell\ScriptBlockLogging'

    if(-not (Test-Path $basePath))
    {
        $null = New-Item $basePath -Force
    }

    Set-ItemProperty $basePath -Name EnableScriptBlockLogging -Value "1"
}
```
