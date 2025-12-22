---
type: procedure
description: >-
  Abuse Active Directory ACLs/ACEs to gain permissions for resetting a target
  user's password, then perform the reset using rpcclient or bloodyAD.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Abusing Active Directory ACLs/ACEs]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/ForceChangePassword]]'
commands:
  - '[[commands/rpcclient-setuserinfo2-password-change]]'
  - '[[commands/bloodyad-change-password-pth]]'
platforms:
  - Windows
tools:
  - '[[tools/rpcclient]]'
  - '[[tools/bloodyAD]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Abuse-AD-ACLs-to-Reset-User-Password

## Summary

This procedure demonstrates how to abuse Active Directory ACLs/ACEs to grant an attacker the permissions needed to reset a target user's password. By modifying access control entries on the target user object or a privileged account, the attacker can then use tools like rpcclient from the Samba suite or bloodyAD to execute the password change. This technique is useful for privilege escalation and lateral movement in Active Directory environments, allowing access to sensitive resources once the new password is set.

## Description

In Active Directory, permissions are controlled through ACLs (Access Control Lists) and ACEs (Access Control Entries). An attacker with initial access to a low-privileged account can identify misconfigured ACLs that allow modification of permissions on user objects. By adding an ACE that grants 'Reset Password' rights (via the 'Change Password' extended right), the attacker can then reset the password of a target user, such as a domain admin. This can be done directly on the target user or by abusing a higher-privileged account's ACLs. Once permissions are modified, tools like rpcclient (interacting with the SAMR RPC interface) or bloodyAD (a Python-based AD manipulation tool) are used to perform the actual password reset. This method requires domain access and can bypass standard password policies if the ACL abuse grants sufficient rights. It is commonly used in red team engagements to simulate persistence or escalation in Windows domain environments.

## Requirements

1. Domain-joined system or network access to a Domain Controller (ports 445/TCP for SMB/RPC).
2. Valid credentials for an account with initial read access to AD objects (e.g., via LDAP or RPC).
3. Tools installed: Samba suite (for rpcclient) or Python with bloodyAD (for pass-the-hash scenarios).
4. Knowledge of the target user's SID or DN, and a strong new password that complies with policy.
5. For ACL modification prerequisite: Access to tools like PowerView or BloodHound to identify and set ACLs (not covered in this procedure, but assumed completed prior).

## Defense

- Implement least privilege: Restrict ACL modifications to domain admins only and audit all changes.
- Monitor AD for permission changes using tools like Microsoft ATA or custom SIEM rules on Event ID 5136 (Directory Service Changes).
- Enable Protected Users group and fine-grained password policies to limit reset capabilities.
- Use multi-factor authentication (MFA) for all accounts to prevent unauthorized access post-reset.
- Regularly audit ACLs with tools like BloodHound to identify overly permissive entries.

## Objectives

1. Gain the ability to reset target user passwords for privilege escalation.
2. Achieve lateral movement by authenticating as the target user with the new password.
3. Maintain access to sensitive domain resources controlled by the target account.

## Instructions

### Step 1: Verify Permissions and Prepare Target Details

**Context**: Before attempting the reset, confirm you have the necessary 'Reset Password' rights via prior ACL modification. Identify the target user and prepare the new password. This step ensures the environment is set up correctly.

Use domain enumeration tools (e.g., [[commands/net-user-enumerate]]) to list users and confirm the target. Why: To avoid errors from invalid targets and ensure the new password meets policy requirements.

**Expected Output**: List of domain users including the target, with no access denied errors.

### Step 2: Reset Password Using rpcclient (NTLM Authentication)

**Context**: If you have valid NTLM credentials with reset rights (gained via ACL abuse), use rpcclient to interact with the SAMR interface on the Domain Controller. This method is reliable for direct password changes without needing pass-the-hash.

**Command** ([[commands/rpcclient-setuserinfo2-password-change]]):
```bash
rpcclient -U '$_ATTACKER_USER%$_ATTACKER_PASSWORD' -W $_DOMAIN -c "setuserinfo2 $_TARGET_USER 23 $_NEW_PASSWORD"
```

> This command connects to the DC via RPC and sets the user's password using info level 23 (password change). Run from a Linux/Kali machine with Samba installed. Expected: Confirmation of successful change if permissions are correct; error if rights are insufficient.

**Expected Output**: 
```
result was OK
```

If failed: "NT_STATUS_ACCESS_DENIED" indicates insufficient ACL rights.

### Step 3: Reset Password Using bloodyAD (Pass-the-Hash)

**Context**: For scenarios where you have the hash of an account with reset rights (e.g., from prior credential dumping), use bloodyAD to perform the change over RPC. This avoids plaintext passwords and is useful in PtH attacks.

**Command** ([[commands/bloodyad-change-password-pth]]):
```bash
bloodyAD.py --host $_DC_IP -d $_DOMAIN -u $_ATTACKER_USER -p :$_ATTACKER_NTLM_HASH changePassword $_TARGET_USER $_NEW_PASSWORD
```

> This invokes the changePassword function in bloodyAD, authenticating with the provided hash. Why: PtH allows usage without cracking the hash. Run from a system with Python and bloodyAD installed. Decision point: If hash is unavailable, fall back to Step 2.

**Expected Output**: 
```
Password changed successfully for user: $_TARGET_USER
```

If failed: Authentication errors or access denied, verify hash and ACLs.

### Step 4: Verify the Reset and Test Access

**Context**: Confirm the password change took effect by attempting authentication as the target user. This validates success and allows immediate use for further actions.

Use tools like [[commands/smbclient-connect]] or Pass-the-Hash with the new credentials to test. Why: Ensures no policy blocks (e.g., must-change-password) and confirms escalation potential.

**Expected Output**: Successful authentication, e.g., SMB share access or shell.

**Success Indicators**:
- No access denied errors in command output.
- Target user authenticates with new password.
