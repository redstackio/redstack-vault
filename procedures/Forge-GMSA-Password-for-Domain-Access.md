---
id: ebdcd7c0-2f72-4ebe-b00c-b9b8cf139ea2
name: Forge-GMSA-Password-for-Domain-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.594889+00:00'
updated_at: '2023-04-10T20:25:56.343182+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Forging Golden GMSA]]'
commands:
  - '[[commands/set-ad-service-account-managed-password-interval]]'
platforms:
  - Windows
tools: []
validated: true
---

# Forge-GMSA-Password-for-Domain-Access

## Summary

This procedure demonstrates how to manipulate the password rotation interval of a Group Managed Service Account (GMSA) in Active Directory to force a predictable password change, enabling the creation of a Golden Ticket for domain-wide authentication and execution. It targets environments where an attacker has sufficient privileges to modify GMSA attributes, allowing lateral movement and persistence without standard credential validation.

## Description

Group Managed Service Accounts (GMSAs) are domain accounts used for service authentication with automatically managed passwords rotated by the Key Distribution Center (KDC). In a 'Golden GMSA' scenario, attackers with delegated rights can alter the ManagedPasswordIntervalInDays attribute to a low value (e.g., 1 day or less) to trigger an immediate or predictable password reset. Once the new password is known or forged (via offline cracking or prediction if set to a weak value), it can be used to generate a Kerberos Golden Ticket, granting access to any domain-joined system as the GMSA. This technique is effective in mature Active Directory environments for privilege escalation and lateral movement, but requires domain admin or equivalent rights to modify service account properties. The procedure assumes the attacker has identified a suitable GMSA (e.g., one used for high-privilege services like SQL Server or IIS).

## Requirements

1. Domain-joined Windows system with Active Directory PowerShell module installed (Import-Module ActiveDirectory).
2. Valid credentials with rights to modify GMSA attributes (e.g., Domain Admin or delegated rights on the service account).
3. Knowledge of the target GMSA name (e.g., via enumeration with Get-ADServiceAccount).
4. Access to a system where the GMSA is permitted to run (GMSAs are restricted to specific computers by default).

## Defense

- Restrict modification rights on GMSA objects using fine-grained access controls; limit who can alter msDS-ManagedPasswordIntervalInDays.
- Monitor Active Directory changes via auditing (Event ID 5136 for directory service object modifications) and tools like Microsoft ATA or custom SIEM rules for GMSA attribute changes.
- Enforce least privilege: Use Protected Users group for admins and enable GMSA computer restrictions.
- Regularly review GMSA usage and rotate principals if suspicious activity is detected.

## Objectives

1. Modify the GMSA password rotation interval to enable predictable password forging.
2. Force or predict the new GMSA password for ticket generation.
3. Authenticate as the GMSA for lateral movement and code execution across the domain.
4. Establish persistence via the forged credentials.

## Instructions

### Step 1: Verify GMSA Existence and Current Settings

**Context**: Before modification, confirm the target GMSA exists and note its current password interval to understand the baseline and ensure modification rights.

**Command** ([[commands/set-ad-service-account-managed-password-interval]]):
```powershell
Get-ADServiceAccount -Identity "TargetGMSA$" -Properties msDS-ManagedPasswordIntervalInDays
```

> This retrieves the GMSA object and displays the current ManagedPasswordIntervalInDays attribute. Expected output includes the attribute value (default 30 days). If the attribute is not visible, confirm your permissions. Success is indicated by the object details without access denied errors.

### Step 2: Set Managed Password Interval to Trigger Reset

**Context**: Alter the password rotation interval to a low value (e.g., 1 day) to force the KDC to generate a new password soon. For immediate effect in testing, set to 0 if supported, though typically minimum is 1. Monitor the change via AD replication.

**Command** ([[commands/set-ad-service-account-managed-password-interval]]):
```powershell
Set-ADServiceAccount -Identity "TargetGMSA$" -ManagedPasswordIntervalInDays 1
```

> This updates the msDS-ManagedPasswordIntervalInDays attribute on the GMSA. Expected output is a confirmation message like "The command completed successfully." Verify with Get-ADServiceAccount afterward. If the interval expires, the KDC auto-rotates the password; in attack scenarios, predict or extract the new hash if you control the rotation timing.

### Step 3: Forge or Extract the New Password and Generate Golden Ticket

**Context**: After rotation, the new password is managed by KDS but can be forged if you know the algorithm or use tools to request and crack TGS tickets. Use the known/forged password with Mimikatz or Rubeus to create a Golden Ticket for domain auth.

**Command** ([[commands/set-ad-service-account-managed-password-interval]]):
```powershell
# Assuming password is forged as 'KnownPassword123'; use external tool like Rubeus for ticket
# Example: .\Rubeus.exe golden /user:TargetGMSA$ /domain:example.com /sid:S-1-5-21-... /rc4:HASH_OF_KNOWN_PASSWORD /ptt
```

> This step integrates with post-rotation tools (not a direct PowerShell command). Expected output from ticket tools is a successful ticket injection without errors. Success is confirmed by authenticating to a domain resource (e.g., \DC01\C$ access) using the GMSA identity. If rotation hasn't occurred, wait or force via domain replication events.
