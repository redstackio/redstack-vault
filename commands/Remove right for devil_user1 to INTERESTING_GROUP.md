---
id: 9b17708c-ea9f-4c18-8c0a-827fe6746b84
name: Remove right for devil_user1 to INTERESTING_GROUP
type: command
executor: bash
data: bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll
  devil_user1 cn=INTERESTING_GROUP,dc=corp False
output: null
created_at: '2023-04-06T03:56:06.850730+00:00'
updated_at: '2023-04-10T20:36:10.633986+00:00'
---

# Remove right for devil_user1 to INTERESTING_GROUP

```bash
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll devil_user1 cn=INTERESTING_GROUP,dc=corp False
```


