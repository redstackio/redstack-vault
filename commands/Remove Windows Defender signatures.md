---
id: b6da71a5-13a1-48d0-bbaa-34908d796aa9
name: Remove Windows Defender signatures
type: command
executor: bash
data: '& "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe"
  -RemoveDefinitions -All

  & "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All'
output: null
created_at: '2023-04-06T03:56:26.616644+00:00'
updated_at: '2023-04-10T20:37:03.357263+00:00'
---

# Remove Windows Defender signatures

```bash
& "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" -RemoveDefinitions -All
& "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```
