---
id: 12a1647e-62a4-43af-aaa5-7f14db280216
name: Execute remote command
type: command
executor: bash
data: python3 ./psexec.py domain/user:password@remote-hostname 'cmd.exe /c whoami'
output: null
created_at: '2023-04-06T03:56:30.784576+00:00'
updated_at: '2023-04-10T20:38:06.599941+00:00'
---

# Execute remote command

```bash
python3 ./psexec.py domain/user:password@remote-hostname 'cmd.exe /c whoami'
```
