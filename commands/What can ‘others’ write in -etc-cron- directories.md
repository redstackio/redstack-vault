---
id: 568195b3-d4dc-46f5-a3d9-bd398d2730ad
name: What can ‘others’ write in /etc/cron* directories
type: command
executor: bash
data: 'ls -aRl /etc/cron* | awk ''$1 ~ /w.$/'' 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:44.249442+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# What can ‘others’ write in /etc/cron* directories

```bash
ls -aRl /etc/cron* | awk '$1 ~ /w.$/' 2>/dev/null

```


