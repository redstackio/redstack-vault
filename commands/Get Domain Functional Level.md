---
id: 75fb9169-2d44-4681-a523-1111c31c08b5
name: Get Domain Functional Level
type: command
executor: bash
data: 'dsquery * "DC=corp,DC=test,DC=com" -scope base -attr msDS-Behavior-Version
  ntMixedDomain

  '
output: null
created_at: '2020-07-14T18:21:11.827893+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get Domain Functional Level

```bash
dsquery * "DC=corp,DC=test,DC=com" -scope base -attr msDS-Behavior-Version ntMixedDomain

```
