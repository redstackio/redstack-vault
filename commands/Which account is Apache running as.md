---
id: 888a6881-f58c-4076-a5a2-1b16da67f04a
name: Which account is Apache running as
type: command
executor: bash
data: 'cat /etc/apache2/envvars 2>/dev/null |grep -i ''user\|group'' |awk ''{sub(/.*\export
  /,"")}1''

  '
output: null
created_at: '2020-07-14T18:14:29.248567+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Which account is Apache running as

```bash
cat /etc/apache2/envvars 2>/dev/null |grep -i 'user\|group' |awk '{sub(/.*\export /,"")}1'

```
