---
id: 556743f4-5498-40f1-8c05-63ec2bd7e2a1
name: "\tList .log files in specified directory (/var/log)"
type: command
executor: bash
data: 'find /var/log -name *.log -type f -exec ls -la {} \; 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:41.288246+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# 	List .log files in specified directory (/var/log)

```bash
find /var/log -name *.log -type f -exec ls -la {} \; 2>/dev/null

```
