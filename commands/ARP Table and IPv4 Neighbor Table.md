---
id: ce50a024-24af-42fc-b258-56e9b06c8f37
name: ARP Table and IPv4 Neighbor Table
type: command
executor: bash
data: 'arp -A

  Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State'
output: null
created_at: '2023-04-06T03:56:28.696292+00:00'
updated_at: '2023-04-10T20:37:53.209844+00:00'
---

# ARP Table and IPv4 Neighbor Table

```bash
arp -A
Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State
```


