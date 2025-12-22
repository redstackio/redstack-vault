---
id: 8ef3cdbe-8f9b-4aca-ab0e-604b2ed3993a
name: Check-AzureAD-User-Consent-Permissions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:15.120372+00:00'
updated_at: '2023-04-10T20:19:34.262374+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Internal Spearphishing|T1534 - Internal Spearphishing]]'
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Illicit Consent Grant]]'
commands:
  - '[[commands/Get-AzureADMSAuthorizationPolicy-Check-Consent]]'
platforms:
  - Azure
tools:
  - '[[tools/AzureAD-PowerShell-Module]]'
validated: true
---

# Check-AzureAD-User-Consent-Permissions

## Summary

This procedure checks the Azure Active Directory (Azure AD) authorization policy to determine if users are permitted to grant consent to applications on their own behalf. This is a key reconnaissance step in illicit consent grant attacks, where attackers assess whether they can trick users into approving malicious app permissions to access cloud resources without administrator intervention.

## Description

Illicit consent grant attacks involve social engineering victims to approve application permissions that allow attackers to access sensitive data or resources in Azure AD environments. Before attempting such an attack, verifying the consent policy is crucial: if users can consent to apps affecting only themselves, attackers can phish for approvals more easily. This procedure uses PowerShell to query the Microsoft Graph API via the AzureAD module to retrieve the permission grant policy IDs assigned to the default user role. An empty or specific policy output indicates restrictions, while the presence of permissive policies (e.g., 'Microsoft.AuthorizationPolicy.01ByDefault.Disallowed') signals vulnerability. This technique aligns with credential access and lateral movement in cloud environments, targeting Azure AD tenants.

## Requirements

1. Valid Azure AD administrator or global reader credentials with permissions to query authorization policies.
2. PowerShell environment with the AzureADPreview module installed.
3. Connectivity to Azure AD endpoints (internet access for Graph API calls).
4. Basic knowledge of PowerShell scripting and Azure AD administration.

## Defense

- Implement conditional access policies to restrict user consent to verified apps only.
- Enable Microsoft Entra ID Protection to monitor and alert on suspicious consent grants.
- Regularly audit and revoke unnecessary app permissions using Azure AD access reviews.
- Train users to recognize phishing attempts requesting app consents.

## Objectives

1. Determine if the Azure AD tenant allows users to self-consent to application permissions.
2. Identify policy configurations that enable illicit consent grant attacks.
3. Gather intelligence for planning phishing or social engineering vectors targeting user approvals.

## Instructions

### Step 1: Connect to Azure AD

**Context**: Authenticate to Azure AD using your credentials to establish a session for querying policies. This step ensures the PowerShell session has the necessary Graph API access.

**Command** ([[commands/Get-AzureADMSAuthorizationPolicy-Check-Consent]]):
```powershell
Connect-AzureAD
```

> This command prompts for login and connects to the Azure AD tenant. Expected output: Successful connection message like "Welcome to Azure AD PowerShell!" with no authentication errors.

### Step 2: Query the Authorization Policy

**Context**: Retrieve the permission grant policy IDs to check if users can consent to apps. If the output includes permissive policies or is empty (indicating default allow), the tenant is vulnerable to user-driven consent attacks.

**Command** ([[commands/Get-AzureADMSAuthorizationPolicy-Check-Consent]]):
```powershell
(Get-AzureADMSAuthorizationPolicy).PermissionGrantPolicyIdsAssignedToDefaultUserRole
```

> Run this after connecting. Expected output: A list of policy IDs (e.g., "Microsoft.AuthorizationPolicy.01ByDefault.Disallowed") or blank if users can consent by default. If blank, users can approve apps affecting themselves, facilitating attacks.
