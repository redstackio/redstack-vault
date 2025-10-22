---
id: 8c4a77f0-6492-4b4d-be30-85154d0bc348
name: Abuse GPO with PowerView to Push Empire Stager
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.724499+00:00'
updated_at: '2023-04-10T20:26:34.284443+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
tags:
- '[[Abuse GPO with PowerView]]'
- '[[Active Directory Attacks]]'
- '[[Exploit Group Policy Objects GPO]]'
---

# Abuse GPO with PowerView to Push Empire Stager

## Summary

Abusing Group Policy Objects (GPO) is a common technique used by attackers to gain persistence and execute malicious code within a target's Active Directory environment. With PowerView, an attacker can enumerate GPOs and identify vulnerable GPOs that can be modified to execute arbitrary PowerShell 

## Description

# Description

Abusing Group Policy Objects (GPO) is a common technique used by attackers to gain persistence and execute malicious code within a target's Active Directory environment. With PowerView, an attacker can enumerate GPOs and identify vulnerable GPOs that can be modified to execute arbitrary PowerShell commands. This specific procedure involves pushing an Empire stager via a vulnerable GPO. By doing so, the attacker can establish a foothold within the target environment and potentially move laterally to other systems.

From a technical standpoint, PowerView is used to enumerate GPOs and identify those that have weak ACLs. Once a vulnerable GPO is identified, PowerShell is used to modify the GPO and add a script that will execute the Empire stager. The stager is then executed on all systems that receive the GPO, allowing the attacker to establish a foothold.

The business value of this attack lies in the ability of the attacker to gain persistence within the target environment, potentially allowing them to maintain access and exfiltrate sensitive data over an extended period of time.

## Requirements

1. Access to the target Active Directory environment

1. PowerView

1. Empire stager

## Defense

1. Ensure that GPOs are properly secured with strong ACLs

1. Monitor for any modifications to GPOs

1. Implement network segmentation to limit lateral movement

## Objectives

1. Gain persistence within the target environment

1. Execute arbitrary PowerShell commands

1. Establish a foothold within the target environment

1. Potentially move laterally to other systems

# Instructions

1. To enumerate group policy objects and their associated access control lists, run the following command:

Get-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name}

To push an Empire stager to machines via a vulnerable GPO, run the following command:

New-GPOImmediateTask -TaskName Debugging -GPODisplayName VulnGPO -CommandArguments '-NoP -NonI -W Hidden -Enc AAAAAAA...' -Force

Replace the command arguments with the appropriate values for your environment.

**Code**: [[# Enumerate GPO
Get-NetGPO | %{Get-ObjectAcl -Reso]]

> The first command retrieves a list of all group policy objects and their associated access control lists. This can be useful for identifying potential misconfigurations or vulnerabilities.

The second command uses the New-GPOImmediateTask cmdlet to push an Empire stager to machines via a vulnerable GPO. The TaskName parameter specifies the name of the scheduled task to be created, while the GPODisplayName parameter specifies the name of the GPO to be targeted. The CommandArguments parameter specifies the arguments to be passed to the stager, and the Force parameter forces the creation of the scheduled task even if it already exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]

## Tags

- [[Abuse GPO with PowerView]]
- [[Active Directory Attacks]]
- [[Exploit Group Policy Objects GPO]]
