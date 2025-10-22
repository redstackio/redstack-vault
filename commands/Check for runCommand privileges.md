---
id: 70c4f900-680f-425b-8061-48ffb81dc5fd
name: Check for runCommand privileges
type: command
executor: bash
data: '$URI = ''https://management.azure.com/subscriptions/b413826f-108d-4049-8c11-d52d5d388768/resources?api-version=2020-10-01''

  $URI = ''https://management.azure.com/subscriptions/b413826f-108d-4049-8c11-d52d5d388768/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'''
output: null
created_at: '2023-05-24T08:00:06.079448+00:00'
updated_at: '2023-05-24T08:06:29.009007+00:00'
---

# Check for runCommand privileges

```bash
$URI = 'https://management.azure.com/subscriptions/b413826f-108d-4049-8c11-d52d5d388768/resources?api-version=2020-10-01'
$URI = 'https://management.azure.com/subscriptions/b413826f-108d-4049-8c11-d52d5d388768/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
```
