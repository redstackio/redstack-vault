---
id: de6124e3-1936-4947-9500-2c8ee164e0f2
name: Find Files and Folder with Regex (PowerShell)
type: command
executor: powershell
data: Get-ChildItem -Recurse | Where Name -Match "$_REGEX"
output: "PS C:\\Users > Get-ChildItem -Recurse | Where Name -Match \"^secret.*\"\n\
  \n\n    Directory: C:\\Users\\Bob\\Desktop\n\n\nMode                LastWriteTime\
  \         Length Name\n----                -------------         ------ ----\n-a----\
  \        4/24/2020  11:23 AM              0 secretdocument.txt"
created_at: '2020-04-24T18:25:00.592827+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find Files and Folder with Regex (PowerShell)

```powershell
Get-ChildItem -Recurse | Where Name -Match "$_REGEX"
```

## Expected Output

```
PS C:\Users > Get-ChildItem -Recurse | Where Name -Match "^secret.*"


    Directory: C:\Users\Bob\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/24/2020  11:23 AM              0 secretdocument.txt
```


