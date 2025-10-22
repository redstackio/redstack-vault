---
id: 8d0aed7f-05cb-4c5e-b148-fba69b613a2f
name: cross compile for 32bit windows (on 32bit linux)
type: command
executor: bash
data: 'apt-get install mingw32

  i586-mingw32msvc-gcc <source>.c -o <outfile> -lws2_32

  '
output: null
created_at: '2020-07-14T18:14:39.841593+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# cross compile for 32bit windows (on 32bit linux)

```bash
apt-get install mingw32
i586-mingw32msvc-gcc <source>.c -o <outfile> -lws2_32

```
