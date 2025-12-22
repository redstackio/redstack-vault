---
type: procedure
description: >-
  Identifies dynamic groups in Azure AD and demonstrates creating rules for
  automatic membership, which can be abused for persistence and access
  escalation using compromised credentials.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
  - '[[techniques/Create-Account|T1136 - Create Account]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Dynamic Group Membership]]'
  - azure-ad
  - persistence
commands:
  - '[[commands/Get-Azure-ADMS-Groups-Filtered-by-Dynamic-Membership]]'
  - '[[commands/Create-Azure-Dynamic-Group-Rule-for-Guest-Vendors]]'
platforms:
  - Azure
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# Abuse-Azure-Dynamic-Group-Membership-and-Guest-Vendor-Rules

## Summary

This procedure demonstrates how to discover dynamic groups in Azure Active Directory (Azure AD) and create membership rules that automatically add users based on attributes, such as guest vendor emails. Attackers with compromised credentials can abuse these features to gain persistent access to resources by defining rules that include their controlled accounts, mimicking legitimate administrative actions.

## Description

Dynamic Group Membership in Azure AD allows automatic addition or removal of users to groups based on user attributes like job title, department, or email patterns. The Guest Vendor Email Rule enables inviting external guests with specific email domains to access resources. Compromising an employee's credentials allows an attacker to enumerate existing dynamic groups for reconnaissance and create new rules to include attacker-controlled guest accounts, achieving persistence without manual group management. This is particularly effective in large environments where attribute-based access is common, and changes appear as normal automation. The technique targets Azure AD for discovery and manipulation, requiring Global Admin or Group Admin permissions.

## Requirements

1. Valid Azure AD credentials with permissions to read groups (e.g., Directory Reader) and create/modify groups (e.g., Groups Administrator).
2. Azure PowerShell module installed (AzureAD or Microsoft.Graph).
3. Access to Azure portal or PowerShell environment for rule application.
4. Compromised insider account or initial access via phishing/spearphishing.

## Defense

- Implement least privilege: Restrict group creation/modification to just-in-time admins.
- Monitor Azure AD logs for dynamic group changes via Microsoft Defender for Cloud Apps or Azure Sentinel.
- Enable MFA and Conditional Access policies to block suspicious rule modifications.
- Regularly audit dynamic group rules and membership queries for anomalies.

## Objectives

1. Discover existing dynamic groups to identify high-value access paths.
2. Create abusive rules to automatically grant access to attacker-controlled guest accounts.
3. Maintain persistent, low-detection access to Azure resources.

## Instructions

### Step 1: Enumerate Dynamic Groups

**Context**: This step discovers all Azure AD groups configured with dynamic membership, revealing potential targets for abuse. Dynamic groups update automatically based on rules, so identifying them helps attackers understand automated access controls.

**Command** ([[commands/Get-Azure-ADMS-Groups-Filtered-by-Dynamic-Membership]]):
```powershell
Get-AzureADMSGroup | Where-Object {$_.GroupTypes -eq 'DynamicMembership'}
```

> This PowerShell command retrieves all Microsoft 365 groups and filters for those with dynamic membership enabled. It uses the AzureAD module to query the tenant. Run this after connecting to Azure AD with Connect-AzureAD. If successful, it lists group IDs, names, and types, allowing attackers to target groups with sensitive permissions like RBAC roles.

### Step 2: Define Guest Vendor Email Rule for Dynamic Membership

**Context**: This step creates a rule expression to automatically add guest users with 'vendor' in their email to a dynamic group, enabling attackers to invite and include their own guest accounts for resource access. This abuses the feature to bypass manual approvals.

**Command** ([[commands/Create-Azure-Dynamic-Group-Rule-for-Guest-Vendors]]):
```powershell
(user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest")
```

> This is a dynamic membership rule expression used when creating or updating a group in Azure AD (via portal, PowerShell, or Graph API). It checks for guest users (userType='guest') with 'vendor' in alternate emails. Apply it using New-AzureADMSGroup with -MembershipRule parameter. Success grants automatic membership to matching guests, allowing persistence via invited vendor accounts. Verify by checking group membership after inviting a test guest.
