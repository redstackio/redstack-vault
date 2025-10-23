---
id: b8d6efdf-255a-4c82-9d14-dc59abb151f4
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.401326+00:00'
updated_at: '2023-04-10T20:34:31.019647+00:00'
---

# Code Snippet b8d6efdf

**Language**: Powershell

```powershell
level15@nebula:/home/flag15$ cp /lib/i386-linux-gnu/libc.so.6 /var/tmp/flag15/

level15@nebula:/home/flag15$ ldd ./flag15 
 linux-gate.so.1 =>  (0x005b0000)
 libc.so.6 => /var/tmp/flag15/libc.so.6 (0x00110000)
 /lib/ld-linux.so.2 (0x00737000)
```


