---
id: 33cf40e1-ce36-4468-9932-68bb1ce653e5
name: Run PrivescCheck.ps1 script and generate report
type: command
executor: bash
data: powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report
  PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
output: null
created_at: '2023-04-06T03:56:28.514734+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
---

# Run PrivescCheck.ps1 script and generate report

```bash
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
```
