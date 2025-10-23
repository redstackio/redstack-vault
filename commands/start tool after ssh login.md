---
id: 2e17c147-c691-413a-9ed4-756722312c63
name: start tool after ssh login
type: command
executor: bash
data: 'ssh username@target-ip -o "ProxyCommand=ncat --proxy-type http --proxy target-ip:proxy-port
  127.0.0.1 22"

  '
output: null
created_at: '2020-07-14T18:14:34.726596+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# start tool after ssh login

```bash
ssh username@target-ip -o "ProxyCommand=ncat --proxy-type http --proxy target-ip:proxy-port 127.0.0.1 22"

```


