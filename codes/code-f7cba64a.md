---
id: f7cba64a-7b9a-49b4-b455-6307d30db336
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.400806+00:00'
updated_at: '2023-04-10T20:34:31.019647+00:00'
---

# Code Snippet f7cba64a

**Language**: Powershell

```powershell
level15@nebula:/home/flag15$ readelf -d flag15 | egrep "NEEDED|RPATH"
 0x00000001 (NEEDED)                     Shared library: [libc.so.6]
 0x0000000f (RPATH)                      Library rpath: [/var/tmp/flag15]

level15@nebula:/home/flag15$ ldd ./flag15 
 linux-gate.so.1 =>  (0x0068c000)
 libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0x00110000)
 /lib/ld-linux.so.2 (0x005bb000)
```


