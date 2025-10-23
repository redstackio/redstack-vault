---
id: de26440e-00e0-4bc8-b50a-31082fdbfb49
name: Get details of all domain computers and export to a CSV file for easy viewing
type: command
executor: bash
data: 'Get-computerproperty -Domain -properties displayname,adspath,lastlogontimestamp,operatingsystem,operatingsystemversion,@{Name=''memberof'';Expression={[string]::join(";",($_.memberof))}}|export-csv
  computerprops.csv

  '
output: null
created_at: '2020-07-14T18:21:07.166481+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get details of all domain computers and export to a CSV file for easy viewing

```bash
Get-computerproperty -Domain -properties displayname,adspath,lastlogontimestamp,operatingsystem,operatingsystemversion,@{Name='memberof';Expression={[string]::join(";",($_.memberof))}}|export-csv computerprops.csv

```


