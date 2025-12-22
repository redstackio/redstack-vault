---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - az-powershell
  - cloud-azure
  - enumerate-tenant-with-az-powershell
  - enumeration
commands:
  - '[[commands/connect-az-account-with-creds]]'
  - '[[commands/get-az-resource]]'
  - '[[commands/get-az-role-assignment-for-user]]'
  - '[[commands/get-az-vm-formatted]]'
  - '[[commands/get-az-web-app-exclude-functions]]'
  - '[[commands/get-az-function-app]]'
  - '[[commands/get-az-storage-account-formatted]]'
  - '[[commands/get-az-key-vault]]'
tools:
  - '[[tools/az-powershell-module]]'
validated: true
---

# Azure Tenant Enumeration with Az PowerShell (Creds)

## Summary

This procedure uses the Az PowerShell module to connect to an Azure tenant with valid credentials and enumerate key resources such as virtual machines, storage accounts, web apps, function apps, key vaults, role assignments, and general resources. It enables discovery of the tenant's infrastructure, which can reveal potential attack paths or unauthorized assets for red teaming or security assessments.

## Description

Azure Tenant Enumeration with Az PowerShell involves authenticating to an Azure Active Directory (AAD) tenant using provided credentials and querying the Azure Resource Manager (ARM) API via PowerShell cmdlets to list discoverable resources. This technique is applicable in cloud environments where an attacker has obtained valid user credentials, allowing them to map the tenant's resource landscape without needing elevated privileges. In a red team scenario, this helps identify high-value targets like key vaults for credential theft or VMs for lateral movement. Security professionals can use it to audit for shadow IT or misconfigurations. The procedure assumes the Az module is installed and focuses on non-interactive authentication to minimize detection.

## Requirements

1. Valid Azure AD credentials (username and password) for a user in the target tenant.
2. Az PowerShell module installed on a system with PowerShell 5.1 or later (Windows recommended for native support).
3. Network access to Azure endpoints (no proxy issues).
4. PowerShell execution policy set to allow script execution (e.g., Set-ExecutionPolicy RemoteSigned).

## Defense

- Restrict Azure AD access with least privilege principles and just-in-time access.
- Enable multi-factor authentication (MFA) and conditional access policies to block legacy authentication.
- Monitor Azure AD sign-ins and PowerShell activity via Microsoft Sentinel or Azure Monitor for anomalous queries (e.g., Get-AzResource from unfamiliar IPs).
- Use Azure Policy to enforce resource tagging and auditing; disable unused service principals.

## Objectives

1. Authenticate to the Azure tenant and establish a session.
2. Enumerate all discoverable resources to map the tenant's attack surface.
3. Identify role assignments and sensitive assets like key vaults for further exploitation.
4. Validate enumeration output to confirm access level and resource visibility.

## Instructions

### Step 1: Install and Import Az PowerShell Module

**Context**: Ensure the Az module is available; this step prepares the environment for authentication and enumeration. If already installed, skip to import.

**Command** ([[tools/az-powershell-module]]):

First, install if needed:
```powershell
Install-Module -Name Az -AllowClobber -Scope CurrentUser
```

Then import:
```powershell
Import-Module Az
```

> This installs the module from PowerShell Gallery and imports it into the session. Expected output: No errors, module version displayed (e.g., Az 10.x.x). Why: The Az module provides the necessary cmdlets for Azure interactions.

### Step 2: Connect to Azure Account

**Context**: Authenticate using the provided credentials to establish a session with the target tenant. This is the entry point for all subsequent enumerations.

**Command** ([[commands/connect-az-account-with-creds]]):
```powershell
$passwd = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("$_USERNAME@$_TENANT_NAME.onmicrosoft.com", $passwd)
Connect-AzAccount -Credential $creds
```

> This creates a secure credential object and connects to Azure. Expected output: JSON response with tenant ID, subscription ID, and user details (e.g., {"tenantId": "...", "user": {"name": "..."}}). If MFA is required, it will prompt or fail. Why: Establishes the authenticated context needed for resource queries; decision point: If connection fails, check credentials or MFA enforcement.

### Step 3: List All Azure Resources

**Context**: Retrieve a comprehensive list of all resources in the tenant to get an overview of the infrastructure.

**Command** ([[commands/get-az-resource]]):
```powershell
Get-AzResource
```

> This queries ARM for all resources visible to the authenticated user. Expected output: Table or list of resources with Name, ResourceType, Location, etc. (e.g., ResourceName : myVM, ResourceType : Microsoft.Compute/virtualMachines). Why: Provides a high-level map; pipe to | Export-Csv for analysis if needed.

### Step 4: List Role Assignments for the User

**Context**: Enumerate permissions assigned to the authenticated user to understand access scope.

**Command** ([[commands/get-az-role-assignment-for-user]]):
```powershell
Get-AzRoleAssignment -SignInName "$_USERNAME@$_TENANT_NAME.onmicrosoft.com"
```

> This lists RBAC assignments. Expected output: Table with RoleDefinitionName (e.g., Contributor), Scope, etc. Why: Reveals privilege level; if Owner or Contributor, broader enumeration is possible.

### Step 5: List Virtual Machines

**Context**: Identify compute resources for potential lateral movement or exploitation.

**Command** ([[commands/get-az-vm-formatted]]):
```powershell
Get-AzVM | Format-List
```

> This retrieves VM details in list format. Expected output: Properties like Name, Location, VMSize, ProvisioningState (e.g., Name : myVM, Location : eastus). Why: VMs often host sensitive data; check for public IPs.

### Step 6: List Web Apps (Excluding Functions)

**Context**: Discover web applications for potential injection or misconfiguration testing.

**Command** ([[commands/get-az-web-app-exclude-functions]]):
```powershell
Get-AzWebApp | Where-Object {$_.Kind -notmatch "functionapp"}
```

> Filters App Services to exclude Function Apps. Expected output: List of web apps with Name, State, Location. Why: Web apps may expose APIs; separate from functions for targeted enumeration.

### Step 7: List Function Apps

**Context**: Enumerate serverless functions for code execution vectors.

**Command** ([[commands/get-az-function-app]]):
```powershell
Get-AzFunctionApp
```

> Retrieves Function App details. Expected output: Names and plans (e.g., Name : myFunctionApp). Why: Functions can be invoked remotely if misconfigured.

### Step 8: List Storage Accounts

**Context**: Identify storage for data exfiltration opportunities.

**Command** ([[commands/get-az-storage-account-formatted]]):
```powershell
Get-AzStorageAccount | Format-List
```

> Lists storage accounts in detail. Expected output: AccountName, Kind, Location, Sku (e.g., AccountName : mystorage). Why: Check for public blobs or keys.

### Step 9: List Key Vaults

**Context**: Target secrets management for credential dumping.

**Command** ([[commands/get-az-key-vault]]):
```powershell
Get-AzKeyVault
```

> Retrieves key vaults. Expected output: VaultName, Location, AccessPolicies. Why: If accessible, proceed to Get-AzKeyVaultSecret; high-value target.

### Step 10: Export and Analyze Results

**Context**: Save outputs for offline analysis; optional but recommended for large tenants.

Use PowerShell export:
```powershell
Get-AzResource | Export-Csv -Path resources.csv
```

> Aggregates data. Expected output: CSV files populated. Why: Facilitates parsing and reporting; decision point: If no resources found, user lacks permissions—escalate or pivot.
