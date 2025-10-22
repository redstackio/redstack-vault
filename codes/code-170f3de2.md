---
id: 170f3de2-044e-4a7a-a469-41fc714c3a34
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.851870+00:00'
updated_at: '2023-04-06T03:56:21.863869+00:00'
---

# Code Snippet 170f3de2

**Language**: Powershell

```powershell
# Windows
PS C:\> msg Swissky /SERVER:CRASHLAB "Stop rebooting the XXXX service !"
PS C:\> msg * /V /W /SERVER:CRASHLAB "Hello all !"

# Linux
$ wall "Stop messing with the XXX service !"
$ wall -n "System will go down for 2 hours maintenance at 13:00 PM"  # "-n" only for root
$ who
$ write root pts/2	# press Ctrl+D  after typing the message. 
```
