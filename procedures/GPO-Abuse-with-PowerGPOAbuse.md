---
id: c847de47-fff9-44db-962b-28d3fdd9d19e
name: GPO-Abuse-with-PowerGPOAbuse
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.672399+00:00'
updated_at: '2023-10-10T20:26:15.893452+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Group Policy Modification|T1484 - Group Policy Modification]]'
sub_techniques: []
tags:
  - '[[tags/Abuse GPO with PowerGPOAbuse]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Exploit Group Policy Objects GPO]]'
commands:
  - '[[commands/add-local-admin-gpo]]'
  - '[[commands/add-user-rights-gpo]]'
  - '[[commands/add-script-to-gpo]]'
  - '[[commands/create-gpo-immediate-task]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerGPOAbuse]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# GPO-Abuse-with-PowerGPOAbuse

## Summary

This procedure demonstrates how to abuse Group Policy Objects (GPOs) in an Active Directory environment using the PowerGPOAbuse PowerShell module. It allows attackers with sufficient permissions to modify GPOs to add local administrators, assign user rights, inject scripts, and create immediate tasks, enabling privilege escalation, persistence, and lateral movement across the domain.

## Description

Group Policy Objects (GPOs) are used to enforce configurations and policies across Active Directory domains. If an attacker gains access to create or edit GPOs (typically requiring domain admin or delegated rights), they can leverage tools like PowerGPOAbuse to inject malicious configurations. This includes adding users to local admin groups on targeted machines, granting advanced privileges like SeDebugPrivilege, deploying scripts that execute on logon or startup, and scheduling immediate tasks for rapid payload execution. The technique targets Windows environments with Active Directory and is effective for post-compromise scenarios where initial foothold credentials allow GPO manipulation. Success relies on the GPO being linked to organizational units affecting target systems, with changes propagating via gpupdate.

## Requirements

1. Domain user account with permissions to create or edit GPOs (e.g., Domain Admin or delegated GPO edit rights).
2. Access to a Windows machine joined to the domain with PowerShell execution policy allowing script loading.
3. PowerGPOAbuse module downloaded and available locally.
4. Target GPO name or ID, and a malicious script file (e.g., evil.ps1) prepared for injection.
5. Network connectivity to a Domain Controller for GPO modifications.

## Defense

- Restrict GPO creation and editing to a minimal set of trusted administrators using Role-Based Access Control (RBAC).
- Enable Group Policy auditing to log all modifications, including who, what, and when changes were made.
- Implement change approval workflows for GPO updates and monitor for anomalous scripts or rights assignments via tools like Microsoft Advanced Group Policy Management (AGPM).
- Regularly review GPO links and filters to ensure they are not overly broad, and use security filtering to limit scope.
- Deploy endpoint detection tools to alert on unexpected script execution from GPO-sourced tasks or privileges.

## Objectives

1. Modify GPOs to grant elevated privileges to attacker-controlled accounts, enabling local admin access on domain machines.
2. Inject and execute malicious scripts or commands via GPO startup/logon scripts or scheduled tasks for persistence and payload delivery.
3. Achieve domain-wide impact by leveraging GPO propagation to affected systems without direct lateral movement.
4. Maintain stealth by mimicking legitimate GPO configurations.

## Instructions

### Step 1: Load the PowerGPOAbuse Module

**Context**: Before using any abuse functions, load the PowerGPOAbuse PowerShell script into the current session to make its cmdlets available. This step is essential as the tool is provided as a .ps1 file that must be dot-sourced.

```powershell
. .\PowerGPOAbuse.ps1
```

> This command imports the module functions without creating a new scope. Expected output is minimal (no errors), confirming the functions like Add-LocalAdmin are now available via Get-Command.

### Step 2: Add a Local Administrator via GPO

**Context**: Use this step to add an attacker-controlled user to the local Administrators group on machines affected by the target GPO, allowing privilege escalation on those systems upon next gpupdate or reboot.

**Command** ([[commands/add-local-admin-gpo]]):
```powershell
Add-LocalAdmin -Identity $_USERNAME -GPOIdentity $_GPONAME
```

> Replace $_USERNAME with the target user (e.g., 'Bobby') and $_GPONAME with the GPO name (e.g., 'SuperSecureGPO'). This modifies the GPO's security settings to include the user in the local admin group. Expected output: Confirmation message like "Successfully added user to local admins in GPO 'SuperSecureGPO'".

### Step 3: Assign User Rights via GPO

**Context**: Grant specific advanced privileges (e.g., SeLoadDriverPrivilege, SeDebugPrivilege) to the user via the GPO, enabling capabilities like driver loading or debugging processes on affected machines for further exploitation.

**Command** ([[commands/add-user-rights-gpo]]):
```powershell
Add-UserRights -Rights $_RIGHTS -Identity $_USERNAME -GPOIdentity $_GPONAME
```

> Specify $_RIGHTS as a comma-separated list (e.g., "SeLoadDriverPrivilege","SeDebugPrivilege"), $_USERNAME as the target user, and $_GPONAME as the GPO. This updates the GPO's user rights assignment policy. Expected output: "User rights assigned successfully in GPO 'SuperSecureGPO'".

### Step 4: Add a Script to GPO

**Context**: Inject a malicious script into the GPO to execute on computer startup or user logon, providing persistence or payload delivery across the domain without direct access to each machine.

**Command** ([[commands/add-script-to-gpo]]):
```powershell
Add-ComputerScript -ScriptName $_SCRIPTNAME -ScriptContent $(Get-Content $_SCRIPTFILE) -GPOIdentity $_GPONAME
```

> Use Add-ComputerScript for machine-wide execution or Add-UserScript for user-specific. Provide $_SCRIPTNAME (e.g., 'EvilScript'), $_SCRIPTFILE (e.g., 'evil.ps1'), and $_GPONAME. This embeds the script content into the GPO's script settings. Expected output: "Script added to GPO 'SuperSecureGPO'".

### Step 5: Create an Immediate Task via GPO

**Context**: Schedule an immediate execution task in the GPO to run a command or script right after policy refresh, ideal for rapid payload deployment without waiting for logon or reboot.

**Command** ([[commands/create-gpo-immediate-task]]):
```powershell
Add-GPOImmediateTask -TaskName $_TASKNAME -Command $_COMMAND -CommandArguments "$_ARGUMENTS" -Author $_AUTHOR -Scope $_SCOPE -GPOIdentity $_GPONAME
```

> Set $_TASKNAME (e.g., 'eviltask'), $_COMMAND (e.g., 'powershell.exe'), $_ARGUMENTS (e.g., "'$(Get-Content evil.ps1)'"), $_AUTHOR (e.g., 'Administrator'), $_SCOPE ('Computer' or 'User'), and $_GPONAME. This creates a scheduled task in the GPO. Expected output: "Immediate task created in GPO 'SuperSecureGPO'".

### Step 6: Verify and Propagate Changes

**Context**: After modifications, force GPO update on target machines to apply changes immediately and verify success.

```powershell
gpupdate /force
Get-GPResultantSetOfPolicy -ReportType Html -Path C:\gpresult.html
```

> Run on a target machine to apply policies. Review the gpresult.html for evidence of new admins, rights, scripts, or tasks. Expected output: Updated policy report showing injected configurations.
