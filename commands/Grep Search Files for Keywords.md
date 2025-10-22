---
id: 0db9e66b-66a6-404a-9eb0-ab25b367fb03
name: Grep Search Files for Keywords
type: command
executor: bash
data: grep -C 5 -iR '$_WORD1\|$_WORD2' *
output: 'root@kali:~# grep -C 5 -iR ''password\|secret'' *

  images/.hidden.txt-The password is hunter2. Don''t tell anyone!

  '
created_at: '2019-10-09T18:38:08.439612+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Grep Search Files for Keywords

```bash
grep -C 5 -iR '$_WORD1\|$_WORD2' *
```

## Expected Output

```
root@kali:~# grep -C 5 -iR 'password\|secret' *
images/.hidden.txt-The password is hunter2. Don't tell anyone!

```
