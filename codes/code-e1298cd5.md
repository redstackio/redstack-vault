---
id: e1298cd5-4b26-4cb8-88a0-87dbc66d48bf
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:27.428300+00:00'
updated_at: '2023-04-10T20:37:15.532586+00:00'
---

# Code Snippet e1298cd5

**Language**: ps1

```ps1
sc queryex termservice
tasklist /M:rdpcorets.dll
netstat -nob | Select-String TermService -Context 1
```
