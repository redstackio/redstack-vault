---
id: 646ee7e3-57a9-45e1-be0a-df4fb09c579a
name: Enumerate SMB Sessions
type: command
executor: bash
data: 'cme smb 10.10.10.0/24 -u Administrator -p ''P@ssw0rd'' --sessions

  SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [+] Enumerated sessions

  SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  \\10.10.10.10            User:Administrator'
output: null
created_at: '2023-04-06T03:56:04.178975+00:00'
updated_at: '2023-04-10T20:36:03.709267+00:00'
---

# Enumerate SMB Sessions

```bash
cme smb 10.10.10.0/24 -u Administrator -p 'P@ssw0rd' --sessions
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [+] Enumerated sessions
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  \\10.10.10.10            User:Administrator
```


