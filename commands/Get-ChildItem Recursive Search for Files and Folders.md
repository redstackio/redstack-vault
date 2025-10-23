---
id: c540eb58-6413-4d52-83e1-e2a493d83a18
name: Get-ChildItem Recursive Search for Files and Folders
type: command
executor: powershell
data: Get-ChildItem -Recurse -Filter "$_FILENAME"
output: "PS C:\\Users> Get-ChildItem -Recurse -Filter \"secrets.txt\"\n\n\n    Directory:\
  \ C:\\Users\\Bob\\Desktop\n\n\nMode                LastWriteTime         Length\
  \ Name\n----                -------------         ------ ----\n-a----       11/26/2019\
  \   8:26 AM           1328 secrets.txt"
created_at: '2019-11-26T17:16:42.492174+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get-ChildItem Recursive Search for Files and Folders

```powershell
Get-ChildItem -Recurse -Filter "$_FILENAME"
```

## Expected Output

```
PS C:\Users> Get-ChildItem -Recurse -Filter "secrets.txt"


    Directory: C:\Users\Bob\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       11/26/2019   8:26 AM           1328 secrets.txt
```


