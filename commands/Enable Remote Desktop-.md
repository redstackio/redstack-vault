---
id: 93576826-091f-4640-af60-9426cfb50d53
name: 'Enable Remote Desktop:'
type: command
executor: bash
data: 'reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
  /t REG_DWORD /d 0 /f

  '
output: null
created_at: '2020-07-14T18:21:27.748083+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enable Remote Desktop:

```bash
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

```
