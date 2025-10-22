---
id: 0c2024b6-a89a-4c87-82ab-3c2e58242407
name: Print current user
type: command
executor: bash
data: EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("getpass").getuser())'
output: null
created_at: '2023-04-06T03:56:33.953633+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
---

# Print current user

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("getpass").getuser())'
```
