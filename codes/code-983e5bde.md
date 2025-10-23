---
id: 983e5bde-d248-4119-aabe-a49263f4b089
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.847641+00:00'
updated_at: '2023-04-10T20:19:31.153686+00:00'
---

# Code Snippet 983e5bde

**Language**: Powershell

```powershell
PS AzureAD> Get-AzureADMSAdministrativeUnit -Id <ID>
- This command retrieves the administrative units in Azure AD based on the specified ID.

PS AzureAD> Get-AzureADMSAdministrativeUnitMember -Id <ID>
- This command retrieves the administrative unit members in Azure AD based on the specified ID.

PS AzureAD> Get-AzureADMSScopedRoleMembership -Id <ID> | fl
- This command retrieves the scoped role membership in Azure AD based on the specified ID and displays the output in a formatted list.

PS AzureAD> Get-AzureADDirectoryRole -ObjectId <RoleId>
- This command retrieves the directory role in Azure AD based on the specified role ID.

PS AzureAD> Get-AzureADUser -ObjectId <RoleMemberInfo.Id> | fl 
- This command retrieves the user in Azure AD based on the specified user ID and displays the output in a formatted list.

PS C:\Tools> $password = "Password" | ConvertToSecureString -AsPlainText -Force
- This command creates a new secure string object based on the specified password.

PS C:\Tools> (Get-AzureADUser -All $true | ?{$_.UserPrincipalName -eq "<Username>@<TENANT NAME>.onmicrosoft.com"}).ObjectId | SetAzureADUserPassword -Password $Password -Verbose
- This command retrieves the object ID of the user with the specified user principal name and sets the user's password to the specified secure string object.
```


