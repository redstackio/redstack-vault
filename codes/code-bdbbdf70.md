---
id: bdbbdf70-c150-4955-856e-81aa5fb257ab
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:57.211905+00:00'
updated_at: '2023-04-06T03:55:57.223042+00:00'
---

# Code Snippet bdbbdf70

**Language**: Bash

```bash
swissky@crashlab:~$ echo ${HOME:0:1}
/

swissky@crashlab:~$ cat ${HOME:0:1}etc${HOME:0:1}passwd
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ echo . | tr '!-0' '"-1'
/

swissky@crashlab:~$ tr '!-0' '"-1' <<< .
/

swissky@crashlab:~$ cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
root:x:0:0:root:/root:/bin/bash
```
