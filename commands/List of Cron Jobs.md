---
id: 49a5669e-3180-4317-9162-d275a2ab4f9d
name: List of Cron Jobs
type: command
executor: bash
data: 'ls -alh /var/spool/cron;

  ls -al /etc/ | grep cron

  ls -al /etc/cron*'
output: null
created_at: '2023-04-06T03:56:18.734154+00:00'
updated_at: '2023-04-10T20:34:25.067486+00:00'
---

# List of Cron Jobs

```bash
ls -alh /var/spool/cron;
ls -al /etc/ | grep cron
ls -al /etc/cron*
```


