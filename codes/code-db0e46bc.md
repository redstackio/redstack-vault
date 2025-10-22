---
id: db0e46bc-3baf-4056-aafa-8afd5854f8b5
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:21.778468+00:00'
updated_at: '2023-04-10T20:21:18.293070+00:00'
---

# Code Snippet db0e46bc

**Language**: ps1

```ps1
host -t ns domain.local
domain.local name server master.domain.local.

host master.domain.local        
master.domain.local has address 192.168.1.1

dig axfr domain.local @192.168.1.1
```
