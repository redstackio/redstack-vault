---
id: 3144e85e-ef22-4eb5-9c84-9ccc0458741b
name: Execute query through linked server
type: command
executor: bash
data: 'SELECT * FROM OPENQUERY("dcorp-sql1", ''SELECT * FROM master..sysservers'')

  SELECT version FROM OPENQUERY("linkedserver", ''SELECT @@version AS version'');

  -- Chain multiple openquery

  SELECT version FROM OPENQUERY("link1",''SELECT version FROM OPENQUERY("link2","SELECT
  @@version AS version")'')'
output: null
created_at: '2023-04-06T03:56:20.034603+00:00'
updated_at: '2023-04-10T20:36:34.685235+00:00'
---

# Execute query through linked server

```bash
SELECT * FROM OPENQUERY("dcorp-sql1", 'SELECT * FROM master..sysservers')
SELECT version FROM OPENQUERY("linkedserver", 'SELECT @@version AS version');

-- Chain multiple openquery
SELECT version FROM OPENQUERY("link1",'SELECT version FROM OPENQUERY("link2","SELECT @@version AS version")')
```
