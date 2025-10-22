---
id: bba3da79-0d80-4019-8994-f927cc6bc949
name: Retrieve table contents
type: command
executor: bash
data: 'sqlcmd -E -S localhost -d DatabaseName -Q "SELECT * FROM SystemUserBase;" -W
  -w 999 -s"," -o "c:\windows\temp\RecruiterProd_MSCRM_userbase.csv"

  '
output: null
created_at: '2020-07-14T18:21:00.906447+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Retrieve table contents

```bash
sqlcmd -E -S localhost -d DatabaseName -Q "SELECT * FROM SystemUserBase;" -W -w 999 -s"," -o "c:\windows\temp\RecruiterProd_MSCRM_userbase.csv"

```
