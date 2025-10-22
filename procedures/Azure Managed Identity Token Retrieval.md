---
id: c152d40e-9dbf-4c1f-84b2-370cb051e6e4
name: Azure Managed Identity Token Retrieval
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.259029+00:00'
updated_at: '2023-05-24T07:56:40.841664+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
platforms:
- Cloud
tags:
- '[[App Service]]'
- '[[Cloud - Azure]]'
- '[[Get Tokens]]'
- '[[Kudu]]'
- '[[Managed Identity]]'
- '[[powershell]]'
- '[[Token from Managed Identity]]'
commands:
- '[[Get Azure CLI Tokens]]'
---

# Azure Managed Identity Token Retrieval

**Status**: ✓ Verified

## Summary

Azure Managed Identity Token Retrieval is a technique used to obtain access tokens for Azure CLI and Az. This technique is useful in cases where a user needs to authenticate to Azure services without having to provide their own credentials. Managed identities are a secure way to authenticate to Azu

## Description

# Description

Azure Managed Identity Token Retrieval is a technique used to obtain access tokens for Azure CLI and Az. This technique is useful in cases where a user needs to authenticate to Azure services without having to provide their own credentials. Managed identities are a secure way to authenticate to Azure services, and this technique allows users to leverage this security feature. By retrieving tokens from managed identities, users can perform actions on Azure resources that they have been granted permission to access.

To retrieve tokens from a managed identity, the user must have permissions to access the Azure resource that the managed identity is assigned to. Once the user has access to the resource, they can retrieve the access token by running the appropriate command. This token can then be used to authenticate to Azure services.

## Requirements

1. Access to the Azure resource that the managed identity is assigned to

## Defense

1. Ensure that users have the least amount of privileges necessary to perform their tasks

1. Use Azure AD Conditional Access policies to restrict access to Azure resources

1. Enable Azure AD Multi-Factor Authentication (MFA) to add an extra layer of security to user authentication

## Objectives

1. Retrieve access tokens for Azure CLI and Az without having to provide user credentials

1. Leverage the security of managed identities to authenticate to Azure services

1. Perform actions on Azure resources that the user has been granted permission to access

# Instructions

1. To get access tokens for Azure CLI and Az, use the following commands from an Azure Resource that has a Managed Identity assigned to it.
- For Azure CLI: az account get-access-token or az account get-access-token --resource-type aad-graph
- For Az: (Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token

Note: The lifetime of a Primary Refresh Token is 14 days.

**Code**: [[# az cli - get tokens 
az account get-access-token]]

> The access tokens are used to authenticate and authorize requests to Azure resources. The commands provided will retrieve access tokens for Azure CLI and Az. The first command is for Azure CLI and it can be used to get the access token for a specific resource type, in this case aad-graph. The second command is for Az and it retrieves the access token for the specified resource URL. It's important to note that the lifetime of a Primary Refresh Token is 14 days and it should be refreshed before it expires to avoid any disruptions in access to Azure resources.

**Command** ([[Get Azure CLI Tokens]]):

```bash
# az cli - get tokens 
az account get-access-token 
az account get-access-token --resource-type aad-graph
# or Az
(Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token
# or from a managed identity using IDENTITY_HEADER and IDENTITY_ENDPOINT
```

2a. (Optional) Get access token from KUDU Service - System Assigned Managed Identity

**Code**: [[# or KUDU Debug Console Powershell - System Assign]]

2b. (Optional) Get access token from Kudu Service - User Assigned Managed Identity

**Code**: [[# or KUDU Debug Console Powershell - User Assigned]]

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[Get Azure CLI Tokens]]

## Tags

- [[App Service]]
- [[Cloud - Azure]]
- [[Get Tokens]]
- [[Kudu]]
- [[Managed Identity]]
- [[powershell]]
- [[Token from Managed Identity]]
