---
id: bf3b231d-b978-4b07-9a09-5be346b0b885
name: find Search for Writable Files by User
type: command
executor: ''
data: find $_DIRECTORY -user $_USER -writable ! -type l 2>/dev/null
output: 'root@hackers:~# find /etc/cron.daily -user root -writable ! -type l 2>/dev/null

  /etc/cron.daily

  /etc/cron.daily/sysstat

  /etc/cron.daily/bsdmainutils

  /etc/cron.daily/0day.conf

  /etc/cron.daily/dpkg

  /etc/cron.daily/man-db

  /etc/cron.daily/samba

  /etc/cron.daily/mlocate

  /etc/cron.daily/debtags

  /etc/cron.daily/apache2

  /etc/cron.daily/logrotate

  /etc/cron.daily/SuperHackerScript.conf

  /etc/cron.daily/cracklib-runtime

  /etc/cron.daily/ntp

  /etc/cron.daily/.placeholder

  /etc/cron.daily/chkrootkit

  /etc/cron.daily/exim4-base

  /etc/cron.daily/apt-compat

  /etc/cron.daily/passwd'
created_at: '2019-09-17T06:24:10.219337+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# find Search for Writable Files by User

```bash
find $_DIRECTORY -user $_USER -writable ! -type l 2>/dev/null
```

## Expected Output

```
root@hackers:~# find /etc/cron.daily -user root -writable ! -type l 2>/dev/null
/etc/cron.daily
/etc/cron.daily/sysstat
/etc/cron.daily/bsdmainutils
/etc/cron.daily/0day.conf
/etc/cron.daily/dpkg
/etc/cron.daily/man-db
/etc/cron.daily/samba
/etc/cron.daily/mlocate
/etc/cron.daily/debtags
/etc/cron.daily/apache2
/etc/cron.daily/logrotate
/etc/cron.daily/SuperHackerScript.conf
/etc/cron.daily/cracklib-runtime
/etc/cron.daily/ntp
/etc/cron.daily/.placeholder
/etc/cron.daily/chkrootkit
/etc/cron.daily/exim4-base
/etc/cron.daily/apt-compat
/etc/cron.daily/passwd
```


