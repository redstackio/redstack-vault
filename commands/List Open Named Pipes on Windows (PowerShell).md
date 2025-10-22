---
id: 7d59b080-bdff-4fa0-bafb-08cf4d60fbe3
name: List Open Named Pipes on Windows (PowerShell)
type: command
executor: powershell
data: '[System.IO.Directory]::GetFiles("\\.\pipe\")'
output: 'PS C:\> [System.IO.Directory]::GetFiles("\\.\pipe\")

  \\.\pipe\InitShutdown

  \\.\pipe\lsass

  \\.\pipe\ntsvcs

  \\.\pipe\scerpc

  \\.\pipe\Winsock2\CatalogChangeListener-2b8-0

  \\.\pipe\Winsock2\CatalogChangeListener-3a8-0

  \\.\pipe\epmapper

  \\.\pipe\Winsock2\CatalogChangeListener-210-0

  \\.\pipe\LSM_API_service

  \\.\pipe\atsvc

  ...'
created_at: '2020-04-29T00:05:04.345714+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Open Named Pipes on Windows (PowerShell)

```powershell
[System.IO.Directory]::GetFiles("\\.\pipe\")
```

## Expected Output

```
PS C:\> [System.IO.Directory]::GetFiles("\\.\pipe\")
\\.\pipe\InitShutdown
\\.\pipe\lsass
\\.\pipe\ntsvcs
\\.\pipe\scerpc
\\.\pipe\Winsock2\CatalogChangeListener-2b8-0
\\.\pipe\Winsock2\CatalogChangeListener-3a8-0
\\.\pipe\epmapper
\\.\pipe\Winsock2\CatalogChangeListener-210-0
\\.\pipe\LSM_API_service
\\.\pipe\atsvc
...
```
