---
id: 64893ee0-c4a1-430a-8c87-0477283abdc7
name: Run PrivescCheck.ps1 script
type: command
executor: bash
data: powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
output: null
created_at: '2023-04-06T03:56:28.514587+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
---

# Run PrivescCheck.ps1 script

```bash
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```
