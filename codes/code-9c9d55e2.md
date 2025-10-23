---
id: 9c9d55e2-bd3f-42ae-8a29-ac92d6b03ab7
type: code
language: Bash
verified: false
created_at: '2019-09-17T06:34:44.762924+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9c9d55e2

**Language**: Bash

```bash
#!/bin/bash

IFS=$'\n'

old_process=$(ps -eo command)

while true; do
    new_process=$(ps -eo command)
    diff <(echo "$old_process") <(echo "$new_process") | grep [\<\>]
    sleep 1
    old_process=$new_process
done
```


