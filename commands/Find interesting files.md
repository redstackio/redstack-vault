---
id: d0281e4b-93dc-421e-8e3c-5922efc46d86
name: Find interesting files
type: command
executor: bash
data: 'powershell Invoke-FileFinder -ComputerName -share share_list.txt -terms ssn,pass,sensitive,secret,admin,login,unattend*.xml,web.config,account
  -Threads 20 | export-csv filefinder_shares.csv

  '
output: null
created_at: '2020-07-14T18:21:07.165739+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find interesting files

```bash
powershell Invoke-FileFinder -ComputerName -share share_list.txt -terms ssn,pass,sensitive,secret,admin,login,unattend*.xml,web.config,account -Threads 20 | export-csv filefinder_shares.csv

```


