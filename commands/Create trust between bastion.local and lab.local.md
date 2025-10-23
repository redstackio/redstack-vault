---
id: b4369bb7-ce4b-4c5a-8b64-d5c2756c7ff1
name: Create trust between bastion.local and lab.local
type: command
executor: bash
data: netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
output: null
created_at: '2023-04-06T03:56:07.394167+00:00'
updated_at: '2023-04-10T20:26:01.511941+00:00'
---

# Create trust between bastion.local and lab.local

```bash
netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
```


