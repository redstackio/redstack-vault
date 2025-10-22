---
id: 1bace875-2ba2-4783-a63f-8eb0baa68a12
type: code
language: Powershell
verified: false
created_at: '2023-05-23T19:23:01.810548+00:00'
updated_at: '2023-05-23T19:23:38.779149+00:00'
---

# Code Snippet 1bace875

**Language**: Powershell

```powershell
PS> $passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force
PS> $creds = New-Object System.Management.Automation.PSCredential ("test@<TENANT NAME>.onmicrosoft.com", $passwd)
PS Az> Connect-AzAccount -Credential $creds

PS Az> Get-AzResource
PS Az> Get-AzRoleAssignment -SignInName test@<TENANT NAME>.onmicrosoft.com
PS Az> Get-AzVM | fl
PS Az> Get-AzWebApp | ?{$_.Kind -notmatch "functionapp"}
PS Az> Get-AzFunctionApp
PS Az> Get-AzStorageAccount | fl
PS Az> Get-AzKeyVault
```
