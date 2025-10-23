---
id: 3eb1d655-8ee4-40a8-ad34-9cf23a622f9f
name: Execute as sa and check if user is sysadmin
type: command
executor: bash
data: 'EXECUTE AS LOGIN = ''sa''

  SELECT IS_SRVROLEMEMBER(''sysadmin'')'
output: null
created_at: '2023-04-06T03:56:21.083530+00:00'
updated_at: '2023-04-10T20:36:46.097015+00:00'
---

# Execute as sa and check if user is sysadmin

```bash
EXECUTE AS LOGIN = 'sa'
SELECT IS_SRVROLEMEMBER('sysadmin')
```


