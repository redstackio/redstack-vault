---
id: 722da87d-5292-4b3b-8eeb-9a4d766f9b6e
name: Import /etc/passwd file into PostgreSQL as a large object
type: command
executor: bash
data: SELECT lo_import('/etc/passwd');
output: null
created_at: '2023-04-06T03:56:35.929754+00:00'
updated_at: '2023-04-10T20:23:15.905451+00:00'
---

# Import /etc/passwd file into PostgreSQL as a large object

```bash
SELECT lo_import('/etc/passwd');
```
