---
id: b653b33e-1a80-4892-934e-2939d8205330
name: Print Python version
type: command
executor: bash
data: 'EXECUTE sp_execute_external_script @language = N''Python'', @script = N''

  import sys

  print(sys.version)

  '''
output: null
created_at: '2023-04-06T03:56:33.953882+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
---

# Print Python version

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'
import sys
print(sys.version)
'
```
