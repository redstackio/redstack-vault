---
id: b9484813-3acb-45e6-8a6b-471f166264e7
name: Cast @@version to integer
type: command
executor: bash
data: cast((SELECT @@version) as int)
output: null
created_at: '2023-04-06T03:56:33.815888+00:00'
updated_at: '2023-04-10T20:22:41.312777+00:00'
---

# Cast @@version to integer

```bash
cast((SELECT @@version) as int)
```
