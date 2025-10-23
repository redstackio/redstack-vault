---
id: 59b2eaa0-a38f-412a-91a7-0d250b6bf906
name: active
type: command
executor: bash
data: 'lsof -nP -iTCP -sTCP:ESTABLISHED | grep HTTPS

  '
output: null
created_at: '2020-07-14T18:21:25.727452+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# active

```bash
lsof -nP -iTCP -sTCP:ESTABLISHED | grep HTTPS

```


