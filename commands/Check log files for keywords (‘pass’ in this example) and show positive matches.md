---
id: 641fd715-7787-47f4-a8aa-fa9707392d9a
name: Check log files for keywords (‘pass’ in this example) and show positive matches
type: command
executor: bash
data: 'grep -l -i pass /var/log/*.log 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:41.287846+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Check log files for keywords (‘pass’ in this example) and show positive matches

```bash
grep -l -i pass /var/log/*.log 2>/dev/null

```


