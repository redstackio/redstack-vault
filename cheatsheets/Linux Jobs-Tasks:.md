---
id: 477fe8bd-4844-4ab2-b854-2d974ce1f9d2
name: 'Linux Jobs/Tasks:'
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:45.142165+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Linux Jobs/Tasks:

**Command** ([[Display scheduled jobs for the specified user – Privileged command]]):

```bash
crontab -l -u %username%

```

**Command** ([[Scheduled jobs overview (hourly, daily, monthly etc)]]):

```bash
ls -la /etc/cron*

```

**Command** ([[What can ‘others’ write in /etc/cron* directories]]):

```bash
ls -aRl /etc/cron* | awk '$1 ~ /w.$/' 2>/dev/null

```

**Command** ([[List of current tasks]]):

```bash
top

```
