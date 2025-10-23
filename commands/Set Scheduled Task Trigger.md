---
id: 76bb43d6-f0b5-4e6f-8dec-5e890f2ef6e7
name: Set Scheduled Task Trigger
type: command
executor: bash
data: $T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
output: null
created_at: '2023-04-06T03:56:27.837479+00:00'
updated_at: '2023-04-10T20:37:30.438026+00:00'
---

# Set Scheduled Task Trigger

```bash
$T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
```


