---
id: cb81c10e-9435-4570-b844-ab7ef1547cf3
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:19.401657+00:00'
updated_at: '2023-04-10T20:34:31.019647+00:00'
---

# Code Snippet cb81c10e

**Language**: Bash

```bash
gcc -fPIC -shared -static-libgcc -Wl,--version-script=version,-Bstatic exploit.c -o libc.so.6
```
