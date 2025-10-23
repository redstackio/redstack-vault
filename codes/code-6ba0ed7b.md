---
id: 6ba0ed7b-6fe5-4800-890e-ceaa39ecd762
type: code
language: Bash
verified: false
created_at: '2020-03-23T01:27:24.693829+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 6ba0ed7b

**Language**: Bash

```bash
for FILE in $(find /home /root -name '.bash_history' 2>/dev/null); do shred -z $FILE; cat /dev/null > $FILE; done
```


