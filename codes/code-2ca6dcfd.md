---
id: 2ca6dcfd-3d12-4758-a2a5-95fbe937d2c0
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:00.324759+00:00'
updated_at: '2023-04-10T20:33:54.897545+00:00'
---

# Code Snippet 2ca6dcfd

**Language**: Powershell

```powershell
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u
```


