---
id: edb0b0e5-77e3-4f69-9e08-9270192ec526
name: Add other email to Azure AD user
type: command
executor: bash
data: Set-AzureADUser -ObjectId <OBJECT-ID> -OtherMails <Username>@<TENANT NAME>.onmicrosoft.com
  -Verbose
output: null
created_at: '2023-04-06T03:56:15.819994+00:00'
updated_at: '2023-04-10T20:19:27.894315+00:00'
---

# Add other email to Azure AD user

```bash
Set-AzureADUser -ObjectId <OBJECT-ID> -OtherMails <Username>@<TENANT NAME>.onmicrosoft.com -Verbose
```


