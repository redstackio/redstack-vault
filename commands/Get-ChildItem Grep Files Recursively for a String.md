---
id: 34ac0102-3aeb-43a3-9ed3-100d7d4ed115
name: Get-ChildItem Grep Files Recursively for a String
type: command
executor: powershell
data: Get-ChildItem -Recurse -Path $_PATH | Select-String -Pattern "$_STRING"
output: 'PS C:\Users> Get-ChildItem -Recurse -Path . |Select-String -Pattern "TOP
  SECRET"


  Bob\Desktop\secrets.txt:1:TOP SECRET TIP'
created_at: '2019-11-26T17:16:42.492729+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[grep]]'
- '[[ps]]'
---

# Get-ChildItem Grep Files Recursively for a String

```powershell
Get-ChildItem -Recurse -Path $_PATH | Select-String -Pattern "$_STRING"
```

## Expected Output

```
PS C:\Users> Get-ChildItem -Recurse -Path . |Select-String -Pattern "TOP SECRET"

Bob\Desktop\secrets.txt:1:TOP SECRET TIP
```


