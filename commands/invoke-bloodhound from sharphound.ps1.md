---
id: 64755c2d-2548-45f6-abd1-5a3b1f7cb8a8
name: invoke-bloodhound from sharphound.ps1
type: command
executor: bash
data: 'import-module .\sharphound.ps1

  invoke-bloodHound -CollectionMethod All -domain target-domain -LDAPUser username
  -LDAPPass password

  '
output: null
created_at: '2020-07-14T18:14:37.324143+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# invoke-bloodhound from sharphound.ps1

```bash
import-module .\sharphound.ps1
invoke-bloodHound -CollectionMethod All -domain target-domain -LDAPUser username -LDAPPass password

```


