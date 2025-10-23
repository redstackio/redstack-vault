---
id: 4f59530c-3ade-4805-80d3-f78b03c51d56
name: Extract databases names
type: command
executor: bash
data: '$ SELECT name FROM master..sysdatabases

  [*] Injection

  [*] msdb

  [*] tempdb'
output: null
created_at: '2023-04-06T03:56:33.777938+00:00'
updated_at: '2023-04-10T20:22:44.170609+00:00'
---

# Extract databases names

```bash
$ SELECT name FROM master..sysdatabases
[*] Injection
[*] msdb
[*] tempdb
```


