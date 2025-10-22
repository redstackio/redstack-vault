---
id: 96c9aff1-5760-47bb-adf6-0814ae1aa7e7
name: Enable xp_cmdshell
type: command
executor: bash
data: 'EXEC sp_configure ''show advanced options'',1;

  RECONFIGURE;

  EXEC sp_configure ''xp_cmdshell'',1;

  RECONFIGURE;'
output: null
created_at: '2023-04-06T03:56:33.953275+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
---

# Enable xp_cmdshell

```bash
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```
