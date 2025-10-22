---
id: b49a4e42-bcd1-4b67-8daf-1208f4cb96e6
name: Azure Tenant Enumeration with Az PowerShell (Creds)
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.971744+00:00'
updated_at: '2023-05-23T19:25:56.301368+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
platforms:
- Cloud
tags:
- '[[Az Powershell]]'
- '[[Cloud - Azure]]'
- '[[Enumerate tenant with Az Powershell]]'
- '[[Enumeration]]'
commands:
- '[[Connect to Azure Account]]'
- '[[List Azure Function Apps]]'
- '[[List Azure Key Vaults]]'
- '[[List Azure Resources]]'
- '[[List Azure Role Assignments]]'
- '[[List Azure Storage Accounts]]'
- '[[List Azure Virtual Machines]]'
- '[[List Azure Web Apps]]'
---

# Azure Tenant Enumeration with Az PowerShell (Creds)

**Status**: ✓ Verified

## Summary

Azure Tenant Enumeration with Az PowerShell is a technique used to discover information about an Azure tenant. This technique involves using Az PowerShell to connect to an Azure tenant and retrieve information about the resources within the tenant. An attacker can use this technique to discover the

## Description

# Description

Azure Tenant Enumeration with Az PowerShell is a technique used to discover information about an Azure tenant. This technique involves using Az PowerShell to connect to an Azure tenant and retrieve information about the resources within the tenant. An attacker can use this technique to discover the resources within an Azure tenant, which can be used to plan further attacks. This technique can also be used by security professionals to discover unauthorized resources within an Azure tenant.

To use this technique, an attacker must have valid credentials for the Azure tenant. The attacker can then use Az PowerShell to connect to the tenant and retrieve information about the resources within the tenant. The information retrieved can include virtual machines, storage accounts, and other resources.

The business value of this technique is that it allows organizations to discover unauthorized resources within their Azure tenant, which can help them to improve their security posture.

## Requirements

1. Valid credentials for the Azure tenant

1. Az PowerShell

## Defense

1. Ensure that access to the Azure tenant is restricted to authorized users only

1. Implement multi-factor authentication to prevent unauthorized access to the Azure tenant

1. Monitor Azure tenant activity for suspicious activity

## Objectives

1. Discover resources within an Azure tenant

1. Plan further attacks

1. Discover unauthorized resources within an Azure tenant

# Instructions

1. To use this command, replace the <PASSWORD> and <TENANT NAME> fields with your actual password and tenant name respectively. Then, copy and paste the entire command into a PowerShell terminal. This command will connect you to your Azure account and retrieve information about your resources.

**Code**: [[PS> $passwd = ConvertTo-SecureString "<PASSWORD>" ]]

> This command is used to connect to an Azure account using PowerShell and retrieve information about the resources in the account. The first three lines of the command create a secure password and credentials object that are used to authenticate the user. The 'Connect-AzAccount' command is then used to connect to the Azure account using the credentials. Once connected, the command retrieves information about the resources in the account using various 'Get-Az' commands. These commands retrieve information about resources such as virtual machines, web apps, function apps, storage accounts, and key vaults.

**Command** ([[Connect to Azure Account]]):

```bash
$passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("test@<TENANT NAME>.onmicrosoft.com", $passwd)
Connect-AzAccount -Credential $creds
```

**Command** ([[List Azure Resources]]):

```bash
Get-AzResource
```

**Command** ([[List Azure Role Assignments]]):

```bash
Get-AzRoleAssignment -SignInName test@<TENANT NAME>.onmicrosoft.com
```

**Command** ([[List Azure Virtual Machines]]):

```bash
Get-AzVM | fl
```

**Command** ([[List Azure Web Apps]]):

```bash
Get-AzWebApp | ?{$_.Kind -notmatch "functionapp"}
```

**Command** ([[List Azure Function Apps]]):

```bash
Get-AzFunctionApp
```

**Command** ([[List Azure Storage Accounts]]):

```bash
Get-AzStorageAccount | fl
```

**Command** ([[List Azure Key Vaults]]):

```bash
Get-AzKeyVault
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[Connect to Azure Account]]
- [[List Azure Function Apps]]
- [[List Azure Key Vaults]]
- [[List Azure Resources]]
- [[List Azure Role Assignments]]
- [[List Azure Storage Accounts]]
- [[List Azure Virtual Machines]]
- [[List Azure Web Apps]]

## Tags

- [[Az Powershell]]
- [[Cloud - Azure]]
- [[Enumerate tenant with Az Powershell]]
- [[Enumeration]]
