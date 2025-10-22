---
id: 3719470f-3938-4e6b-b061-c119d8966490
name: Execute custom command with StandIn.exe
type: command
executor: bash
data: StandIn.exe --gpo --filter Shards --tasktype computer --taskname Liber --author
  "REDHOOK\Administrator" --command "C:\I\do\the\thing.exe" --args "with args"
output: null
created_at: '2023-04-06T03:56:03.746787+00:00'
updated_at: '2023-04-10T20:25:53.888835+00:00'
---

# Execute custom command with StandIn.exe

```bash
StandIn.exe --gpo --filter Shards --tasktype computer --taskname Liber --author "REDHOOK\Administrator" --command "C:\I\do\the\thing.exe" --args "with args"
```
