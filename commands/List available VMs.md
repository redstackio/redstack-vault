---
id: 10b3d6df-a84d-4677-ace6-46b3b443762e
name: List available VMs
type: command
executor: bash
data: Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name
output: "Get-AzureRmVM -status | where {$_.PowerState -EQ \"VM running\"} | select\
  \ ResourceGroupName,Name\n\nResourceGroupName    Name       \n-----------------\
  \    ----       \nTESTRESOURCES        Remote-Test"
created_at: '2023-05-28T03:59:38.556373+00:00'
updated_at: '2023-05-28T03:59:38.880779+00:00'
---

# List available VMs

```bash
Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name
```

## Expected Output

```
Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name

ResourceGroupName    Name       
-----------------    ----       
TESTRESOURCES        Remote-Test
```


