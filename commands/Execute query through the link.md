---
id: 6f6a8c08-abda-4d29-a50c-d7915a1b4c46
name: Execute query through the link
type: command
executor: bash
data: 'select * from openquery("dcorp-sql1", ''select * from master..sysservers'')

  select version from openquery("linkedserver", ''select @@version as version'');'
output: null
created_at: '2023-04-06T03:56:34.105254+00:00'
updated_at: '2023-04-10T20:22:42.442119+00:00'
---

# Execute query through the link

```bash
select * from openquery("dcorp-sql1", 'select * from master..sysservers')
select version from openquery("linkedserver", 'select @@version as version');
```


