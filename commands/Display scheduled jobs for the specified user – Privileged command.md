---
id: 881f9889-ad6f-45b7-a474-4c933424e72f
name: Display scheduled jobs for the specified user – Privileged command
type: command
executor: bash
data: 'crontab -l -u %username%

  '
output: null
created_at: '2020-07-14T18:14:44.248691+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Display scheduled jobs for the specified user – Privileged command

```bash
crontab -l -u %username%

```
