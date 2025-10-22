---
id: 04b568da-c6a2-4f9c-be78-c45663358027
name: Windows Registry HKLM Run Key Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.993429+00:00'
updated_at: '2023-04-10T20:37:29.335286+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[Elevated]]'
- '[[Registry HKLM]]'
- '[[Windows - Persistence]]'
commands:
- '[[Add backdoor to startup registry]]'
---

# Windows Registry HKLM Run Key Persistence

## Summary

Windows Registry HKLM Run Key Persistence is a technique used by attackers to maintain their foothold on a compromised system. This technique involves adding a registry key to the HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run location, which ensures that a specified program will be executed ev

## Description

# Description

Windows Registry HKLM Run Key Persistence is a technique used by attackers to maintain their foothold on a compromised system. This technique involves adding a registry key to the HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run location, which ensures that a specified program will be executed every time the system boots up. Attackers can use this technique to maintain persistence on a system even after a reboot. This technique is commonly used by malware authors to ensure the malware is executed every time the system starts up. 

From a technical standpoint, this technique involves adding a registry key to the HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run location. This registry key contains a value that specifies the program to be executed at startup. This technique requires elevated privileges to add the registry key to the HKLM hive. 

The business value of this technique is that attackers can maintain persistence on a compromised system and continue to exfiltrate sensitive data or use the system as a foothold to launch further attacks.

## Requirements

1. Elevated privileges to add the registry key to the HKLM hive

## Defense

1. Implement the principle of least privilege to prevent attackers from gaining elevated privileges

1. Monitor the HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run location for unauthorized changes

1. Use endpoint detection and response (EDR) tools to detect and respond to malicious activity on endpoints

## Objectives

1. Maintain persistence on a compromised system

1. Ensure that a specified program is executed every time the system boots up

# Instructions

1. To create a new Run key value using PowerShell, follow these steps:
1. Open PowerShell as an administrator
2. Type the following command: New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'Backdoor' -Value 'C:\Windows\Temp\backdoor.exe' -PropertyType String
3. Press Enter

**Code**: [[Value name: Backdoor
Value data: C:\Windows\Temp\b]]

> This command creates a new Run key value in the Windows registry. The Run key is a registry key that contains a list of programs that are executed automatically when Windows starts. By creating a new value in the Run key, you can add a program to the list of programs that are executed automatically.

The command uses the New-ItemProperty cmdlet to create a new value in the Run key. The -Path parameter specifies the path to the Run key, and the -Name and -Value parameters specify the name and data of the new value. The -PropertyType parameter specifies the type of the new value, which in this case is a string.

2. This command adds registry run keys to execute the specified file on system startup.

**Code**: [[reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Win]]

> The command adds registry keys to the specified locations in the Windows registry. These keys are used to execute the specified file on system startup. The /v option specifies the name of the value to be added or modified. The /t option specifies the type of the registry value to be added or modified. The /d option specifies the data for the registry value to be added or modified. In this case, the command adds a registry key named 'Evil' with a value of 'C:\tmp\backdoor.exe' to each of the specified locations in the registry.

**Command** ([[Add backdoor to startup registry]]):

```bash
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Add backdoor to startup registry]]

## Tags

- [[Elevated]]
- [[Registry HKLM]]
- [[Windows - Persistence]]
