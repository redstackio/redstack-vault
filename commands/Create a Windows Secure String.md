---
id: 343600f5-fe61-4572-88de-f22f97402962
name: Create a Windows Secure String
type: command
executor: powershell
data: $Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
output: PS C:\Users\Bob > $Pass = ConvertTo-SecureString -String "secretpass" -AsPlainText
  -Force
created_at: '2020-03-13T23:31:09.273542+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[ps]]'
---

# Create a Windows Secure String

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```

## Expected Output

```
PS C:\Users\Bob > $Pass = ConvertTo-SecureString -String "secretpass" -AsPlainText -Force
```


