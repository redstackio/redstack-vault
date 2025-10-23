---
id: f4ff030f-1d7f-401d-b6e2-93ae483fa82e
name: Print current user with whoami
type: command
executor: bash
data: EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("os").system("whoami"))'
output: null
created_at: '2023-04-06T03:56:33.953703+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
---

# Print current user with whoami

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("os").system("whoami"))'
```


