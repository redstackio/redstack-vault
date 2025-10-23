---
id: 6e4b1257-c520-4a22-b76c-8e96bdbdc2b2
name: vssadmin create command only applies to Server OS (Win2k3,2008)
type: command
executor: command_prompt
data: 'vssadmin list shadows

  vssadmin create shadow /for=C:

  wmic /node:DC1 /user:DOMAIN\domainadminsvc /password:domainadminsvc123 process call
  create "cmd /c vssadmin create shadow /for=C

  mklink /D C:\VscAccess \\?\GLOBALROOT\Device\HardDiskVolumeShadowCopy1

  copy \\?\GLOBALROOT\Device\HardDiskVolumeShadowCopy4\path\to\some\file e:\files

  '
output: null
created_at: '2020-07-14T18:21:24.520056+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# vssadmin create command only applies to Server OS (Win2k3,2008)

```command_prompt
vssadmin list shadows
vssadmin create shadow /for=C:
wmic /node:DC1 /user:DOMAIN\domainadminsvc /password:domainadminsvc123 process call create "cmd /c vssadmin create shadow /for=C
mklink /D C:\VscAccess \\?\GLOBALROOT\Device\HardDiskVolumeShadowCopy1
copy \\?\GLOBALROOT\Device\HardDiskVolumeShadowCopy4\path\to\some\file e:\files

```


