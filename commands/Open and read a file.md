---
id: b5ae3201-3694-40b6-8fc3-06b6ce876382
name: Open and read a file
type: command
executor: bash
data: EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(open("C:\\inetpub\\wwwroot\\web.config",
  "r").read())'
output: null
created_at: '2023-04-06T03:56:33.953785+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
---

# Open and read a file

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(open("C:\\inetpub\\wwwroot\\web.config", "r").read())'
```


