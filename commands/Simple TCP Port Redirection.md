---
id: 67ba75cb-11b4-4225-8df3-feb4194630eb
name: Simple TCP Port Redirection
type: command
executor: bash
data: 'socat TCP-LISTEN:80,fork TCP::80

  '
output: null
created_at: '2020-07-14T18:21:06.518195+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Simple TCP Port Redirection

```bash
socat TCP-LISTEN:80,fork TCP::80

```
