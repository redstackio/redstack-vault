---
id: cf294a26-84f2-4131-a71e-48c8d10fddd4
name: View domain groups
type: command
executor: bash
data: 'net group /domain

  powershell (new-object system.directoryservices.directorysearcher("(&(objectcategory=user)(samaccountname=$($env:username)))")).FindOne().GetDirectoryEntry().memberof

  '
output: null
created_at: '2020-07-14T18:21:27.745198+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# View domain groups

```bash
net group /domain
powershell (new-object system.directoryservices.directorysearcher("(&(objectcategory=user)(samaccountname=$($env:username)))")).FindOne().GetDirectoryEntry().memberof

```


