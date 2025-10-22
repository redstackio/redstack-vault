---
id: 781b9384-af36-4f07-bff5-c32c2944cadf
name: Convert @@version to string
type: command
executor: bash
data: ''' + convert(int,@@version) + '''
output: null
created_at: '2023-04-06T03:56:33.815978+00:00'
updated_at: '2023-04-10T20:22:41.312777+00:00'
---

# Convert @@version to string

```bash
' + convert(int,@@version) + '
```
