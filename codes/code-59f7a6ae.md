---
id: 59f7a6ae-7fd2-40ef-ae42-bfc0425b0654
type: code
language: Bash
verified: false
created_at: '2019-10-31T21:16:30.121798+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 59f7a6ae

**Language**: Bash

```bash
for FILE in $(find /home /root -name '.bash_history' 2>/dev/null); do shred -z $FILE; cat /dev/null > $FILE; done
```
