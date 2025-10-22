---
id: e97f30dd-9a95-49dc-810b-a81a99e802fc
name: Find computers with Constrined Delegation
type: command
executor: bash
data: "Get-NetComputer -TrustedToAuth | select samaccountname \n"
output: null
created_at: '2020-07-15T19:06:26.863179+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find computers with Constrined Delegation

```bash
Get-NetComputer -TrustedToAuth | select samaccountname 

```
