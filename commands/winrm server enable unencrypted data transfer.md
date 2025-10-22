---
id: 43a1fcf3-46c3-4581-9754-8d217d8d6ecb
name: winrm server enable unencrypted data transfer
type: command
executor: bash
data: 'winrm set winrm/config/Service @{AllowUnencrypted="true"}

  '
output: null
created_at: '2020-07-14T18:21:13.085647+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# winrm server enable unencrypted data transfer

```bash
winrm set winrm/config/Service @{AllowUnencrypted="true"}

```
