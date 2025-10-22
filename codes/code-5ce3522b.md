---
id: 5ce3522b-7ab2-416e-b827-ed373648f5e9
type: code
language: Powershell
verified: false
created_at: '2023-05-23T19:23:37.738072+00:00'
updated_at: '2023-05-23T19:23:39.384689+00:00'
---

# Code Snippet 5ce3522b

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
