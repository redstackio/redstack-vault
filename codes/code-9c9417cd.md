---
id: 9c9417cd-0739-4bf2-be01-382ae454a66b
type: code
language: Bash
verified: false
created_at: '2020-04-03T09:06:24.730755+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9c9417cd

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
