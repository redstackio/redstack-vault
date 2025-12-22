---
id: eb801578-0f3f-4f94-bc3a-21b01c8c0e15
name: azure-ad-enumeration-using-powershell-with-credentials
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.913837+00:00'
updated_at: '2023-05-23T19:34:10.735036+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
platforms:
  - Cloud
tags:
  - '[[tags/AzureAD Module]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Enumerate tenant with Azure AD Powershell]]'
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/connect-azure-ad-using-credentials]]'
  - '[[commands/get-all-azure-ad-users]]'
  - '[[commands/get-azure-ad-users-userprincipalname]]'
  - '[[commands/get-all-azure-ad-groups]]'
  - '[[commands/get-all-azure-ad-devices]]'
  - '[[commands/get-global-administrator-role-members]]'
  - '[[commands/get-custom-role-definitions]]'
validated: true
---

# Azure AD Enumeration Using PowerShell with Credentials

## Summary

This procedure uses the AzureAD PowerShell module to connect to an Azure Active Directory tenant using provided credentials and enumerate key resources such as users, groups, devices, and roles. It enables discovery of account details, group memberships, and administrative privileges, which can inform further targeted attacks like spear-phishing or privilege escalation in cloud environments.

## Description

Azure AD enumeration with PowerShell involves authenticating to the target tenant via the AzureAD module and executing cmdlets to extract directory objects. This technique targets Azure AD, Microsoft's cloud-based identity and access management service, to map the organizational structure. By retrieving user principal names, group details, device registrations, and role assignments, attackers gain insights into high-value targets like global administrators. The process requires valid credentials, typically obtained through prior compromise or phishing, and assumes the account has sufficient permissions (e.g., read access to directory data). This is particularly effective in hybrid environments where on-premises Active Directory syncs with Azure AD, revealing synced accounts and permissions.

## Requirements

1. PowerShell environment (version 5.1 or later recommended).
2. AzureAD and AzureADPreview PowerShell modules installed.
3. Valid credentials for an Azure AD account with directory read permissions.
4. Network access to Azure AD endpoints (e.g., login.microsoftonline.com).

## Defense

- Implement multi-factor authentication (MFA) for all Azure AD accounts to prevent credential-based access.
- Monitor PowerShell activity via Azure AD sign-in logs and Microsoft Defender for Cloud Apps for unusual cmdlet executions or connections from unknown IPs.
- Apply the principle of least privilege by restricting directory read access to necessary roles only.
- Enable Azure AD Privileged Identity Management (PIM) to just-in-time elevate permissions and audit role assignments.

## Objectives

1. Connect to the Azure AD tenant using provided credentials.
2. Enumerate all users, groups, devices, and custom roles to identify potential targets.
3. Extract specific details like user principal names and global administrator members for targeted follow-on attacks.

## Instructions

### Step 1: Import AzureAD Modules and Set Up Credentials

**Context**: Load the required PowerShell modules and convert the password to a secure string to create a credential object. This prepares the environment for authentication without hardcoding sensitive data.

The full setup script is available in [[codes/azure-ad-full-enumeration-script]]. For modular execution, import modules manually if not already loaded.

### Step 2: Connect to Azure AD

**Context**: Authenticate to the target tenant using the credential object. This step establishes a session and verifies access to directory resources. If MFA is enabled, interactive prompts may appear; use app passwords or service principals for automation.

**Command** ([[commands/connect-azure-ad-using-credentials]]):
```powershell
$passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential("<UPN>@<TENANT>.onmicrosoft.com", $passwd)
Connect-AzureAD -Credential $creds
```

> This command prompts for confirmation if needed and outputs a welcome message indicating successful connection. Failure results in authentication errors like invalid credentials.

### Step 3: Enumerate All Azure AD Users

**Context**: Retrieve a complete list of user objects in the tenant, including attributes like display name, UPN, and object ID. This identifies all accounts for further profiling.

**Command** ([[commands/get-all-azure-ad-users]]):
```powershell
Get-AzureADUser -All $true
```

> Outputs a table of user objects. Success is indicated by a list of users without errors; pipe to Export-Csv for saving results.

### Step 4: Get User Principal Names Only

**Context**: Extract just the User Principal Names (UPNs) from all users to quickly identify email addresses for phishing or password spraying campaigns. This filters out unnecessary details for lightweight enumeration.

**Command** ([[commands/get-azure-ad-users-userprincipalname]]):
```powershell
Get-AzureADUser -All $true | Select-Object UserPrincipalName
```

> Displays a column of UPNs. Verify by checking for known domain suffixes like @tenant.onmicrosoft.com.

### Step 5: Enumerate All Azure AD Groups

**Context**: List all security and Microsoft 365 groups, including membership hints. This reveals team structures and privileged groups for lateral movement planning.

**Command** ([[commands/get-all-azure-ad-groups]]):
```powershell
Get-AzureADGroup -All $true
```

> Returns group objects with IDs, names, and types. Success: No empty results; use Get-AzureADGroupMember for deeper dives.

### Step 6: Enumerate All Azure AD Devices

**Context**: Discover registered devices (e.g., computers, mobiles) joined to the tenant. This maps the device inventory for potential persistence or remote access vectors.

**Command** ([[commands/get-all-azure-ad-devices]]):
```powershell
Get-AzureADDevice
```

> Lists device objects with IDs, display names, and OS types. Expect output for hybrid-joined devices if applicable.

### Step 7: Get Global Administrator Role Members

**Context**: Identify members of the highest-privilege role to target for escalation. This filters for the 'Global Administrator' role and lists its users.

**Command** ([[commands/get-global-administrator-role-members]]):
```powershell
Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember
```

> Outputs user objects in the role. Success: List of admins; if empty, role may not be activated.

### Step 8: Get Custom Role Definitions

**Context**: Retrieve non-built-in role definitions to understand custom permissions in the tenant. This highlights deviations from standard Azure AD roles.

**Command** ([[commands/get-custom-role-definitions]]):
```powershell
Get-AzureADMSRoleDefinition | Where-Object {$_.IsBuiltin -eq $False} | Select-Object DisplayName
```

> Shows custom role names. Verify by absence of built-in roles in output.
