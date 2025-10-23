---
id: d3675e75-af8f-410f-ab30-9d06df8aa09d
name: Find computers with Unconstrained Delegation
type: command
executor: bash
data: "Get-NetComputer -Unconstrained | select samaccountname \n"
output: null
created_at: '2020-07-15T19:06:26.864320+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find computers with Unconstrained Delegation

```bash
Get-NetComputer -Unconstrained | select samaccountname 

```


