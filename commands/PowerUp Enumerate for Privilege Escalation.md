---
id: 89fb504d-bae1-442f-a5c4-407e91a60b09
name: PowerUp Enumerate for Privilege Escalation
type: command
executor: command_prompt
data: SharpUp.exe audit
output: "C:\\Temp>SharpUp.exe audit \n\n=== SharpUp: Running Privilege Escalation\
  \ Checks ===\n\n\n=== Modifiable Services ===\n\nName             : UsoSVC\nDisplayName\
  \      : UsoSVC\n..."
created_at: '2020-03-13T18:30:55.939823+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerUp Enumerate for Privilege Escalation

```command_prompt
SharpUp.exe audit
```

## Expected Output

```
C:\Temp>SharpUp.exe audit 

=== SharpUp: Running Privilege Escalation Checks ===

=== Modifiable Services ===

Name             : UsoSVC
DisplayName      : UsoSVC
...
```
