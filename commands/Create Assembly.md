---
id: 9a6398fd-a129-4627-8805-8b9526edebd6
name: Create Assembly
type: command
executor: bash
data: 'CREATE ASSEMBLY my_assembly

  FROM ''c:\temp\cmd_exec.dll''

  WITH PERMISSION_SET = UNSAFE;'
output: null
created_at: '2023-04-06T03:56:20.431422+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
---

# Create Assembly

```bash
CREATE ASSEMBLY my_assembly
FROM 'c:\temp\cmd_exec.dll'
WITH PERMISSION_SET = UNSAFE;
```


