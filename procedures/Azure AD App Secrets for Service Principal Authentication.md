---
id: 19cbb75b-4b2e-4269-9c79-0388c7026731
name: Azure AD App Secrets for Service Principal Authentication
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.395914+00:00'
updated_at: '2023-05-24T21:56:17.514673+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Valid Accounts|T1078 - Valid Accounts]]'
platforms:
- Cloud
tags:
- '[[Add credentials to all Enterprise Applications]]'
- '[[Application Registration]]'
- '[[Cloud - Azure]]'
commands:
- '[[Add secrets]]'
- '[[Use secrets to authenticate as Service Principal]]'
---

# Azure AD App Secrets for Service Principal Authentication

**Status**: ✓ Verified

## Summary

This procedure allows the user to add Azure AD App Secrets for Service Principal authentication to all Enterprise Applications. This can be used for initial access by an attacker who has valid credentials or through brute force attacks. The technical explanation is that the Azure AD App Secret is a

## Description

# Description

This procedure allows the user to add Azure AD App Secrets for Service Principal authentication to all Enterprise Applications. This can be used for initial access by an attacker who has valid credentials or through brute force attacks. The technical explanation is that the Azure AD App Secret is a password that is used by the application to authenticate with Azure AD. This allows the application to access resources in Azure AD that are assigned to the application. The business value of this procedure is that it allows for easier management of credentials for all Enterprise Applications.

## Requirements

1. Azure PowerShell installed on your local machine

1. An existing Azure AD application for which a secret needs to be added

1. Valid GraphToken for the Azure AD application

1. Tenant ID, App ID, and Secret/Password for the Azure AD application

## Defense

1. Ensure that secrets are stored and used securely, avoiding clear text wherever possible

1. Validate the identities before adding secrets or authenticating as Service Principal

1. Regularly rotate Azure AD application secrets and maintain secure access control

## Objectives

1. Securely add an Azure AD application secret using PowerShell

1. Use the application secret to authenticate as a Service Principal

# Instructions

*<u>Overv*iew</u>

**Code**: [[# Add secrets
PS > . C:\Tools\Add-AzADAppSecret.ps]]

> Ensure that these commands are executed in a secure environment to  prevent unauthorized access to Azure resources. Regularly review and  update your security measures to keep your Azure environment safe.

## Steps

1. To add secrets for Azure AD App and authenticate as Service Principal using those secrets, follow the below instructions:

**Command** ([[Add secrets]]):

```bash
# Add secrets
PS > . C:\Tools\Add-AzADAppSecret.ps1
PS > Add-AzADAppSecret -GraphToken $graphtoken -Verbose

```

**Command** ([[Use secrets to authenticate as Service Principal]]):

```powershell
PS > $password = ConvertTo-SecureString '<SECRET/PASSWORD>' -AsPlainText -Force
PS > $creds = New-Object System.Management.Automation.PSCredential('<AppID>', $password)
PS > Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Add secrets]]
- [[Use secrets to authenticate as Service Principal]]

## Tags

- [[Add credentials to all Enterprise Applications]]
- [[Application Registration]]
- [[Cloud - Azure]]
