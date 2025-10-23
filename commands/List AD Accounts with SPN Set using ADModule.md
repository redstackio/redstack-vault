---
id: a63d756b-5f43-4d83-a9cb-a95698ee367e
name: List AD Accounts with SPN Set using ADModule
type: command
executor: ''
data: Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
output: null
created_at: '2023-01-12T17:49:32.489275+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List AD Accounts with SPN Set using ADModule

```bash
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```


