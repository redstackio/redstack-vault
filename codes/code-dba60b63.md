---
id: dba60b63-3501-4d7b-be3f-95eb7f2804f6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.335855+00:00'
updated_at: '2023-04-10T20:25:09.845260+00:00'
---

# Code Snippet dba60b63

**Language**: Powershell

```powershell
openssl req -subj '/CN=[domain.of.server.to.mitm]' -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem
```


