---
id: bfe3b546-284d-4a78-8e40-419f6bedc7c8
name: by port
type: command
executor: bash
data: 'lsof -i TCP:8443

  lsof -i TCP:10-1024

  '
output: null
created_at: '2020-07-14T18:21:25.726004+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# by port

```bash
lsof -i TCP:8443
lsof -i TCP:10-1024

```
