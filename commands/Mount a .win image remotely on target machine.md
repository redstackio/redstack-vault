---
id: aa4a7754-4b4d-4b84-88f2-bc2d5f60343c
name: Mount a .win image remotely on target machine
type: command
executor: bash
data: 'Dism /get-wiminfo /wimfile:z:\win7\Acme_Win7.wim Boot Dir

  Dism /Mount-Wim /WimFile:z:\win7\Acme_Win7.wim /index:1 /MountDir:C:\windows\temp\offline
  C: Drive

  Dism /Mount-Wim /WimFile:z:\win7\Acme_Win7.wim /index:2 /MountDir:C:\windows\temp\offline
  Dism /UnMount-Wim /MountDir:C:\windows\temp\offline /discard

  '
output: null
created_at: '2020-07-14T18:21:27.749133+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mount a .win image remotely on target machine

```bash
Dism /get-wiminfo /wimfile:z:\win7\Acme_Win7.wim Boot Dir
Dism /Mount-Wim /WimFile:z:\win7\Acme_Win7.wim /index:1 /MountDir:C:\windows\temp\offline C: Drive
Dism /Mount-Wim /WimFile:z:\win7\Acme_Win7.wim /index:2 /MountDir:C:\windows\temp\offline Dism /UnMount-Wim /MountDir:C:\windows\temp\offline /discard

```
