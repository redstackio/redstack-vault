---
id: af9396ab-b779-4580-8385-f2478cc2b17f
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:14:43.329087+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet af9396ab

**Language**: Bash

```bash

echo public > community.txt
echo private >> community.txt
echo manager >> community.txt
for ip in $(seq 200 254); do echo 1.2.3.${ip}; done > target-ip.txt

```
