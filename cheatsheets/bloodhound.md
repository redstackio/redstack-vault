---
id: 74523919-4be0-4459-b7c1-a952d804ce55
name: bloodhound
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:37.342182+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# bloodhound

**Command** ([[invoke-bloodhound from sharphound.ps1]]):

```bash
import-module .\sharphound.ps1
invoke-bloodHound -CollectionMethod All -domain target-domain -LDAPUser username -LDAPPass password

```
