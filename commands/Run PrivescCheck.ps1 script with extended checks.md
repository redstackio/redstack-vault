---
id: 6e352a62-e1f0-42d8-a1f4-f93911eb2767
name: Run PrivescCheck.ps1 script with extended checks
type: command
executor: bash
data: powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
output: null
created_at: '2023-04-06T03:56:28.514679+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
---

# Run PrivescCheck.ps1 script with extended checks

```bash
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
```
