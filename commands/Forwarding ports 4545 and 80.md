---
id: b531622f-c9be-4323-89e3-f3a89bb119e8
name: Forwarding ports 4545 and 80
type: command
executor: bash
data: 'netsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44
  connectport=4545

  netsh interface portproxy add v4tov4 listenport=80 connectaddress=192.168.50.44
  connectport=80'
output: null
created_at: '2023-04-06T03:56:22.387690+00:00'
updated_at: '2023-04-10T20:25:17.186023+00:00'
---

# Forwarding ports 4545 and 80

```bash
netsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44 connectport=4545
netsh interface portproxy add v4tov4 listenport=80 connectaddress=192.168.50.44 connectport=80
```
