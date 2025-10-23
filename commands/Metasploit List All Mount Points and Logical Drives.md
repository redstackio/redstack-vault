---
id: ea9233b9-fc75-4333-bee6-7c4e1f1b7787
name: Metasploit List All Mount Points and Logical Drives
type: command
executor: metasploit
data: show_mount
output: "meterpreter > show_mount\n\nMounts / Drives\n===============\n\nName  Type\
  \   Size (Total)  Size (Free)  Mapped to\n----  ----   ------------  -----------\
  \  ---------\nC:\\   fixed  31.90 GiB     8.61 GiB     \nD:\\   cdrom  0.00 B  \
  \      0.00 B       \n\n\nTotal mounts/drives: 2"
created_at: '2020-07-09T00:22:14.476070+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit List All Mount Points and Logical Drives

```metasploit
show_mount
```

## Expected Output

```
meterpreter > show_mount

Mounts / Drives
===============

Name  Type   Size (Total)  Size (Free)  Mapped to
----  ----   ------------  -----------  ---------
C:\   fixed  31.90 GiB     8.61 GiB     
D:\   cdrom  0.00 B        0.00 B       


Total mounts/drives: 2
```


