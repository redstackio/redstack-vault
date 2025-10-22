---
id: 1937a5aa-92e9-49dd-bae5-31bab60b575e
name: 'Command to change the proxy address:'
type: command
executor: bash
data: "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\"\
  \ /v ProxyServer /t REG_SZ /d proxyserveraddress:proxyport /f \n"
output: null
created_at: '2020-07-14T18:21:27.748817+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Command to change the proxy address:

```bash
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d proxyserveraddress:proxyport /f 

```
