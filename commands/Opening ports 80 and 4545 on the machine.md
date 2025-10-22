---
id: d9ef9b85-6a0e-48fe-9aa2-efc75c873318
name: Opening ports 80 and 4545 on the machine
type: command
executor: bash
data: 'netsh advfirewall firewall add rule name="PortForwarding 80" dir=in action=allow
  protocol=TCP localport=80

  netsh advfirewall firewall add rule name="PortForwarding 80" dir=out action=allow
  protocol=TCP localport=80

  netsh advfirewall firewall add rule name="PortForwarding 4545" dir=in action=allow
  protocol=TCP localport=4545

  netsh advfirewall firewall add rule name="PortForwarding 4545" dir=out action=allow
  protocol=TCP localport=4545'
output: null
created_at: '2023-04-06T03:56:22.387762+00:00'
updated_at: '2023-04-10T20:25:17.186023+00:00'
---

# Opening ports 80 and 4545 on the machine

```bash
netsh advfirewall firewall add rule name="PortForwarding 80" dir=in action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="PortForwarding 80" dir=out action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=in action=allow protocol=TCP localport=4545
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=out action=allow protocol=TCP localport=4545
```
