---
id: 1925c8a0-cab3-4f84-ab8b-409f7936124e
name: Port Forwarding from local port to destination port
type: command
executor: bash
data: 'netsh interface portproxy add v4tov4 listenaddress=localaddress listenport=localport
  connectaddress=destaddress connectport=destport

  netsh interface portproxy add v4tov4 listenport=3340 listenaddress=10.1.1.110 connectport=3389
  connectaddress=10.1.1.110'
output: null
created_at: '2023-04-06T03:56:22.387663+00:00'
updated_at: '2023-04-10T20:25:17.186023+00:00'
---

# Port Forwarding from local port to destination port

```bash
netsh interface portproxy add v4tov4 listenaddress=localaddress listenport=localport connectaddress=destaddress connectport=destport
netsh interface portproxy add v4tov4 listenport=3340 listenaddress=10.1.1.110 connectport=3389 connectaddress=10.1.1.110
```
