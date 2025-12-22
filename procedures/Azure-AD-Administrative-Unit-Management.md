---
id: 9418fe37-bf21-4774-a70d-602afabc316a
name: Azure-AD-Administrative-Unit-Management
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:15.860141+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Protocol Tunneling|T1572 - Protocol Tunneling]]'
sub_techniques: []
tags:
  - '[[tags/Administrative Unit]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/create-secure-string-from-plaintext]]'
  - '[[commands/get-azureadms-administrative-unit]]'
  - '[[commands/get-azureadms-administrative-unit-member]]'
  - '[[commands/get-azuread-directory-role]]'
  - '[[commands/get-azureadms-scoped-role-membership]]'
  - '[[commands/get-azuread-user-by-object-id]]'
  - '[[commands/set-azuread-user-password-by-upn]]'
platforms:
  - Azure
  - Cloud
tools:
  - '[[tools/AzureAD-PowerShell-Module]]'
validated: true
---

# Azure-AD-Administrative-Unit-Management

## Summary

This procedure demonstrates how to manage administrative units in Azure Active Directory (Azure AD) using PowerShell cmdlets from the AzureAD module. Administrative units enable scoped delegation of administrative permissions, allowing control over specific users, groups, or resources. In an offensive security context, an attacker with compromised credentials can use this to discover cloud services, enumerate roles and members, and escalate privileges by modifying passwords or memberships within scoped units, facilitating lateral movement or persistence in the Azure environment.

## Description

Administrative units in Azure AD provide a way to partition the directory for delegated administration, restricting the scope of roles to specific subsets of users or devices. This procedure covers enumeration of units, members, and roles, as well as password modifications for privilege manipulation. It assumes the attacker has initial access via valid Azure AD credentials with at least read permissions on administrative units. The technique aligns with discovery of cloud infrastructure and can enable command and control through scoped access. Successful execution allows mapping of administrative boundaries, identifying high-value targets, and potentially backdooring accounts within units.

## Requirements

1. Valid Azure AD credentials with permissions to read administrative units, roles, and users (e.g., Global Reader or Directory Readers role).
2. PowerShell environment with the AzureAD module installed and connected via `Connect-AzureAD`.
3. Network access to Azure AD endpoints (no specific ports beyond standard HTTPS/443).
4. For password changes, elevated permissions like User Administrator or higher within the scoped unit.

## Defense

- Enable Azure AD Privileged Identity Management (PIM) to require just-in-time activation for administrative roles and audit all changes to administrative units.
- Implement monitoring with Azure AD logs, Microsoft Sentinel, or similar SIEM for anomalous PowerShell activity, role assignments, and password resets.
- Use Conditional Access policies to restrict administrative actions to trusted locations and devices.
- Regularly review and limit membership in administrative units to least privilege.

## Objectives

1. Enumerate administrative units, members, and scoped roles to map the Azure AD structure and identify privilege boundaries.
2. Retrieve directory roles and user details to discover high-value accounts.
3. Modify user passwords within scoped units to achieve persistence or escalation.
4. Gain insights into delegated administrations for further lateral movement.

## Instructions

### Step 1: Connect to Azure AD and Enumerate Administrative Units

**Context**: Begin by connecting to Azure AD if not already done, then retrieve a specific administrative unit by ID to understand its configuration. This step discovers the existence and details of scoped administrative boundaries.

**Command** ([[commands/get-azureadms-administrative-unit]]):
```powershell
Get-AzureADMSAdministrativeUnit -Id $_ADMIN_UNIT_ID
```

> This command fetches details of the administrative unit, including display name, description, and visibility. Replace `$_ADMIN_UNIT_ID` with the actual GUID of the unit. Expected output includes properties like `Id`, `DisplayName`, and `Memberships`. Use this to verify the unit's scope before deeper enumeration.

### Step 2: Retrieve Members of the Administrative Unit

**Context**: Once the unit is identified, list its members to discover users or groups under this scoped administration, revealing potential targets for escalation.

**Command** ([[commands/get-azureadms-administrative-unit-member]]):
```powershell
Get-AzureADMSAdministrativeUnitMember -Id $_ADMIN_UNIT_ID
```

> This retrieves a list of members (users, groups) in the unit. The `$_ADMIN_UNIT_ID` parameter specifies the unit's GUID. Expected output is a collection of member objects with IDs and types. Pipe to `Format-List` for readability if needed.

### Step 3: Enumerate Scoped Role Memberships

**Context**: Identify role assignments within the administrative unit to understand delegated permissions and potential privilege paths.

**Command** ([[commands/get-azureadms-scoped-role-membership]]):
```powershell
Get-AzureADMSScopedRoleMembership -Id $_MEMBERSHIP_ID | Format-List
```

> This command lists details of a specific scoped role membership by ID, showing role template and administrative unit associations. Use `$_MEMBERSHIP_ID` from prior outputs. Expected output includes `RoleDefinitionId`, `AdministrativeUnitId`, and member details in a formatted list.

### Step 4: Retrieve Directory Role Details

**Context**: Fetch information on a directory role to map global or scoped permissions, aiding in identifying escalation opportunities.

**Command** ([[commands/get-azuread-directory-role]]):
```powershell
Get-AzureADDirectoryRole -ObjectId $_ROLE_ID
```

> Retrieves the specified directory role by its object ID. `$_ROLE_ID` is the GUID of the role. Expected output shows role name, description, and status (e.g., enabled). This helps correlate roles with administrative units.

### Step 5: Get User Details by Object ID

**Context**: Look up a specific user from role or membership outputs to gather attributes like UPN, which can be used for targeted modifications.

**Command** ([[commands/get-azuread-user-by-object-id]]):
```powershell
Get-AzureADUser -ObjectId $_USER_ID | Format-List
```

> Fetches user details using the object ID from previous steps. `$_USER_ID` is the user's GUID. Expected output includes `UserPrincipalName`, `DisplayName`, and other attributes in a formatted list.

### Step 6: Create Secure String for Password

**Context**: Prepare a secure string representation of a new password for use in modifications, ensuring secure handling in PowerShell.

**Command** ([[commands/create-secure-string-from-plaintext]]):
```powershell
$password = "$_NEW_PASSWORD" | ConvertToSecureString -AsPlainText -Force
```

> Converts a plaintext password to a secure string. Replace `$_NEW_PASSWORD` with the desired password. Expected output is a `SecureString` object stored in `$password`, ready for use in password set operations.

### Step 7: Set User Password by UPN

**Context**: Change a user's password using their UPN to backdoor or reset access within the administrative unit, achieving persistence.

**Command** ([[commands/set-azuread-user-password-by-upn]]):
```powershell
(Get-AzureADUser -All $true | Where-Object {$_.UserPrincipalName -eq "$_USERNAME@$_TENANT.onmicrosoft.com"}).ObjectId | Set-AzureADUserPassword -Password $password -Verbose
```

> First queries all users to find the target by UPN, then pipes the ObjectId to set the password. Parameters: `$_USERNAME` (username), `$_TENANT` (tenant name), `$password` (from Step 6). Expected output confirms the password update with verbose details; success if no errors and confirmation message appears.
