---
id: c0079203-1ded-4fba-b335-0ce2e6e27014
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.651569+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - '[[techniques/Active Scanning|T1595 - Active Scanning]]'
  - >-
    [[techniques/Domain Generation Algorithms|T1483 - Domain Generation
    Algorithms]]
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
sub_techniques: []
tags:
  - '[[tags/Azure Recon Tools]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/pipenv-shell-activate]]'
  - '[[commands/roadrecon-authenticate-with-credentials]]'
  - '[[commands/powerzure-create-backdoor]]'
  - '[[commands/powerzure-execute-backdoor]]'
  - '[[commands/powerzure-execute-command-on-vm]]'
  - '[[commands/powerzure-execute-msbuild-on-vm]]'
  - '[[commands/azucar-export-with-certificate-credentials]]'
  - '[[commands/azucar-export-with-certificate-and-password]]'
  - '[[commands/azucar-export-to-print-cached-creds]]'
  - '[[commands/roadrecon-gather-data]]'
  - '[[commands/powerzure-get-all-secrets]]'
  - '[[commands/powerzure-get-available-vm-disks]]'
  - '[[commands/bark-get-azure-ad-users]]'
  - '[[commands/powerzure-get-resources]]'
  - '[[commands/roadrecon-launch-gui]]'
  - '[[commands/azure-cli-login-with-credentials]]'
  - '[[commands/cd-to-stormspotter-frontend-directory]]'
  - '[[commands/azucar-resolve-tenantid-for-username]]'
  - '[[commands/powerzure-set-role-on-resource]]'
  - '[[commands/powerzure-set-subscription]]'
  - '[[commands/stormspotter-start-backend]]'
  - '[[commands/stormspotter-start-collector]]'
  - '[[commands/stormspotter-start-frontend]]'
  - '[[commands/powershell-unblock-azucar-files]]'
platforms:
  - Azure
  - Windows
tools:
  - '[[tools/BARK]]'
  - '[[tools/ROADRecon]]'
  - '[[tools/Azure-StormSpotter]]'
  - '[[tools/Azucar]]'
  - '[[tools/AzuriteExplorer]]'
  - '[[tools/MicroBurst]]'
  - '[[tools/PowerZure]]'
validated: true
---

# Azure-Reconnaissance

## Summary

This procedure outlines the use of multiple open-source tools to perform comprehensive reconnaissance on an Azure environment, including enumeration of Azure AD users, resources, subscriptions, secrets, and domain information. It enables attackers to map the cloud infrastructure, identify misconfigurations, and discover potential entry points for further exploitation in a Microsoft Azure tenant.

## Description

Azure Reconnaissance involves systematically gathering intelligence on an organization's Azure Active Directory (AAD), subscriptions, virtual machines, key vaults, and other resources using specialized tools. This procedure covers authentication methods, data collection via APIs like Microsoft Graph and Azure Resource Manager, and visualization of attack paths. It is typically used in red team engagements to simulate adversary discovery phases, helping to uncover weak permissions, exposed secrets, and trust relationships. The target environment is a Microsoft Azure cloud setup with AAD-integrated resources. Prerequisites include valid Azure credentials (user, app, or certificate-based) with read access to targeted scopes. Expected outcomes include exported reports in CSV, JSON, or graph databases for analysis.

## Requirements

1. Valid Azure AD credentials (username/password, client ID/secret, or certificate) with at least Reader role on target subscriptions.
2. Installed tools: PowerShell 5.1+, Azure CLI, Python 3.x with pipenv for some tools.
3. Network access to Azure endpoints (e.g., login.microsoftonline.com, management.azure.com).
4. Windows or Linux host for execution, with Git for submodule dependencies.

## Defense

- Implement least-privilege access controls using Azure RBAC and PIM to limit read permissions on resources.
- Enable Azure AD logging (Sign-ins, Audit logs) and monitor for anomalous API calls via Microsoft Sentinel or Azure Monitor.
- Use Azure AD Conditional Access policies to restrict authentication from unknown locations or devices.
- Regularly audit and rotate service principal credentials; disable legacy authentication methods.
- Deploy tools like Microsoft Defender for Cloud to detect enumeration attempts and unusual data exports.

## Objectives

1. Enumerate Azure AD users, groups, and applications to identify high-value targets.
2. Map Azure resources, subscriptions, and configurations to reveal misconfigurations.
3. Extract sensitive data like secrets and domain info for further exploitation planning.
4. Visualize the environment to understand trust relationships and attack paths.

## Instructions

### Step 1: Enumerate Azure AD Users with BARK

**Context**: Authenticate to Azure AD and retrieve all users via Microsoft Graph API to build a user inventory for targeting privileged accounts.

**Script** ([[codes/bark-auth-and-get-users-script]]):

Use the BARK script to handle token acquisition and user enumeration.

**Command** ([[commands/bark-get-azure-ad-users]]):
```powershell
. .\BARK.ps1
$MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com" -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com"
$MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "contoso.onmicrosoft.com"
$MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```

