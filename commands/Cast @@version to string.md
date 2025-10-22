---
id: 6e02fe43-9271-4ead-b09e-9a0701095cf1
name: Cast @@version to string
type: command
executor: bash
data: ''' + cast((SELECT @@version) as int) + '''
output: null
created_at: '2023-04-06T03:56:33.816032+00:00'
updated_at: '2023-04-10T20:22:41.312777+00:00'
---

# Cast @@version to string

```bash
' + cast((SELECT @@version) as int) + '
```
