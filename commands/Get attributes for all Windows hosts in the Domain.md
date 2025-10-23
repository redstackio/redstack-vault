---
id: 2897dfbc-ea1f-4b24-a363-255e0acc7f55
name: Get attributes for all Windows hosts in the Domain
type: command
executor: bash
data: 'dsquery * -filter "(&(objectclass=computer) (objectcategory=computer) (operatingSystem=Windows*))"
  -limit 0 |dsget computer -dn -samid -desc -loc >c:\windows\temp\computers.log

  '
output: null
created_at: '2020-07-14T18:21:11.826343+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get attributes for all Windows hosts in the Domain

```bash
dsquery * -filter "(&(objectclass=computer) (objectcategory=computer) (operatingSystem=Windows*))" -limit 0 |dsget computer -dn -samid -desc -loc >c:\windows\temp\computers.log

```


