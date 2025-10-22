---
id: 6544b7e5-8508-4023-83b1-c7f4fec65207
name: cross compile for 32Bit windows (on 64bit linux)
type: command
executor: bash
data: 'i686-w64-mingw32-gcc -o ms11-046.exe ms11-046.c -lws2_32

  '
output: null
created_at: '2020-07-14T18:14:39.841230+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# cross compile for 32Bit windows (on 64bit linux)

```bash
i686-w64-mingw32-gcc -o ms11-046.exe ms11-046.c -lws2_32

```
