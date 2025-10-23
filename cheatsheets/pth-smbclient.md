---
id: e418ec69-458d-4875-bfe2-37d917b5c30a
name: pth-smbclient
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:43.463283+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# pth-smbclient



**Command** ([[connect to target-share and auth via ntlm-hash]]):

```bash
pth-smbclient --user=username --pw-nt-hash -m smb3 \\\\target-ip\\target-share ntlm-hash

```






