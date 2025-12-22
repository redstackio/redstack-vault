---
type: procedure
description: >-
  Abuse Active Directory ACLs to force change a domain user's password and gain
  unauthorized access to the account.
verified: true
submitted: false
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Abusing Active Directory ACLs/ACEs]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/ForceChangePassword]]'
commands:
  - '[[commands/Set-Domain-User-Password-PowerShell]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Force-Change-Domain-User-Password-via-ACL-Abuse

## Summary

This procedure demonstrates how to abuse misconfigured Access Control Lists (ACLs) or Access Control Entries (ACEs) in Active Directory to force change the password of a target domain user account. By modifying or leveraging existing permissions on the user object, an attacker can reset the password without knowing the original, enabling account takeover for credential access or persistence.

## Description

In Active Directory environments, user objects are protected by ACLs that define who can perform actions like password resets. If an attacker has been granted excessive permissions (e.g., via genericAll, writeDacl, or specific extended rights like "Change Password"), they can use tools like PowerView to directly set a new password. This technique targets domain-joined Windows systems and requires domain authentication with sufficient privileges. It is commonly used post-initial access to escalate control over high-value accounts, leading to lateral movement or data exfiltration. Success depends on prior reconnaissance to identify permissive ACLs, and it leaves audit logs of password changes that can be monitored.

## Requirements

1. Domain authentication with an account that has ACL permissions on the target user object (e.g., ChangePassword extended right or ownership).
2. PowerView module loaded in a PowerShell session (typically via Import-Module PowerView).
3. Network access to a Domain Controller (ports 445/TCP for LDAP/SMB).
4. Target Windows domain environment (Active Directory).

## Defense

- Implement least privilege: Regularly audit and tighten ACLs on user objects using tools like BloodHound or AD auditing to remove unnecessary permissions.
- Enable advanced auditing for directory service changes and monitor Event IDs 4724 (password reset) and 5136 (directory service object modification).
- Use protected users group for high-privilege accounts to prevent password changes without admin approval.
- Deploy just-in-time administration and privileged access workstations to limit exposure.

## Objectives

1. Identify and abuse permissive ACLs on a target user account to reset its password.
2. Gain unauthorized access to the compromised account for further operations like resource access or persistence.
3. Verify the password change without alerting the user or triggering immediate detection.

## Instructions

### Step 1: Verify ACL Permissions on Target User

**Context**: Before attempting a password change, confirm that your current account has the necessary permissions on the target user object. This step uses PowerView to query ACLs and ensures the attack is feasible, avoiding unnecessary noise.

Use PowerView's Get-DomainObjectAcl to enumerate permissions:

**Command** ([[commands/Get-Domain-Object-Acl-PowerShell]]):
```powershell
Get-DomainObjectAcl -Identity TargetUser | Select-Object -ExpandProperty AclEntries | ?{$_.SecurityIdentifier -match $env:USERNAME}
```

> This command retrieves ACL entries for the target user and filters for your account's SID. It explains the rights granted, such as GenericAll or ExtendedRight for password changes. If no relevant ACEs appear, the attack cannot proceed without further privilege escalation.

**Expected Output**: A list of ACEs showing permissions like "Change Password" or "Reset Password" for your SID.

### Step 2: Prepare Secure Password String

**Context**: Convert the new password into a secure string format required by Active Directory cmdlets. This step isolates the password handling to prevent exposure in logs or memory.

**Command** ([[commands/Convert-To-Secure-String-PowerShell]]):
```powershell
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
```

> The ConvertTo-SecureString cmdlet creates an encrypted string object from plaintext. Use a strong, unique password here to avoid easy cracking if logs are captured. This step is necessary because AD functions expect secure strings for password operations.

**Expected Output**: A SecureString object stored in $NewPassword, verifiable with (Get-Member $NewPassword) showing type System.Security.SecureString.

### Step 3: Set the New Password on Target User

**Context**: Execute the password change using the prepared secure string. This directly modifies the user object in AD, assuming permissions from Step 1.

**Code** ([[codes/PowerShell-Set-Domain-User-Password]]):
```powershell
Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
```

> This invokes the Set-DomainUserPassword function from PowerView, which performs an LDAP modify operation to update the unicodePwd attribute. Replace 'TargetUser' with the actual username. If successful, the user's password is immediately changed on all domain controllers.

**Expected Output**: No output if successful; errors like "Access Denied" indicate insufficient permissions.

### Step 4: Verify Password Change

**Context**: Test the new credentials to confirm access and ensure no lockout or alerts were triggered. This validates the objective without further AD modifications.

Use standard PowerShell to attempt authentication:

**Command** ([[commands/Test-AD-User-Credentials-PowerShell]]):
```powershell
$Cred = New-Object System.Management.Automation.PSCredential('TargetUser', $NewPassword)
Get-WmiObject -Class Win32_ComputerSystem -ComputerName . -Credential $Cred
```

> This creates a PSCredential object and tests it against the local system (or a DC). Success confirms the password works for WMI queries, implying full account access.

**Expected Output**: WMI object details if authenticated; authentication failure otherwise.
