---
id: 6e4ae063-f82a-4549-b5db-c82aaaa23217
name: View Permissions for Sales.vIndividualCustomer
type: command
executor: bash
data: SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER
  BY subentity_name, permission_name;
output: null
created_at: '2023-04-06T03:56:34.157896+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
---

# View Permissions for Sales.vIndividualCustomer

```bash
SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER BY subentity_name, permission_name;
```


