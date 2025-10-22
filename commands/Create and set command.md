---
id: 303ac77d-c16b-4178-b48c-1fe161e848cb
name: Create and set command
type: command
executor: bash
data: 'echo ''#!/bin/sh'' > /cmd

  echo "ps aux > $host_path/output" >> /cmd

  chmod a+x /cmd'
output: null
created_at: '2023-04-06T03:56:17.110299+00:00'
updated_at: '2023-04-10T20:33:50.379078+00:00'
---

# Create and set command

```bash
echo '#!/bin/sh' > /cmd
echo "ps aux > $host_path/output" >> /cmd
chmod a+x /cmd
```
