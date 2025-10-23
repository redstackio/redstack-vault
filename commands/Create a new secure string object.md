---
id: 84f78f12-7740-4c96-bc62-7c083cd4bca5
name: Create a new secure string object
type: command
executor: bash
data: $password = "Password" | ConvertToSecureString -AsPlainText -Force
output: null
created_at: '2023-04-06T03:56:15.848056+00:00'
updated_at: '2023-04-10T20:19:31.152057+00:00'
---

# Create a new secure string object

```bash
$password = "Password" | ConvertToSecureString -AsPlainText -Force
```


