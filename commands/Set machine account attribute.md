---
id: 8fe6344d-1d2a-4254-85f1-9b1a96512e5a
name: Set Machine Account Attribute
type: command
executor: bash
data: powermad@windows> Set-MachineAccountAttribute -MachineAccount "ControlledComputer"
  -Value "ControlledComputer" -Attribute samaccountname -Verbose
output: null
created_at: '2023-04-06T03:56:03.097023+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Set Machine Account Attribute

```bash
powermad@windows> Set-MachineAccountAttribute -MachineAccount "ControlledComputer" -Value "ControlledComputer" -Attribute samaccountname -Verbose
```
