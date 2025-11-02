---
id: e8834c77-abc3-4d76-9030-76ecf1d4e5af
name: PowerShell Generate a Secure String
type: command
executor: ''
data: $pass = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force
output: PS C:\> $pass = ConvertTo-SecureString "secretpass" -AsPlainText -Force
created_at: '2019-09-30T19:48:33.640394+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
- '[[ps]]'
---

# PowerShell Generate a Secure String

```bash
$pass = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force
```

## Expected Output

```
PS C:\> $pass = ConvertTo-SecureString "secretpass" -AsPlainText -Force
```


