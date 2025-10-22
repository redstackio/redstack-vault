---
id: af40e63e-2ab4-4407-ab1c-6ff2ea23b0a7
name: Dynamic Group Membership and Guest Vendor Email Rule
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.793925+00:00'
updated_at: '2023-04-10T20:19:31.722778+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Cloud - Azure]]'
- '[[Dynamic Group Membership]]'
commands:
- '[[Filter Azure AD groups by Dynamic Membership]]'
- '[[Filter Users]]'
---

# Dynamic Group Membership and Guest Vendor Email Rule

## Summary

Dynamic Group Membership and Guest Vendor Email Rule are two Azure features that enable administrators to automatically manage access to resources. Dynamic Group Membership allows administrators to define rules that automatically add or remove users to a group based on attributes such as job title 

## Description

# Description

Dynamic Group Membership and Guest Vendor Email Rule are two Azure features that enable administrators to automatically manage access to resources. Dynamic Group Membership allows administrators to define rules that automatically add or remove users to a group based on attributes such as job title or department. Guest Vendor Email Rule allows administrators to create a rule that automatically invites external vendors to access resources. These features can be used by attackers to gain access to sensitive resources by compromising an employee's credentials and then using those credentials to automatically gain access to resources. This attack can be difficult to detect because it appears to be legitimate user behavior.

## Requirements

1. Valid credentials for an Azure account with the necessary permissions to create and manage dynamic groups and guest vendor email rules

## Defense

1. Implement multi-factor authentication to reduce the risk of compromised credentials

1. Monitor for suspicious activity related to the creation and modification of dynamic groups and guest vendor email rules

1. Limit the permissions of Azure accounts to only those necessary to perform their job functions

## Objectives

1. Gain access to sensitive resources in the Azure environment

1. Maintain access to the compromised environment

# Instructions

1. To retrieve a list of groups that allow dynamic membership, run the following command in Azure PowerShell:

**Code**: [[Get-AzureADMSGroup | ?{$_.GroupTypes -eq 'DynamicM]]

> This command uses the Get-AzureADMSGroup cmdlet to retrieve a list of all groups in the Azure Active Directory tenant. The command then filters the results to only include groups that have the 'DynamicMembership' GroupType attribute. Dynamic membership allows for automatic membership updates based on user or device attributes. This command can be useful for managing large groups of users or devices that require frequent updates to their membership.

**Command** ([[Filter Azure AD groups by Dynamic Membership]]):

```bash
Get-AzureADMSGroup | ?{$_.GroupTypes -eq 'DynamicMembership'}
```

2. This command is used to set up a rule that will only allow guest users with vendor email addresses to access certain resources.

**Code**: [[(user.otherMails -any (_ -contains &quot;vendor&qu]]

> The 'user.otherMails -any (_ -contains &quot;vendor&quot;)' part of the command checks if the user has any email addresses that contain the word 'vendor'. The 'user.userType -eq &quot;guest&quot;' part of the command checks if the user is a guest user. The 'and' operator combines the two conditions so that the rule will only apply if both conditions are met. This rule can be used to restrict access to resources such as vendor-specific information or vendor portals.

**Command** ([[Filter Users]]):

```bash
(user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest")
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Filter Azure AD groups by Dynamic Membership]]
- [[Filter Users]]

## Tags

- [[Cloud - Azure]]
- [[Dynamic Group Membership]]
