---
id: affb50dd-d0ed-48e9-aa0f-b99fd8af3e2b
name: Get Firewall Rules
type: command
executor: bash
data: $f=New-object -comObject HNetCfg.FwPolicy2;$f.rules |  where {$_.action -eq
  "0"} | select name,applicationname,localports
output: null
created_at: '2023-04-06T03:56:26.713024+00:00'
updated_at: '2023-04-10T20:37:05.992696+00:00'
---

# Get Firewall Rules

```bash
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules |  where {$_.action -eq "0"} | select name,applicationname,localports
```
