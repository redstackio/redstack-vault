---
id: 013b77ee-d08d-4e2d-8c4d-62fef28ea99e
name: Access machine using password
type: command
executor: bash
data: Enter-PSSession -ComputerName <AnyMachineYouLike> -Credential <Domain>\Administrator
output: null
created_at: '2023-04-06T03:56:28.268893+00:00'
updated_at: '2023-04-10T20:37:25.397457+00:00'
---

# Access machine using password

```bash
Enter-PSSession -ComputerName <AnyMachineYouLike> -Credential <Domain>\Administrator
```
