---
id: aeb6c4dd-5612-4895-9ce3-5a9b1dc40c94
name: Cron User Access Files
type: command
executor: bash
data: 'cat /etc/at.allow

  cat /etc/at.deny

  cat /etc/cron.allow

  cat /etc/cron.deny*'
output: null
created_at: '2023-04-06T03:56:18.734308+00:00'
updated_at: '2023-04-10T20:34:25.067486+00:00'
---

# Cron User Access Files

```bash
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny*
```
