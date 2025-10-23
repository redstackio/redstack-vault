---
id: 64a1000d-77f7-43f5-9f87-be377120e9da
name: Active Directory Recon - Using AD Module
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.472447+00:00'
updated_at: '2023-04-10T20:36:08.291570+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Recon]]'
- '[[Using AD Module]]'
commands:
- '[[Enumerate Domains of Forest]]'
- '[[Get Active Directory Forest]]'
- '[[Get Active Directory Forest by Identity]]'
- '[[Get all AD Computers]]'
- '[[Get all AD Groups]]'
- '[[Get all properties of a specific user]]'
- '[[Get details of a specific AD trust]]'
- '[[Get Domain Controller Information]]'
- '[[Get Specific Domain Controller Information]]'
- '[[Get user with specific string in Description attribute]]'
- '[[List all AD trusts in the domain]]'
---

# Active Directory Recon - Using AD Module

## Summary

Active Directory Recon using the AD Module is a technique used by attackers to gather information about a target Active Directory environment. This technique involves using the AD Module to query Active Directory for information about domain controllers, users, computers, groups, and trust relation

## Description

# Description

Active Directory Recon using the AD Module is a technique used by attackers to gather information about a target Active Directory environment. This technique involves using the AD Module to query Active Directory for information about domain controllers, users, computers, groups, and trust relationships. By gathering this information, attackers can identify potential targets for further attacks, such as privilege escalation or lateral movement.

From a technical perspective, this technique involves using PowerShell to connect to the target Active Directory environment and running AD Module cmdlets to query for information. This technique is often used in combination with other reconnaissance techniques to build a complete picture of the target environment.

From a business perspective, this technique can be used by attackers to gain a foothold in the target environment and move laterally to other systems. This can result in data theft, system disruption, and reputational damage to the target organization.

 

## Requirements

1. Access to the target Active Directory environment

1. PowerShell with the AD Module installed

 

## Defense

1. Limit access to the AD Module to only authorized users

1. Monitor for suspicious activity involving the AD Module

1. Implement least privilege access controls to limit the impact of successful attacks

 

## Objectives

1. Gather information about the target Active Directory environment

1. Identify potential targets for further attacks

1. Build a complete picture of the target environment

 

# Instructions

1. Use the Get-ADDomainController cmdlet to retrieve a list of domain controllers in the current domain or a specified domain.

 



**Code**: [[Get-ADDomainController
Get-ADDomainController -Ide]]



> The Get-ADDomainController cmdlet retrieves the domain controllers specified by the parameters. If no parameters are specified, this cmdlet retrieves all domain controllers in the domain. The Identity parameter specifies the Active Directory domain or forest to get the domain controllers from. If you do not specify a value for the Identity parameter, the cmdlet uses the domain of the current user.



**Command** ([[Get Domain Controller Information]]):

```bash
Get-ADDomainController
```





**Command** ([[Get Specific Domain Controller Information]]):

```bash
Get-ADDomainController -Identity <DomainName>
```



2. Use the Get-ADUser command to retrieve information about all users in the domain. Use the -Filter parameter to specify the filter criteria, and the -Properties parameter to specify which properties to retrieve.

 



**Code**: [[Get-ADUser -Filter * -Identity <user> -Properties ]]



> The Get-ADUser command is used to retrieve information about all users in the domain. The -Filter parameter is used to specify the filter criteria, which can be used to retrieve specific users based on certain attributes like name, title, department, etc. The -Properties parameter is used to specify which properties to retrieve for each user. For example, you can use the -Properties parameter to retrieve the user's name, description, email address, etc. The command can also be used to retrieve a specific "string" on a user's attribute by using the -Filter parameter with the -like operator, and then piping the output to the Select-Object cmdlet to display only the Name and Description properties.



**Command** ([[Get all properties of a specific user]]):

```bash
Get-ADUser -Filter * -Identity <user> -Properties *
```





**Command** ([[Get user with specific string in Description attribute]]):

```bash
Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description | select Name, Description
```



3. This command is used to retrieve all the computers and groups in the domain. The 'Get-ADComputer' cmdlet is used to retrieve information about the computers and the 'Get-ADGroup' cmdlet is used to retrieve information about the groups.

 



**Code**: [[Get-ADComputer -Filter * -Properties *
Get-ADGroup]]



> The '-Filter' parameter is used to filter the results based on certain criteria. Here, we are using '*' to retrieve all the objects. The '-Properties' parameter is used to specify the properties that should be retrieved for the objects. Here, we are using '*' to retrieve all the properties.



**Command** ([[Get all AD Computers]]):

```bash
Get-ADComputer -Filter * -Properties *
```





**Command** ([[Get all AD Groups]]):

```bash
Get-ADGroup -Filter *
```



4. To enumerate all domain trusts, run the command 'Get-ADTrust -Filter *'. To get information about a specific domain trust, run the command 'Get-ADTrust -Identity <DomainName>'. Replace <DomainName> with the name of the domain trust you want to get information about.

 



**Code**: [[Get-ADTrust -Filter *
Get-ADTrust -Identity <Domai]]



> This command is used to retrieve information about domain trusts in Active Directory. The 'Get-ADTrust' cmdlet is used to perform this operation. The 'Filter' parameter is used to retrieve all domain trusts, while the 'Identity' parameter is used to retrieve information about a specific domain trust. The output of this command includes information such as the trust type, direction, and status of the domain trust.



**Command** ([[List all AD trusts in the domain]]):

```bash
Get-ADTrust -Filter *
```





**Command** ([[Get details of a specific AD trust]]):

```bash
Get-ADTrust -Identity <DomainName>
```



5. This command is used to enumerate the trust relationships between forests in an Active Directory environment.

 



**Code**: [[Get-ADForest
Get-ADForest -Identity <ForestName>

]]



> The Get-ADForest command retrieves the properties of the specified Active Directory forest, or the current forest if no forest is specified. The -Identity parameter specifies the name of the forest whose properties are being retrieved. The .Domains property returns the domain names in the forest. This command can be used to identify the trust relationships between forests by comparing the domain names in each forest.



**Command** ([[Get Active Directory Forest]]):

```bash
Get-ADForest
```





**Command** ([[Get Active Directory Forest by Identity]]):

```bash
Get-ADForest -Identity <ForestName>
```





**Command** ([[Enumerate Domains of Forest]]):

```bash
(Get-ADForest).Domains
```



6. To retrieve the AppLocker rule collections, run the following command:

 



**Code**: [[Get-AppLockerPolicy -Effective | select -ExpandPro]]



> This command retrieves the AppLocker policy rule collections that are currently in effect on the system. The rule collections contain the rules that define which applications are allowed or blocked on the system. The output of this command includes information such as the rule type, the enforcement mode, and the rule conditions. This information can be useful for troubleshooting AppLocker policy issues and for auditing the security posture of the system.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Commands Used

- [[Enumerate Domains of Forest]]
- [[Get Active Directory Forest]]
- [[Get Active Directory Forest by Identity]]
- [[Get all AD Computers]]
- [[Get all AD Groups]]
- [[Get all properties of a specific user]]
- [[Get details of a specific AD trust]]
- [[Get Domain Controller Information]]
- [[Get Specific Domain Controller Information]]
- [[Get user with specific string in Description attribute]]
- [[List all AD trusts in the domain]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Recon]]
- [[Using AD Module]]


