---
id: b050f3f7-8775-49ee-b112-e147f01e44cf
name: Abuse Group Policy Objects with pyGPOAbuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.703618+00:00'
updated_at: '2023-04-10T20:26:12.011925+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Emond|T1546.014 - Emond]]'
- '[[Print Processors|T1547.012 - Print Processors]]'
tags:
- '[[Abuse GPO with pyGPOAbuse]]'
- '[[Active Directory Attacks]]'
- '[[Exploit Group Policy Objects GPO]]'
---

# Abuse Group Policy Objects with pyGPOAbuse

## Summary

Abusing Group Policy Objects (GPOs) is a common technique used by attackers to gain persistence and elevate privileges within an Active Directory environment. pyGPOAbuse is a Python tool that allows an attacker to interact with GPOs and modify them in a variety of ways. This tool can be used to ena

## Description

# Description

Abusing Group Policy Objects (GPOs) is a common technique used by attackers to gain persistence and elevate privileges within an Active Directory environment. pyGPOAbuse is a Python tool that allows an attacker to interact with GPOs and modify them in a variety of ways. This tool can be used to enable or disable certain policies, add new policies, or even execute arbitrary code as SYSTEM on all machines within the domain. Attackers can use this tool to escalate privileges and maintain persistence within the environment.

Technical Explanation: pyGPOAbuse works by abusing the SYSVOL share in Active Directory, which is used to distribute GPOs to all machines within the domain. By modifying the contents of the SYSVOL share, an attacker can modify the GPOs and execute arbitrary code on all machines within the domain. This technique is particularly dangerous because GPOs are automatically applied to all machines within the domain and are executed with SYSTEM privileges. Once an attacker has successfully modified a GPO, they can maintain persistence and escalate privileges within the environment.

Business Value: By abusing GPOs with pyGPOAbuse, attackers can gain persistent access to an organization's network and escalate their privileges. This can allow them to steal sensitive data, install malware, or cause other damage to the organization. Organizations should be aware of this technique and take steps to secure their GPOs and Active Directory environment.

 

## Requirements

1. Access to the Active Directory environment

1. Python and pyGPOAbuse installed on the attacker's machine

1. Credentials with permissions to modify GPOs

 

## Defense

1. Regularly review and monitor GPOs for unauthorized modifications

1. Restrict access to the SYSVOL share and GPOs to only authorized users

1. Implement least privilege access controls to limit the impact of GPO abuse

 

## Objectives

1. Gain persistence within the Active Directory environment

1. Escalate privileges to gain access to sensitive data

1. Maintain access to the environment for future attacks

 

# Instructions

1. The pyGPOAbuse tool is used to abuse Group Policy Objects (GPOs) in Active Directory environments. In this example, we are cloning the pyGPOAbuse repository from GitHub and using it to add the user 'john' to the local administrators group on the domain. We are also running a reverse shell example that connects to a remote IP address and port, and creates a new TCP client. The -powershell flag is used to specify that the command to be executed is PowerShell. The -command flag is used to specify the PowerShell command to be executed. The -taskname flag is used to specify the name of the task that will be created in the Task Scheduler. The -description flag is used to specify a description for the task. The -user flag is used to specify the user account that will be used to create the scheduled task.

 



**Code**: [[$ git clone https://github.com/Hackndo/pyGPOAbuse
]]



> This command is useful for red teamers and penetration testers who want to escalate their privileges on a domain. By abusing Group Policy Objects, they can add themselves to privileged groups on the domain, such as the local administrators group, and gain access to sensitive resources. The reverse shell example can be used to establish a persistent backdoor on the target system, allowing the attacker to maintain access even if their initial access is discovered and removed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Emond|T1546.014 - Emond]]
- [[Print Processors|T1547.012 - Print Processors]]

## Tags

- [[Abuse GPO with pyGPOAbuse]]
- [[Active Directory Attacks]]
- [[Exploit Group Policy Objects GPO]]


