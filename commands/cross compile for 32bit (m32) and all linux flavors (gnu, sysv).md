---
id: abfb24a7-6dae-49bd-b2f9-2696334b6363
name: cross compile for 32bit (m32) and all linux flavors (gnu, sysv)
type: command
executor: bash
data: 'apt-get install libc6-dev-i386

  gcc -m32 -Wall -Wl,--hash-style=both 9545.c -o exploit

  '
output: null
created_at: '2020-07-14T18:14:39.841110+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# cross compile for 32bit (m32) and all linux flavors (gnu, sysv)

```bash
apt-get install libc6-dev-i386
gcc -m32 -Wall -Wl,--hash-style=both 9545.c -o exploit

```
