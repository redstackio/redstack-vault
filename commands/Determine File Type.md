---
id: 1908ddc7-a7de-4ce7-9f34-d0189ff055a1
name: Determine File Type
type: command
executor: bash
data: file $_FILE
output: 'root@00b5b1279bcc:~# file /bin/ls

  /bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked,
  interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=a65f86cd6394e8f583c14d786d13b3bcbe051b87,
  stripped'
created_at: '2020-03-10T03:42:55.679470+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Determine File Type

```bash
file $_FILE
```

## Expected Output

```
root@00b5b1279bcc:~# file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=a65f86cd6394e8f583c14d786d13b3bcbe051b87, stripped
```


