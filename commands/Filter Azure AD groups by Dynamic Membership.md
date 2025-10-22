---
id: ccb4c82b-a5d0-4e09-bbbf-010a64949cd6
name: Filter Azure AD groups by Dynamic Membership
type: command
executor: bash
data: Get-AzureADMSGroup | ?{$_.GroupTypes -eq 'DynamicMembership'}
output: null
created_at: '2023-04-06T03:56:15.788312+00:00'
updated_at: '2023-04-10T20:19:31.729228+00:00'
---

# Filter Azure AD groups by Dynamic Membership

```bash
Get-AzureADMSGroup | ?{$_.GroupTypes -eq 'DynamicMembership'}
```
