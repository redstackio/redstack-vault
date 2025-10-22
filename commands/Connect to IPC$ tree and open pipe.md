---
id: d1823cfe-94a3-4175-bc29-1e5bd7c95bdb
name: Connect to IPC$ tree and open pipe
type: command
executor: bash
data: 'tid = s.connectTree(''IPC$'')

  fid_main = self.openPipe(s,tid,r''\\RemCom_communicaton'',0x12019f)'
output: null
created_at: '2023-04-06T03:56:30.905514+00:00'
updated_at: '2023-04-10T20:37:58.731576+00:00'
---

# Connect to IPC$ tree and open pipe

```bash
tid = s.connectTree('IPC$')
fid_main = self.openPipe(s,tid,r'\\RemCom_communicaton',0x12019f)
```
