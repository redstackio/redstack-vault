---
id: 0fb2dc38-282d-4ed9-9cda-37f4cb53f742
name: UDP Port Redirection
type: command
executor: bash
data: 'socat udp4-recvfrom:53,reuseaddr,fork udp4-sendto:; echo -ne

  '
output: null
created_at: '2020-07-14T18:21:06.518348+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# UDP Port Redirection

```bash
socat udp4-recvfrom:53,reuseaddr,fork udp4-sendto:; echo -ne

```
