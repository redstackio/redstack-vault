---
id: 3d9faa7e-a34f-49e9-a134-092c8c9463b2
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:54:08.675522+00:00'
updated_at: '2023-05-24T07:54:51.686920+00:00'
---

# Code Snippet 3d9faa7e

**Language**: Powershell

```powershell
# Import the AzureAD module by running the 'Import-Module' command with the path to the AzureAD.psd1 file.
Import-Module C:\Tools\AzureAD\AzureAD.psd1

# Create an access token for Azure AD by setting the '$AADToken' variable to the access token value.
$AADToken = 'eyJ0…'

# Connect to Azure AD using the 'Connect-AzureAD' command with the '-AadAccessToken', '-TenantId', and '-AccountId' arguments. Replace <TENANT-ID> with your tenant ID and <ACCOUNT-ID> with your account ID.
Connect-AzureAD -AadAccessToken $AADToken -TenantId <TENANT-ID> -AccountId <ACCOUNT-ID>
```


