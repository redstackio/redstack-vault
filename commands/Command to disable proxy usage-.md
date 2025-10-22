---
id: 040e9ec6-e03d-4971-9a5e-698ad94d60fb
name: 'Command to disable proxy usage:'
type: command
executor: bash
data: "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\"\
  \ /v ProxyEnable /t REG_DWORD /d 0 /f \n"
output: null
created_at: '2020-07-14T18:21:27.748475+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Command to disable proxy usage:

```bash
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f 

```
