---
id: 6852732b-4451-4cf2-a4fa-3382a366c6e1
name: find Search for Files with Wildcards
type: command
executor: ''
data: find $_DIRECTORY -iname "*$_WORD*" -ls 2>/dev/null
output: 'root@hackers:~# find /etc/cron.daily -iname "*conf*" -ls 2>/dev/null

  -rw-r--r-- 1 root root 0 Sep 16 22:54 /etc/cron.daily/0day.conf

  -rw-r--r-- 1 root root 0 Sep 16 22:54 /etc/cron.daily/SuperHackerScript.conf'
created_at: '2019-09-17T06:24:10.194637+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# find Search for Files with Wildcards

```bash
find $_DIRECTORY -iname "*$_WORD*" -ls 2>/dev/null
```

## Expected Output

```
root@hackers:~# find /etc/cron.daily -iname "*conf*" -ls 2>/dev/null
-rw-r--r-- 1 root root 0 Sep 16 22:54 /etc/cron.daily/0day.conf
-rw-r--r-- 1 root root 0 Sep 16 22:54 /etc/cron.daily/SuperHackerScript.conf
```


