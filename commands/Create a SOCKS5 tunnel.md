---
id: e1683693-f1ed-44a6-8c04-13379677a602
name: Create a SOCKS5 tunnel
type: command
executor: bash
data: ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@IP_VPS
output: null
created_at: '2023-04-06T03:56:22.549983+00:00'
updated_at: '2023-04-10T20:25:14.782686+00:00'
---

# Create a SOCKS5 tunnel

```bash
ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@IP_VPS
```


