---
id: cf5b3de3-0cec-426d-8da9-fa731454d196
name: Azure Application Proxy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.928320+00:00'
updated_at: '2023-04-10T20:19:39.384764+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Application Proxy]]'
- '[[Cloud - Azure]]'
commands:
- '[[Enumerate applications with Proxy]]'
- '[[Find Service Principal for Finance Management System]]'
- '[[Get assigned users and groups for the specified application]]'
- '[[Run GetApplicationProxyAssignedUsersAndGroups script]]'
---

# Azure Application Proxy Enumeration

## Summary

The Azure Application Proxy Enumeration procedure is used to discover details about the Azure Application Proxy and the users/groups assigned to it. This information can be used by an attacker to gain a better understanding of the target environment and potentially identify weak points for further 

## Description

# Description

The Azure Application Proxy Enumeration procedure is used to discover details about the Azure Application Proxy and the users/groups assigned to it. This information can be used by an attacker to gain a better understanding of the target environment and potentially identify weak points for further exploitation. 

The Azure Application Proxy is a service provided by Microsoft that allows users to access on-premises web applications from anywhere and on any device. It works by creating a secure tunnel between the on-premises application and the Azure cloud, and then authenticating the user through Azure Active Directory. By enumerating these details, an attacker can gain insight into the applications that are being proxied and the users/groups that have access to them.

The business value of this procedure is that it allows administrators to assess the security of their Azure Application Proxy configuration and ensure that only authorized users have access to the on-premises applications that are being proxied.

 

## Requirements

1. Valid Azure credentials with permissions to access the Azure Application Proxy

1. Access to the Azure portal

 

## Defense

1. Ensure that only authorized users have access to the Azure Application Proxy

1. Implement Multi-Factor Authentication (MFA) for all users accessing the Azure Application Proxy

1. Regularly review and update the users and groups assigned to the Azure Application Proxy

 

## Objectives

1. Discover details about the Azure Application Proxy

1. Identify users and groups assigned to the Azure Application Proxy

 

# Instructions

1. To enumerate the application that have Proxy and their details, run the following commands:
1. Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}
2. Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq "<APPLICATION-DISPLAY-NAME>"}

To get the users and groups assigned to the application proxy, run the following commands:
1. . C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
2. Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>

 



**Code**: [[# Enumerate application that have Proxy
PS C:\Tool]]



> This command is used to enumerate the applications that have a proxy and their details. The first command retrieves all Azure AD applications with the -All parameter set to $true. It then pipes the output to a ForEach-Object loop where it tries to retrieve the application proxy details using the GetAzureADApplicationProxyApplication command. The second command retrieves the Azure AD service principal for the Finance Management System application. 

The second set of commands is used to get the users and groups assigned to the application proxy. The first command loads the GetApplicationProxyAssignedUsersAndGroups PowerShell script. The second command retrieves the users and groups assigned to the application proxy using the -ObjectId parameter.



**Command** ([[Enumerate applications with Proxy]]):

```bash
Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}
```





**Command** ([[Find Service Principal for Finance Management System]]):

```bash
Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq "Finance Management System"}
```





**Command** ([[Run GetApplicationProxyAssignedUsersAndGroups script]]):

```bash
. C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
```





**Command** ([[Get assigned users and groups for the specified application]]):

```bash
Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Enumerate applications with Proxy]]
- [[Find Service Principal for Finance Management System]]
- [[Get assigned users and groups for the specified application]]
- [[Run GetApplicationProxyAssignedUsersAndGroups script]]

## Tags

- [[Application Proxy]]
- [[Cloud - Azure]]


