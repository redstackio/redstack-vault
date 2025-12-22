---
id: 19cbb75b-4b2e-4269-9c79-0388c7026731
name: Add-Azure-AD-App-Secret-for-Service-Principal-Authentication
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.395914+00:00'
updated_at: '2023-05-24T21:56:17.514673+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - add-credentials-to-enterprise-applications
  - application-registration
  - cloud-azure
commands:
  - '[[commands/Add-AzADAppSecret-Using-GraphToken]]'
  - '[[commands/Connect-AzAccount-As-Service-Principal-Using-Secret]]'
tools: []
validated: true
---

# Add-Azure-AD-App-Secret-for-Service-Principal-Authentication

## Summary

This procedure demonstrates how to add secrets to Azure AD applications to enable service principal authentication, which can be leveraged by attackers with valid credentials for initial access, persistence, or privilege escalation in Azure environments. By creating and using application secrets, the procedure allows authentication as a service principal to access assigned Azure resources without interactive user logins.

## Description

In Azure Active Directory (Azure AD), service principals represent applications or services that need to access Azure resources. Adding a secret (a password-like credential) to an Azure AD app registration enables non-interactive authentication via the service principal. This technique is commonly used legitimately for automation but can be abused by attackers who gain access to an existing app registration or Graph API tokens. For instance, an attacker with a valid Graph token can add a secret to an enterprise application, then use it to authenticate and perform actions like resource management or data exfiltration. The procedure requires Azure PowerShell and focuses on secure secret addition and subsequent authentication, mapping to MITRE ATT&CK for valid accounts usage in cloud persistence and evasion.

## Requirements

1. Azure PowerShell module installed on the local machine (Install-Module -Name Az -AllowClobber if needed).
2. An existing Azure AD application registration with permissions to add secrets.
3. A valid Graph API access token ($graphtoken) for the Azure AD application, obtained via prior authentication or token acquisition.
4. Tenant ID, Application (App) ID, and the generated secret/password for authentication.
5. Local machine with PowerShell execution policy allowing script execution (Set-ExecutionPolicy RemoteSigned).

## Defense

- Store and handle secrets securely, using Azure Key Vault instead of plaintext storage and enabling automatic rotation.
- Implement least-privilege access: Validate and audit identities before allowing secret additions via role-based access control (RBAC).
- Monitor Azure AD sign-ins for service principal authentications, especially from unusual IPs or with new secrets; enable logging in Microsoft Defender for Cloud and set alerts for anomalous app registrations.
- Regularly rotate application secrets and certificates, and use managed identities where possible to avoid long-lived secrets.

## Objectives

1. Add a secret to an Azure AD application securely using PowerShell and a Graph token.
2. Authenticate as the service principal using the new secret to gain access to Azure resources.
3. Establish persistence or escalate privileges via valid service principal accounts in the target tenant.

## Instructions

### Step 1: Source and Execute the Add-AzADAppSecret Script

**Context**: This step loads a custom PowerShell script to add a secret to the Azure AD application using the provided Graph token. The script interacts with the Microsoft Graph API to create the secret without requiring full interactive login, enabling attackers to persist credentials in enterprise apps.

**Command** ([[commands/Add-AzADAppSecret-Using-GraphToken]]):
```powershell
. C:\Tools\Add-AzADAppSecret.ps1
Add-AzADAppSecret -GraphToken $graphtoken -Verbose
```

> The -Verbose flag provides detailed output for troubleshooting. Ensure the $graphtoken variable holds a valid bearer token with Application.ReadWrite.All permissions. This step generates a new secret value, which should be captured immediately as it won't be retrievable later.

### Step 2: Authenticate as Service Principal Using the Secret

**Context**: After adding the secret, convert it to a secure string and create credentials for non-interactive login to Azure. This allows the service principal to assume roles assigned to the app, potentially granting access to subscriptions, key vaults, or other resources.

**Command** ([[commands/Connect-AzAccount-As-Service-Principal-Using-Secret]]):
```powershell
$password = ConvertTo-SecureString '<SECRET/PASSWORD>' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('<AppID>', $password)
Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'
```

> Replace <SECRET/PASSWORD> with the output from Step 1, <AppID> with the application's client ID, and <TenantID> with the Azure tenant ID. Success connects the PowerShell session to Azure as the service principal, allowing subsequent Az cmdlet executions like Get-AzSubscription.
