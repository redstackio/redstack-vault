---
type: procedure
description: >-
  Enumerate Azure AD applications configured with Application Proxy and identify
  assigned users and groups to discover access patterns in the target
  environment.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - azure
  - application-proxy
  - discovery
  - cloud
commands:
  - '[[commands/enumerate-azure-ad-applications-with-proxy]]'
  - '[[commands/find-azure-ad-service-principal-by-display-name]]'
  - '[[commands/import-get-application-proxy-assigned-users-and-groups-script]]'
  - '[[commands/get-application-proxy-assigned-users-and-groups-by-object-id]]'
platforms:
  - Azure AD
tools: []
validated: true
---

# Azure Application Proxy Enumeration

## Summary

This procedure enumerates Azure Active Directory (Azure AD) applications configured with Application Proxy, retrieves details such as display names and Object IDs, identifies associated service principals, and lists assigned users and groups. It helps attackers map the target organization's proxied on-premises applications and access controls, potentially revealing misconfigurations or high-value targets for lateral movement.

## Description

Azure Application Proxy enables secure remote access to on-premises web applications via Azure AD authentication. By enumerating these configurations, an attacker with compromised Azure credentials can discover which internal applications are exposed externally, who has access (users/groups), and related service principals. This discovery aids in identifying weak points, such as overly permissive assignments or legacy applications. The procedure assumes access to the AzureAD PowerShell module and uses built-in cmdlets along with a custom script for detailed user/group enumeration. It maps to MITRE ATT&CK's Cloud Service Discovery technique, focusing on Azure environments.

## Requirements

1. Valid Azure AD credentials with at least read access to applications and service principals (e.g., Global Reader or Application Reader role).
2. PowerShell environment with the AzureAD module installed (Install-Module AzureAD if needed).
3. Access to run PowerShell scripts; the custom GetApplicationProxyAssignedUsersAndGroups.ps1 script must be available (download or create based on Azure AD Graph API queries for app assignments).
4. Network connectivity to Azure endpoints.

## Defense

- Implement least privilege access: Restrict application read permissions to necessary roles and enable Privileged Identity Management (PIM).
- Enable Azure AD logging and monitor for anomalous enumeration queries via Microsoft Sentinel or Azure Monitor.
- Use Conditional Access policies to enforce MFA and device compliance for administrative accounts.
- Regularly audit Application Proxy configurations and assigned users/groups using Azure AD reports.

## Objectives

1. Identify all Azure AD applications using Application Proxy and their identifiers.
2. Locate service principals associated with specific proxied applications.
3. Retrieve users and groups assigned to Application Proxy applications to map access.
4. Uncover potential entry points for further exploitation in hybrid environments.

## Instructions

### Step 1: Enumerate Azure AD Applications with Application Proxy

**Context**: This step retrieves all Azure AD applications and filters those configured with Application Proxy by attempting to query proxy details. It outputs display names and Object IDs for proxied apps, helping identify exposed on-premises resources.

**Command** ([[commands/enumerate-azure-ad-applications-with-proxy]]):
```powershell
Get-AzureADApplication -All $true | ForEach-Object {try {Get-AzureADApplicationProxyApplication -ObjectId $_.ObjectID; $_.DisplayName; $_.ObjectID} catch {}}
```

> This pipeline lists all applications and attempts proxy retrieval; errors are caught silently to continue processing. Run this in a PowerShell session connected to Azure AD (Connect-AzureAD first if not already).

**Expected Output**: A list of proxied applications, e.g.,
```
ExternalUrl              : https://financeapp-contoso.msappproxy.net
InternalUrl              : http://internal-finance
DisplayName              : Finance Management System
ObjectId                 : 12345678-1234-1234-1234-123456789abc
```
Followed by display names and Object IDs for matching apps.

### Step 2: Find Service Principal by Display Name

**Context**: Once a target application is identified (e.g., from Step 1), query for its service principal to get additional details like app roles or credentials, which may reveal integration points.

**Command** ([[commands/find-azure-ad-service-principal-by-display-name]]):
```powershell
Get-AzureADServicePrincipal -All $true | Where-Object {$_.DisplayName -eq "<APPLICATION-DISPLAY-NAME>"}
```

> Replace <APPLICATION-DISPLAY-NAME> with the name from Step 1, such as "Finance Management System". This filters all service principals to find the matching one.

**Expected Output**: Details of the service principal, e.g.,
```
ObjectId                                   DisplayName             AppId
--------                                   -----------             -----
12345678-1234-1234-1234-123456789abc       Finance Management System 87654321-4321-4321-4321-cba987654321
```

### Step 3: Import the Custom Enumeration Script

**Context**: Load the custom PowerShell script that defines the Get-ApplicationProxyAssignedUsersAndGroups function, which queries Azure AD for assignments beyond standard cmdlets.

**Command** ([[commands/import-get-application-proxy-assigned-users-and-groups-script]]):
```powershell
. C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
```

> Ensure the script is placed in C:\Tools\ (or adjust path). This script typically uses Azure AD Graph API to fetch app role assignments for proxy apps.

**Expected Output**: No output if successful; the function becomes available in the session. Verify with Get-Command Get-ApplicationProxyAssignedUsersAndGroups.

### Step 4: Get Assigned Users and Groups by Object ID

**Context**: Use the loaded function to retrieve users and groups assigned to the specific Application Proxy application, revealing access mappings.

**Command** ([[commands/get-application-proxy-assigned-users-and-groups-by-object-id]]):
```powershell
Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>
```

> Replace <OBJECT-ID> with the Object ID from Step 1 or 2. This lists direct and group-based assignments.

**Expected Output**: List of assignments, e.g.,
```
UserPrincipalName          DisplayName             ObjectId
-----------------          -----------             --------
user@contoso.com           John Doe                11111111-1111-1111-1111-111111111111
group@contoso.com          Finance Admins          22222222-2222-2222-2222-222222222222
```