> This sequence imports the BARK module, obtains a refresh token using username/password, exchanges it for a Graph API access token, and fetches all AAD users with progress indication. If successful, it outputs a list of users including IDs, names, and roles.

### Step 2: Authenticate and Gather Data with ROADRecon

**Context**: Set up a virtual environment, authenticate to the tenant, collect AAD data into a local database, and optionally launch the GUI for visualization.

**Command** ([[commands/pipenv-shell-activate]]):
```bash
pipenv shell
```

**Command** ([[commands/roadrecon-authenticate-with-credentials]]):
```bash
roadrecon auth -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
```

**Command** ([[commands/roadrecon-gather-data]]):
```bash
roadrecon gather
```

**Command** ([[commands/roadrecon-launch-gui]]):
```bash
roadrecon gui
```

> Activate the pipenv environment first, then authenticate using credentials. Gather populates the local SQLite database with AAD objects like users, groups, and apps. Launch the GUI to query and visualize data. Success is indicated by populated database files and no auth errors.

### Step 3: Set Up Azure StormSpotter for Resource Mapping

**Context**: Run backend, frontend, and collector sessions to ingest Azure data into a Neo4j graph database for BloodHound-style analysis.

**Script** ([[codes/stormspotter-setup-sessions-script]]):

Follow the multi-session setup in the script.

**Command** ([[commands/pipenv-shell-activate]]):
```bash
pipenv shell
```

**Command** ([[commands/stormspotter-start-backend]]):
```bash
python ssbackend.pyz
```

**Command** ([[commands/cd-to-stormspotter-frontend-directory]]):
```bash
cd C:\Tools\stormspotter\frontend\dist\spa\
```

**Command** ([[commands/stormspotter-start-frontend]]):
```bash
quasar.cmd serve -p 9091 --history
```

**Command** ([[commands/azure-cli-login-with-credentials]]):
```bash
az login -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
```

**Command** ([[commands/stormspotter-start-collector]]):
```bash
python C:\Tools\stormspotter\stormcollector\sscollector.pyz cli
```

> In separate sessions: Start backend (Neo4j), frontend (web UI on localhost:9091), and collector (after az login) to pull data. Access UI with neo4j/BloodHound credentials. Expected: Graph database populated with Azure entities.

### Step 4: Export Azure Configurations with Azucar

**Context**: Unblock scripts, then export subscription data using cached creds or certificates to identify risks.

**Command** ([[commands/powershell-unblock-azucar-files]]):
```powershell
Get-ChildItem -Recurse c:\Azucar_V10 | Unblock-File
```

**Command** ([[commands/azucar-export-to-print-cached-creds]]):
```powershell
.\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT
```

**Command** ([[commands/azucar-export-with-certificate-credentials]]):
```powershell
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```

**Command** ([[commands/azucar-export-with-certificate-and-password]]):
```powershell
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```

**Command** ([[commands/azucar-resolve-tenantid-for-username]]):
```powershell
.\Azucar.ps1 -ResolveTenantUserName user@company.com
```

> Unblock files to avoid execution policy issues. Export using cached creds for quick print output or certificates for file exports. Resolve TenantID if needed. Outputs include risk assessments in specified formats.

### Step 5: Review Subscriptions with AzuriteExplorer

**Context**: Initialize dependencies and review Azure RM subscriptions for resource enumeration.

**Script** ([[codes/azuriteexplorer-setup-and-review-script]]):

Execute the setup and review commands from the script.

> Import modules after git submodules, then run review functions to list subscriptions and custom resources. Useful for initial scoping.

### Step 6: Gather Domain Info with MicroBurst

**Context**: Import modules and collect domain-related Azure data for trust discovery.

**Script** ([[codes/microburst-get-azure-domain-info]]):

Run the import and Get-AzureDomainInfo from the script.

> Outputs verbose details on domains, services, and configs to the specified folder. Aids in identifying federated trusts.

### Step 7: Perform Role-Based Recon with PowerZure

**Context**: Set subscription, then use role-specific commands to enumerate and interact with resources.

**Command** ([[commands/powerzure-set-subscription]]):
```powershell
$ ipmo .\PowerZure.psm1 ; Set-Subscription -Id [idgoeshere]
```

**Command** ([[commands/powerzure-get-resources]]):
```powershell
Get-Resources
```

**Command** ([[commands/powerzure-get-all-secrets]]):
```powershell
Get-AllSecrets
```

**Command** ([[commands/powerzure-get-available-vm-disks]]):
```powershell
Get-AvailableVMDisks ; Get-VMDisk
```

**Command** ([[commands/powerzure-set-role-on-resource]]):
```powershell
Set-Role -Role Contributor -User test@contoso.com -Resource Win10VMTest
```

**Script** ([[codes/powerzure-role-based-commands-script]]):

Reference Reader/Contributor commands in the script for enumeration.

> Import PowerZure, set subscription, then run gets for resources/secrets/disks. Higher roles enable role assignment or backdoor creation. Expected: Detailed resource inventories.
