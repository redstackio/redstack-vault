---
id: 0a31cea8-b444-4f75-9ad6-3e08a265f16e
name: Add Computer to Domain
type: command
executor: bash
data: impacket@linux> addcomputer.py -computer-name 'ControlledComputer$' -computer-pass
  'ComputerPassword' -dc-host DC01 -domain-netbios domain 'domain.local/user1:complexpassword'
output: null
created_at: '2023-04-06T03:56:03.096135+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Add Computer to Domain

```bash
impacket@linux> addcomputer.py -computer-name 'ControlledComputer$' -computer-pass 'ComputerPassword' -dc-host DC01 -domain-netbios domain 'domain.local/user1:complexpassword'
```


