---
id: 81b3dccf-aabc-4476-a093-49f13ad90785
name: Print Human Readable Strings in a File
type: command
executor: bash
data: strings $_FILE
output: 'root@a7ffb5e7e757:/# strings /bin/ls

  /lib64/ld-linux-x86-64.so.2

  libselinux.so.1

  _ITM_deregisterTMCloneTable

  __gmon_start__

  _ITM_registerTMCloneTable

  fgetfilecon

  freecon

  lgetfilecon

  libc.so.6

  fflush

  strcpy

  gmtime_r

  __printf_chk

  ...'
created_at: '2020-03-10T04:32:47.071481+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Print Human Readable Strings in a File

```bash
strings $_FILE
```

## Expected Output

```
root@a7ffb5e7e757:/# strings /bin/ls
/lib64/ld-linux-x86-64.so.2
libselinux.so.1
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
fgetfilecon
freecon
lgetfilecon
libc.so.6
fflush
strcpy
gmtime_r
__printf_chk
...
```


