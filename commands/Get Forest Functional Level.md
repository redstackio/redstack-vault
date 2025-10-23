---
id: ebc2d7e8-1fc2-4bef-b8f4-e4fb73d5c79c
name: Get Forest Functional Level
type: command
executor: bash
data: 'dsquery * "CN=Partitions,CN=Configuration,DC=corp,DC=test,DC=com" -scope base
  -attr msDS-Behavior-Version ntMixedDomain

  '
output: null
created_at: '2020-07-14T18:21:11.828082+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get Forest Functional Level

```bash
dsquery * "CN=Partitions,CN=Configuration,DC=corp,DC=test,DC=com" -scope base -attr msDS-Behavior-Version ntMixedDomain

```


