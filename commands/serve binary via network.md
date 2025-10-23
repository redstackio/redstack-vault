---
id: e1df075d-46de-4d4f-9455-fe076cf028b0
name: serve binary via network
type: command
executor: bash
data: 'socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./binary"

  '
output: null
created_at: '2020-07-14T18:15:02.617321+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# serve binary via network

```bash
socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./binary"

```


