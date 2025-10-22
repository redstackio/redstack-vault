---
id: 12f4f1d3-aabd-4379-850a-3501eaf9a5fd
name: List Tables in Database
type: command
executor: bash
data: 'sqlcmd -E -S localhost -Q "SELECT * FROM DatabaseName.information_schema.tables;"
  -W -w 999 -s"," -o "c:\windows\temp\RecruiterProd_MSCRM_tables.csv"

  '
output: null
created_at: '2020-07-14T18:21:00.906085+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Tables in Database

```bash
sqlcmd -E -S localhost -Q "SELECT * FROM DatabaseName.information_schema.tables;" -W -w 999 -s"," -o "c:\windows\temp\RecruiterProd_MSCRM_tables.csv"

```
