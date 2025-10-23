---
id: af42c17e-2721-43bc-8be3-089e58860b14
name: Search for Files Modified Within 60 Minutes
type: command
executor: bash
data: find / -ctime -60
output: 'root@hackers:~/Content/Enumeration# find /etc -ctime -1

  /etc

  /etc/emacs/site-start.d

  /etc/emacs/site-start.d/50autoconf.el

  /etc/alternatives

  /etc/alternatives/automake

  /etc/alternatives/aclocal

  /etc/alternatives/automake.1.gz

  /etc/alternatives/aclocal.1.gz

  /etc/cron.daily

  /etc/cron.daily/0day.conf

  /etc/cron.daily/SuperHackerScript.conf

  /etc/OpenCL/vendors

  /etc/OpenCL/vendors/pocl.icd

  /etc/resolv.conf

  /etc/ld.so.cache'
created_at: '2019-09-17T06:24:10.225354+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Search for Files Modified Within 60 Minutes

```bash
find / -ctime -60
```

## Expected Output

```
root@hackers:~/Content/Enumeration# find /etc -ctime -1
/etc
/etc/emacs/site-start.d
/etc/emacs/site-start.d/50autoconf.el
/etc/alternatives
/etc/alternatives/automake
/etc/alternatives/aclocal
/etc/alternatives/automake.1.gz
/etc/alternatives/aclocal.1.gz
/etc/cron.daily
/etc/cron.daily/0day.conf
/etc/cron.daily/SuperHackerScript.conf
/etc/OpenCL/vendors
/etc/OpenCL/vendors/pocl.icd
/etc/resolv.conf
/etc/ld.so.cache
```


