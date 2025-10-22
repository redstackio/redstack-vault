---
id: cc88b0a8-cee1-4eef-823d-3516b2416552
name: 'Command to enable proxy usage:'
type: command
executor: bash
data: "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\"\
  \ /v ProxyEnable /t REG_DWORD /d 1 /f \n"
output: null
created_at: '2020-07-14T18:21:27.748327+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Command to enable proxy usage:

```bash
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f 

```
