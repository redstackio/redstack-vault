---
id: 83d25991-ed83-4754-8b83-67aa930a322d
name: Get list of DCs
type: command
executor: bash
data: 'nslookup -type=srv _ldap._tcp.dc._msdcs.corp.test.com

  '
output: null
created_at: '2020-07-14T18:21:27.743275+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get list of DCs

```bash
nslookup -type=srv _ldap._tcp.dc._msdcs.corp.test.com

```
