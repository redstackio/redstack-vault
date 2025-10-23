---
id: 62f3142b-4c4e-46d3-baa6-7e45bef01872
name: Get Domain Computer Object SID
type: command
executor: bash
data: $SID_FROM_PREVIOUS_COMMAND = Get-DomainComputer MACHINE_ACCOUNT_NAME -Properties
  objectsid | Select -Expand objectsid
output: null
created_at: '2023-04-06T03:56:07.771479+00:00'
updated_at: '2023-04-06T03:56:07.808296+00:00'
---

# Get Domain Computer Object SID

```bash
$SID_FROM_PREVIOUS_COMMAND = Get-DomainComputer MACHINE_ACCOUNT_NAME -Properties objectsid | Select -Expand objectsid
```


