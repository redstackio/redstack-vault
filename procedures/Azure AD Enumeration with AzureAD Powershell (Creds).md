---
id: eb801578-0f3f-4f94-bc3a-21b01c8c0e15
name: Azure AD Enumeration with AzureAD Powershell (Creds)
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.913837+00:00'
updated_at: '2023-05-23T19:34:10.735036+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
platforms:
- Cloud
tags:
- '[[AzureAD Module]]'
- '[[Cloud - Azure]]'
- '[[Enumerate tenant with Azure AD Powershell]]'
- '[[Enumeration]]'
commands:
- '[[Connect to AzureAD]]'
- '[[Get all Azure AD devices]]'
- '[[Get all Azure AD groups]]'
- '[[Get all Azure AD users]]'
- '[[Get all Azure AD users and select only their User Principal Name]]'
- '[[Get all custom role definitions]]'
- '[[Get all members of the Global Administrator role]]'
---

# Azure AD Enumeration with AzureAD Powershell (Creds)

**Status**: ✓ Verified

## Summary

Azure AD Enumeration with Powershell is a technique used to discover information about a target Azure tenant. This technique involves using Azure AD Powershell cmdlets to retrieve information about users, groups, devices, and roles in the target tenant. This information can be used to identify pote

## Description

# Description

Azure AD Enumeration with Powershell is a technique used to discover information about a target Azure tenant. This technique involves using Azure AD Powershell cmdlets to retrieve information about users, groups, devices, and roles in the target tenant. This information can be used to identify potential targets, gain a better understanding of the target environment, and plan further attacks.

From a technical perspective, this technique involves using Powershell to connect to the target Azure tenant and retrieve information about the tenant's users, groups, devices, and roles. This can be done by using cmdlets such as Get-AzureADUser, Get-AzureADGroup, Get-AzureADDevice, and Get-AzureADDirectoryRole.

From a business value perspective, this technique can help an attacker identify high-value targets within an organization and plan further attacks, such as spear-phishing or password spraying.

## Requirements

1. Access to a Powershell environment

1. Credentials for connecting to the target Azure tenant

## Defense

1. Implement multi-factor authentication for all accounts in the Azure tenant

1. Monitor for suspicious Powershell activity, such as unusual cmdlet usage or connections to unknown tenants

1. Enforce the principle of least privilege by limiting access to sensitive information in the Azure tenant

## Objectives

1. Enumerate users, groups, devices, and roles in an Azure AD tenant

1. Identify potential targets for further attacks

# Instructions

1. To retrieve information about Azure AD users, groups, devices and roles, run the following commands in PowerShell:

**Code**: [[Import-Module C:\Tools\AzureAD\AzureAD.psd1
Import]]

> The AzureAD PowerShell module provides cmdlets (commands) that allow  users/administrators to automate tasks related to user and group management,  application registration, role-based access control, authentication  settings, and more within Azure AD.

**Command** ([[Connect to AzureAD]]):

```bash
Import-Module C:\Tools\AzureAD\AzureAD.psd1
Import-Module C:\Tools\AzureADPreview\AzureADPreview.psd1

# Convert password to secure string
$passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force

# Create credentials object
$creds = New-Object System.Management.Automation.PSCredential("test@<TENANT NAME>.onmicrosoft.com", $passwd)

# Connect to Azure AD
Connect-AzureAD -Credential $creds
```

**Command** ([[Get all Azure AD users]]):

```bash
Get-AzureADUser -All $true
```

**Command** ([[Get all Azure AD users and select only their User Principal Name]]):

```bash
Get-AzureADUser -All $true | select UserPrincipalName
```

**Command** ([[Get all Azure AD groups]]):

```bash
Get-AzureADGroup -All $true
```

**Command** ([[Get all Azure AD devices]]):

```bash
Get-AzureADDevice
```

**Command** ([[Get all members of the Global Administrator role]]):

```bash
Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember
```

**Command** ([[Get all custom role definitions]]):

```bash
Get-AzureADMSRoleDefinition | ?{$_.IsBuiltin -eq $False} | select DisplayName
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[Connect to AzureAD]]
- [[Get all Azure AD devices]]
- [[Get all Azure AD groups]]
- [[Get all Azure AD users]]
- [[Get all Azure AD users and select only their User Principal Name]]
- [[Get all custom role definitions]]
- [[Get all members of the Global Administrator role]]

## Tags

- [[AzureAD Module]]
- [[Cloud - Azure]]
- [[Enumerate tenant with Azure AD Powershell]]
- [[Enumeration]]
