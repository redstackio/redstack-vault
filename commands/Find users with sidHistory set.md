---
id: 8f555455-d1e7-4bbc-bbf0-8211c0c1ac1e
name: Find users with sidHistory set
type: command
executor: bash
data: "Get-NetUser -LDAPFilter '(sidHistory=*)' \n"
output: null
created_at: '2020-07-15T19:06:26.862716+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find users with sidHistory set

```bash
Get-NetUser -LDAPFilter '(sidHistory=*)' 

```


