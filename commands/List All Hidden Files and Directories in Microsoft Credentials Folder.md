---
id: 3c62294a-ce12-4c33-aa83-0ee4d4227b0f
name: List All Hidden Files and Directories in Microsoft Credentials Folder
type: command
executor: bash
data: 'Get-ChildItem -Hidden C:\Users\username\AppData\Local\Microsoft\Credentials\

  Get-ChildItem -Hidden C:\Users\username\AppData\Roaming\Microsoft\Credentials\'
output: null
created_at: '2023-04-06T03:56:26.245263+00:00'
updated_at: '2023-04-10T20:37:12.179475+00:00'
---

# List All Hidden Files and Directories in Microsoft Credentials Folder

```bash
Get-ChildItem -Hidden C:\Users\username\AppData\Local\Microsoft\Credentials\
Get-ChildItem -Hidden C:\Users\username\AppData\Roaming\Microsoft\Credentials\
```


