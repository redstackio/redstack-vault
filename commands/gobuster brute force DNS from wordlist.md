---
id: f599844a-2b32-4d4a-9d00-abf2a45820b1
name: gobuster brute force DNS from wordlist
type: command
executor: bash
data: 'gobuster dns -d $TARGET_DOMAIN -w $WORDLIST

  '
output: null
created_at: '2020-07-24T17:11:23.972351+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# gobuster brute force DNS from wordlist

```bash
gobuster dns -d $TARGET_DOMAIN -w $WORDLIST

```
