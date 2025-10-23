---
id: f02faa43-7411-4cd0-8925-b3a1fa941926
name: List available compilers
type: command
executor: bash
data: 'dpkg --list 2>/dev/null| grep compiler |grep -v decompiler 2>/dev/null && yum
  list installed ''gcc*'' 2>/dev/null| grep gcc 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:29.247962+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List available compilers

```bash
dpkg --list 2>/dev/null| grep compiler |grep -v decompiler 2>/dev/null && yum list installed 'gcc*' 2>/dev/null| grep gcc 2>/dev/null

```


