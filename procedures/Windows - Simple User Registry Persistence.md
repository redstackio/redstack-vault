---
id: 307623de-dd0f-4681-b0b7-3f527962ff97
name: Windows - Simple User Registry Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.778833+00:00'
updated_at: '2023-04-10T20:37:28.563366+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[Registry HKCU]]'
- '[[Simple User]]'
- '[[Windows - Persistence]]'
commands:
- '[[Add registry key and value for persisting cmd.exe with calc.exe on current user
  run]]'
- '[[Add registry key and value for persisting cmd.exe with calc.exe on current user
  run and output environment variables]]'
- '[[Add registry key and value for persisting cmd.exe with calc.exe on logon script]]'
- '[[Add registry keys for backdoor persistence]]'
- '[[Backdoor Installation]]'
---

# Windows - Simple User Registry Persistence

## Summary

Windows - Simple User Registry Persistence is a technique used by attackers to ensure that their malware or backdoor is automatically executed every time the user logs in. This technique involves creating a registry key in the HKCU hive that points to the location of the malware or backdoor. When t

## Description

# Description

Windows - Simple User Registry Persistence is a technique used by attackers to ensure that their malware or backdoor is automatically executed every time the user logs in. This technique involves creating a registry key in the HKCU hive that points to the location of the malware or backdoor. When the user logs in, Windows automatically executes the malware or backdoor. This technique is particularly useful for attackers who want to maintain access to a compromised system even after a reboot.

From a technical perspective, this technique involves adding a registry key to the HKCU hive that points to the location of the malware or backdoor. The key is typically added to the Run or RunOnce subkey, which ensures that the malware or backdoor is executed every time the user logs in. This technique can be used by attackers who have gained access to a system as a simple user, but want to elevate their privileges and maintain persistence.

From a business perspective, this technique can be used by attackers to maintain access to a compromised system and exfiltrate sensitive data. It can also be used to install additional malware or backdoors on the compromised system, which can be used for further attacks.

## Requirements

1. Access to the system as a simple user

1. Ability to modify the registry

## Defense

1. Implement strict access controls to prevent unauthorized access to the system

1. Regularly monitor the system for any changes to the registry

1. Use endpoint protection software to detect and block any malicious activity

## Objectives

1. Maintain access to a compromised system

1. Elevate privileges

1. Install additional malware or backdoors

1. Exfiltrate sensitive data

# Instructions

1. To create a backdoor registry value in Windows, follow these steps:
1. Open the Registry Editor by typing 'regedit' in the Run dialog box (Windows Key + R).
2. Navigate to HKCU\Software\Microsoft\Windows\CurrentVersion\Run.
3. Right-click on an empty space in the right pane and select 'New' > 'String Value'.
4. Enter 'Backdoor' as the name of the value.
5. Enter 'C:\Users\Rasta\AppData\Local\Temp\backdoor.exe' as the data for the value.
6. Close the Registry Editor.

**Code**: [[Value name: Backdoor
Value data: C:\Users\Rasta\Ap]]

> This command creates a new registry value called 'Backdoor' in the Run key within HKCU\Software\Microsoft\Windows. The value data is set to 'C:\Users\Rasta\AppData\Local\Temp\backdoor.exe', which is the location of the backdoor executable file. When the user logs in, the backdoor executable will be automatically executed.

**Command** ([[Backdoor Installation]]):

```bash
C:\Users\Rasta\AppData\Local\Temp\backdoor.exe
```

2. To add a backdoor to the Windows startup using the registry, run the following commands:

**Code**: [[reg add "HKEY_CURRENT_USER\Software\Microsoft\Wind]]

> This command adds a registry key to the Windows startup locations, which will execute the specified file every time the computer starts. The command adds the registry key to four different startup locations to ensure that the backdoor is executed even if one of the locations is disabled or deleted. The /v flag specifies the name of the registry value, /t specifies the type of the registry value, and /d specifies the data of the registry value. In this case, the name of the registry value is 'Evil', the type is 'REG_SZ', and the data is the path to the backdoor executable file.

**Command** ([[Add registry keys for backdoor persistence]]):

```bash
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
```

3. The SharPersist command is used to add persistence to a system via registry keys. The -t flag specifies the type of persistence to be added, in this case, registry. The -c flag specifies the command to be executed, in this case, cmd.exe. The -a flag specifies the arguments to be passed to the command, in this case, /c calc.exe. The -k flag specifies the registry key to be used for persistence, in this case, hkcurun and logonscript. The -v flag specifies the value name to be used for persistence, in this case, Test Stuff. The -m flag specifies the mode of persistence, in this case, add. The -o flag specifies the options for persistence, in this case, env.

**Code**: [[SharPersist -t reg -c "C:\Windows\System32\cmd.exe]]

> This command is used to add persistence to a system by creating registry keys. The registry keys are created under the specified hive and key path, and the specified command is executed with the specified arguments every time the system starts up or the user logs in. The -t flag specifies the type of persistence to be added, which can be either registry or scheduled task. The -c flag specifies the command to be executed, which can be any valid command or script. The -a flag specifies the arguments to be passed to the command. The -k flag specifies the registry key to be used for persistence. The -v flag specifies the value name to be used for persistence. The -m flag specifies the mode of persistence, which can be either add or remove. The -o flag specifies the options for persistence, which can be env for user environment variables or sys for system environment variables.

**Command** ([[Add registry key and value for persisting cmd.exe with calc.exe on current user run]]):

```bash
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add
```

**Command** ([[Add registry key and value for persisting cmd.exe with calc.exe on current user run and output environment variables]]):

```bash
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add -o env
```

**Command** ([[Add registry key and value for persisting cmd.exe with calc.exe on logon script]]):

```bash
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript" -m add
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Add registry key and value for persisting cmd.exe with calc.exe on current user run]]
- [[Add registry key and value for persisting cmd.exe with calc.exe on current user run and output environment variables]]
- [[Add registry key and value for persisting cmd.exe with calc.exe on logon script]]
- [[Add registry keys for backdoor persistence]]
- [[Backdoor Installation]]

## Tags

- [[Registry HKCU]]
- [[Simple User]]
- [[Windows - Persistence]]
