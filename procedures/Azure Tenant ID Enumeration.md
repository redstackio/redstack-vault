---
id: 24504543-c4ab-4c7c-9579-ce03e4dbce58
name: Azure Tenant ID Enumeration
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.066249+00:00'
updated_at: '2023-05-23T17:03:22.734578+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
platforms:
- Cloud
tags:
- '[[Active Directory Federation Services]]'
- '[[Cloud - Azure]]'
- '[[Enumerate manually]]'
- '[[Enumeration]]'
- '[[Tenant ID]]'
commands:
- '[[Get Tenant Realm Information]]'
- '[[Get the Tenant ID from AzureAD]]'
- '[[Get User Realm Information]]'
---

# Azure Tenant ID Enumeration

**Status**: ✓ Verified

## Summary

Azure Tenant Enumeration is the process of manually identifying the Tenant ID and Federation settings for an Azure AD/O365 environment. This procedure is typically used by attackers to gather information about the target environment, including the structure of the Azure AD/O365 environment, and the

## Description

# Description

Azure Tenant Enumeration is the process of manually identifying the Tenant ID and Federation settings for an Azure AD/O365 environment. This procedure is typically used by attackers to gather information about the target environment, including the structure of the Azure AD/O365 environment, and the users and groups that are present within it. This information can then be used to plan a more targeted attack against the environment.

To perform Azure Tenant Enumeration, an attacker would use the 'Get Tenant ID' command to obtain the Tenant ID for the target Azure environment. The 'Azure AD/O365 Federation' command can then be used to determine whether or not the target environment is federated with an external identity provider.

From a business perspective, Azure Tenant Enumeration can be used to identify potential security weaknesses in an Azure AD/O365 environment, allowing organizations to take proactive measures to secure their environment before an attacker is able to exploit any vulnerabilities.

 

## Requirements

1. Access to the Azure AD/O365 environment

 

## Defense

1. Implement multi-factor authentication for all users in the Azure AD/O365 environment

1. Monitor the Azure AD/O365 environment for suspicious activity, such as failed login attempts or unusual login locations

1. Regularly review and update the Federation settings to ensure that they are configured securely

 

## Objectives

1. Identify the Tenant ID and Federation settings for an Azure AD/O365 environment

1. Gather information about the structure of the Azure AD/O365 environment, and the users and groups that are present within it

1. Plan a more targeted attack against the environment

 

# Instructions

1. Validate the Tenant exists using an email address of the domain and is the Tenant Federated?

 



**Code**: [[https://login.microsoftonline.com/getuserrealm.srf]]



> This command provides the URLs to retrieve the user realm information for Azure AD or O365 federation. The 'instruction' field provides a step-by-step guide on how to federate your on-premises Active Directory with Azure AD or O365. The federation process involves verifying domain ownership, installing and configuring Azure AD Connect, configuring federation settings, verifying the federation configuration, and testing the federation by signing in to Azure AD or O365 using your on-premises credentials.



**Command** ([[Get User Realm Information]]):

```bash
https://login.microsoftonline.com/getuserrealm.srf?login=<USER>@<DOMAIN>&xml=1
```





**Command** ([[Get Tenant Realm Information]]):

```bash
https://login.microsoftonline.com/getuserrealm.srf?login=root@<TENANT NAME>.onmicrosoft.com&xml=1
```



2. To get the Tenant ID, run the following command or curl the urls.


 



**Code**: [[PS> Get-AzureADTenantDetail

OR

# Replace <Domain]]



> This command retrieves details about the Azure Active Directory tenant, including the Tenant ID. The Tenant ID is a unique identifier for your organization's tenant in Azure AD. It is required for various administrative tasks, such as configuring applications and assigning permissions. The command retrieves the Tenant ID by querying the Azure AD service endpoint for the tenant's OpenID Connect configuration information.





**Command** ([[Get the Tenant ID from AzureAD]]):

```bash
Get-AzureADTenantDetail
```





## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[Get Tenant Realm Information]]
- [[Get the Tenant ID from AzureAD]]
- [[Get User Realm Information]]

## Tags

- [[Active Directory Federation Services]]
- [[Cloud - Azure]]
- [[Enumerate manually]]
- [[Enumeration]]
- [[Tenant ID]]


