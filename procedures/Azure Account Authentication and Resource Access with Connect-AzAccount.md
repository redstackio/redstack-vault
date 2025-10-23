---
id: 6691e7e9-a931-4621-b34c-ef5f5767d533
name: Azure Account Authentication and Resource Access with Connect-AzAccount
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.293900+00:00'
updated_at: '2023-05-30T13:47:18.352959+00:00'
tags:
- '[[Cloud - Azure]]'
- '[[Token from Managed Identity]]'
- '[[Use Tokens]]'
commands:
- '[[Connect to Azure Account with Access Token]]'
- '[[Connect to Azure Account with Access Token and Graph Token]]'
- '[[Connect to AzureAD]]'
- '[[Connect to AzureAD module]]'
- '[[Get Azure Resource]]'
- '[[Set AzureAD Token]]'
---

# Azure Account Authentication and Resource Access with Connect-AzAccount

**Status**: ✓ Verified

## Summary

Azure Managed Identity is a feature that provides Azure services with an automatically managed identity in Azure Active Directory (Azure AD). This feature enables you to authenticate to services that support Azure AD authentication without having to insert credentials into your code. This procedure

## Description

# Description

Azure Managed Identity is a feature that provides Azure services with an automatically managed identity in Azure Active Directory (Azure AD). This feature enables you to authenticate to services that support Azure AD authentication without having to insert credentials into your code. This procedure explains how to retrieve an access token from the Managed Identity and use it to connect to Azure services. The token can also be used to retrieve a Graph token which can be used to access the Microsoft Graph API. By using this procedure, an attacker can obtain access to Azure services and data without the need for a username and password. This procedure can be used to escalate privileges and move laterally within an Azure environment.

 

## Requirements

1. PowerShell is installed and accessible.

1. The Az module is installed and up-to-date.

1. Valid access tokens (access token, graph access token) are available.

1. Proper permissions are granted to interact with Azure resources.

 

## Defense

1. Safeguard and limit the access to access tokens and account credentials.

1. Regularly monitor logs and audit trails for any suspicious activities.

1. Implement role-based access control (RBAC) to control access to Azure resources.

 

## Objectives

1. Authenticate to an Azure account using an access token.

1. Authenticate to an Azure account using an access token and a graph access token.

1. Access Azure resources using the authenticated account.

1. Troubleshoot common errors related to resource access.

 

# Instructions

*<u>Overv*iew</u>



**Code**: [[# Login using an Access Token
PS C:\Tools> $token ]]



> If the connection is not successful, an error message will be displayed.

## 

## Steps

1. Authenticate to AzureAD using Access token and Graph Access Token



**Command** ([[Connect to Azure Account with Access Token]]):

```powershell
PS C:\Tools> $token = 'eyJ0e..'
PS C:\Tools> Connect-AzAccount -AccessToken $token -AccountId <ACCOUNT-ID>

```





**Command** ([[Connect to Azure Account with Access Token and Graph Token]]):

```powershell
PS C:\Tools> $token = <TOKEN>
PS C:\Tools> $graphaccesstoken = <GRAPHTOKEN>
PS C:\Tools> Connect-AzAccount -AccessToken $token -GraphAccessToken $graphaccesstoken -AccountId <ACCOUNT-ID>

```





**Command** ([[Get Azure Resource]]):

```powershell
PS C:\Tools> Get-AzResource

```





**2. (Optional) To connect to Azure Active Directory using AzureAD PowerShell, execute the following commands:**

 



**Code**: [[# Import the AzureAD module by running the 'Import]]



>  If the connection is not successful, an error message will be displayed.



**Command** ([[Connect to AzureAD module]]):

```bash
Import-Module C:\Tools\AzureAD\AzureAD.psd1
```





**Command** ([[Set AzureAD Token]]):

```bash
$AADToken = 'eyJ0…'
```





**Command** ([[Connect to AzureAD]]):

```bash
Connect-AzureAD -AadAccessToken $AADToken -TenantId <TENANT-ID> -AccountId <ACCOUNT-ID>
```



## Commands Used

- [[Connect to Azure Account with Access Token]]
- [[Connect to Azure Account with Access Token and Graph Token]]
- [[Connect to AzureAD]]
- [[Connect to AzureAD module]]
- [[Get Azure Resource]]
- [[Set AzureAD Token]]

## Tags

- [[Cloud - Azure]]
- [[Token from Managed Identity]]
- [[Use Tokens]]


