---
id: 464e2639-10ac-4499-a3e4-62c6c2d2535f
name: Get attributes for computers in a specific OU
type: command
executor: bash
data: 'dsquery computer <OU=PUT OU HERE> -limit 0 |dsget computer -dn -samid -desc
  -l >c:\windows\temp\out.log

  '
output: null
created_at: '2020-07-14T18:21:11.825893+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get attributes for computers in a specific OU

```bash
dsquery computer <OU=PUT OU HERE> -limit 0 |dsget computer -dn -samid -desc -l >c:\windows\temp\out.log

```
