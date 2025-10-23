---
id: 7fed233d-a9b0-453e-a551-20d4db7ee9a5
name: Setup TCP listener
type: command
executor: bash
data: sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:192.168.83.131:9998 &
output: null
created_at: '2023-04-06T03:56:05.609174+00:00'
updated_at: '2023-04-10T20:26:29.616322+00:00'
---

# Setup TCP listener

```bash
sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:192.168.83.131:9998 &
```


