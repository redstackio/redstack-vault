---
id: 8a9f6edb-60bb-431a-8420-686425fe923f
name: List SMB Shares
type: command
executor: bash
data: smbclient -I 10.10.10.100 -L ACTIVE -N -U ""
output: null
created_at: '2023-04-06T03:56:03.238680+00:00'
updated_at: '2023-04-10T20:26:35.786286+00:00'
---

# List SMB Shares

```bash
smbclient -I 10.10.10.100 -L ACTIVE -N -U ""
```


