---
id: 430dddcd-98f4-4908-9b36-4cee786a2372
name: Enable Wdigest
type: command
executor: bash
data: reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential
  /t REG_DWORD /f /d 1
output: null
created_at: '2023-04-06T03:56:27.124127+00:00'
updated_at: '2023-04-10T20:37:16.231490+00:00'
---

# Enable Wdigest

```bash
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /f /d 1
```
