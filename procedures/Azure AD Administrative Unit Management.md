---
id: 9418fe37-bf21-4774-a70d-602afabc316a
name: Azure AD Administrative Unit Management
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.860141+00:00'
updated_at: '2023-04-10T20:19:31.135607+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Protocol Tunneling|T1572 - Protocol Tunneling]]'
tags:
- '[[Administrative Unit]]'
- '[[Cloud - Azure]]'
commands:
- '[[Create a new secure string object]]'
- '[[Retrieve administrative unit members in Azure AD]]'
- '[[Retrieve administrative units in Azure AD]]'
- '[[Retrieve directory role in Azure AD]]'
- '[[Retrieve scoped role membership in Azure AD]]'
- '[[Retrieve user in Azure AD]]'
- '[[Set user password in Azure AD]]'
---

# Azure AD Administrative Unit Management

## Summary

The Azure AD Administrative Unit Management procedure is used to manage administrative units in Azure Active Directory. Administrative units allow for granular control over the scope of administrative permissions, and can be used to delegate administrative tasks to specific users or groups. By leve

## Description

# Description

The Azure AD Administrative Unit Management procedure is used to manage administrative units in Azure Active Directory. Administrative units allow for granular control over the scope of administrative permissions, and can be used to delegate administrative tasks to specific users or groups. By leveraging administrative units, an attacker with compromised credentials can escalate their privileges and gain access to sensitive data or systems. This procedure involves using Azure AD Management Commands to create, modify, or delete administrative units.

 

## Requirements

1. Valid Azure Active Directory credentials

1. Access to Azure AD Management Commands

 

## Defense

1. Implement strong password policies and multi-factor authentication to prevent credential theft

1. Monitor administrative unit changes for suspicious activity

1. Restrict access to administrative units to only those who require it

 

## Objectives

1. Create, modify, or delete administrative units in Azure Active Directory

1. Escalate privileges to gain access to sensitive data or systems

 

# Instructions

1. Fill in the details for multiple commands, instruction fields, and explain the arguments of the command in detail.

 



**Code**: [[PS AzureAD> Get-AzureADMSAdministrativeUnit -Id <I]]



> 



**Command** ([[Retrieve administrative units in Azure AD]]):

```bash
Get-AzureADMSAdministrativeUnit -Id <ID>
```





**Command** ([[Retrieve administrative unit members in Azure AD]]):

```bash
Get-AzureADMSAdministrativeUnitMember -Id <ID>
```





**Command** ([[Retrieve scoped role membership in Azure AD]]):

```bash
Get-AzureADMSScopedRoleMembership -Id <ID> | fl
```





**Command** ([[Retrieve directory role in Azure AD]]):

```bash
Get-AzureADDirectoryRole -ObjectId <RoleId>
```





**Command** ([[Retrieve user in Azure AD]]):

```bash
Get-AzureADUser -ObjectId <RoleMemberInfo.Id> | fl
```





**Command** ([[Create a new secure string object]]):

```bash
$password = "Password" | ConvertToSecureString -AsPlainText -Force
```





**Command** ([[Set user password in Azure AD]]):

```bash
(Get-AzureADUser -All $true | ?{$_.UserPrincipalName -eq "<Username>@<TENANT NAME>.onmicrosoft.com"}).ObjectId | SetAzureADUserPassword -Password $Password -Verbose
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Protocol Tunneling|T1572 - Protocol Tunneling]]

## Commands Used

- [[Create a new secure string object]]
- [[Retrieve administrative unit members in Azure AD]]
- [[Retrieve administrative units in Azure AD]]
- [[Retrieve directory role in Azure AD]]
- [[Retrieve scoped role membership in Azure AD]]
- [[Retrieve user in Azure AD]]
- [[Set user password in Azure AD]]

## Tags

- [[Administrative Unit]]
- [[Cloud - Azure]]


