---
id: 0b037093-4eb1-44bb-bee5-72362cc00c5a
name: Lateral Movement DCOM
type: command
executor: bash
data: "-t, --target=VALUE         Target Machine\n-b, --binary=VALUE         Binary:\
  \ powershell.exe\n-a, --args=VALUE           Arguments: -enc <blah>\n-m, --method=VALUE\
  \         Methods: MMC20Application, ShellWindows,\n                           \
  \ ShellBrowserWindow, ExcelDDE, VisioAddonEx,\n                            OutlookShellEx,\
  \ ExcelXLL, VisioExecLine, \n                            OfficeMacro\n-r, --reg,\
  \ --registry      Enable registry manipulation\n-h, -?, --help             Show\
  \ Help\n\nCurrent Methods: MMC20.Application, ShellWindows, ShellBrowserWindow,\
  \ ExcelDDE, VisioAddonEx, OutlookShellEx, ExcelXLL, VisioExecLine, OfficeMacro."
output: null
created_at: '2023-04-06T03:56:07.043362+00:00'
updated_at: '2023-04-10T20:26:18.160002+00:00'
---

# Lateral Movement DCOM

```bash
-t, --target=VALUE         Target Machine
-b, --binary=VALUE         Binary: powershell.exe
-a, --args=VALUE           Arguments: -enc <blah>
-m, --method=VALUE         Methods: MMC20Application, ShellWindows,
                            ShellBrowserWindow, ExcelDDE, VisioAddonEx,
                            OutlookShellEx, ExcelXLL, VisioExecLine, 
                            OfficeMacro
-r, --reg, --registry      Enable registry manipulation
-h, -?, --help             Show Help

Current Methods: MMC20.Application, ShellWindows, ShellBrowserWindow, ExcelDDE, VisioAddonEx, OutlookShellEx, ExcelXLL, VisioExecLine, OfficeMacro.
```


