---
id: 4bbb0548-c6d2-4b97-b8e7-cccb3f8755dc
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:23:19.286944+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 4bbb0548

**Language**: Bash

```bash

echo public > community.txt
echo private >> community.txt
echo manager >> community.txt
for ip in $(seq 200 254); do echo 1.2.3.${ip}; done > target-ip.txt

```
