---
id: 2b9b06ca-b490-4226-8613-27673a0099fa
name: Add-Domain-Admin-to-RODC-Password-Replication-Group
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.366454+00:00'
updated_at: '2023-04-10T20:26:02.526383+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Account-Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/RODC]]'
  - '[[tags/Password Replication]]'
commands:
  - '[[commands/set-domainobject-modify-rodc-attribute]]'
tools:
  - '[[tools/PowerSploit]]'
platforms:
  - Windows
  - Active Directory
validated: true
---

# Add-Domain-Admin-to-RODC-Password-Replication-Group

## Summary

This procedure modifies the Read-Only Domain Controller (RODC) object in Active Directory to add a Domain Admin account to its msDS-RevealOnDemandGroup attribute. By doing so, it forces the RODC to cache the Domain Admin's password hash, enabling offline authentication and facilitating privilege escalation or lateral movement in environments where writable domain controllers are unavailable, such as remote sites with limited connectivity.

## Description

In Active Directory environments with RODCs deployed for branch offices or low-bandwidth locations, RODCs are designed to cache credentials only for allowed users and groups to minimize security risks. The msDS-RevealOnDemandGroup attribute controls which accounts' passwords can be replicated to the RODC on demand. An attacker with sufficient privileges (e.g., Domain Admin or delegated rights on the RODC object) can use PowerSploit's Set-DomainObject cmdlet to append the Domain Admin's distinguished name (DN) to this attribute. Once set, the RODC will replicate the Domain Admin's credentials, allowing the attacker to perform pass-the-hash attacks or authenticate as the Domain Admin even when the RODC is isolated from writable DCs. This technique is particularly effective in hybrid or distributed AD setups and can lead to full domain compromise if not monitored.

## Requirements

1. Authenticated access to the domain with privileges to modify the RODC computer object (e.g., Domain Admin or equivalent rights on the RODC$ object).
2. PowerSploit module loaded in a PowerShell session on a domain-joined Windows machine.
3. Knowledge of the RODC's computer name (e.g., RODC$) and the target Domain Admin's DN (e.g., CN=Administrator,CN=Users,DC=domain,DC=local).
4. Network connectivity to a domain controller for LDAP operations.

## Defense

- Restrict modification rights on RODC objects using explicit ACLs, denying Domain Admins unnecessary write access to msDS-RevealOnDemandGroup.
- Enable advanced auditing for directory service changes on RODCs and monitor for unauthorized attribute modifications using tools like Microsoft Advanced Threat Analytics or SIEM integrations.
- Regularly review and audit membership of RODC password replication groups via PowerShell or ADUC.
- Deploy RODCs with minimal allowed replication groups and use Protected Users group for high-privilege accounts to prevent caching.

## Objectives

1. Force the RODC to cache the Domain Admin's password hash for offline use.
2. Enable pass-the-hash or credential-based lateral movement from the RODC.
3. Escalate privileges in isolated network segments.

## Instructions

### Step 1: Load PowerSploit and Verify Access

**Context**: Ensure the PowerSploit module is imported and you have the necessary permissions to query and modify the RODC object. This step confirms your session can interact with Active Directory.

Run the following to import PowerSploit:

```powershell
import-module PowerSploit
```

Then, verify the RODC object exists and your access:

**Command** ([[commands/get-domainobject-rodc-query]]):

```powershell
Get-DomainObject -Identity RODC$
```

> This queries the RODC computer object and displays its current attributes, including msDS-RevealOnDemandGroup. If you see the object details without errors, proceed. If access is denied, elevate privileges.

### Step 2: Modify the msDS-RevealOnDemandGroup Attribute

**Context**: Append the Domain Admin's DN to the RODC's msDS-RevealOnDemandGroup to allow password replication. This uses the existing Allowed RODC Password Replication Group and adds the Administrator explicitly.

**Code** ([[codes/PowerShell-Set-RODC-RevealOnDemandGroup]]):

```ps1
PowerSploit> Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
```

**Command** ([[commands/set-domainobject-modify-rodc-attribute]]):

```powershell
Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
```

> This command updates the attribute with an array containing the default group and the Administrator DN. Replace 'domain.local' with your actual domain. Expected output is a confirmation message like 'The object was modified successfully.' If the attribute already includes the entry, it will be updated without error.

### Step 3: Verify the Modification

**Context**: Confirm the change took effect by requerying the RODC object to check the updated attribute.

**Command** ([[commands/get-domainobject-rodc-query]]):

```powershell
Get-DomainObject -Identity RODC$ -Properties msDS-RevealOnDemandGroup
```

> Look for the msDS-RevealOnDemandGroup attribute in the output; it should now list the Allowed RODC Password Replication Group and the Administrator DN. This verifies the replication policy has been altered.

### Step 4: Trigger Password Replication and Extract Credentials

**Context**: Force replication to cache the password and then extract it using DCSync or similar techniques for further exploitation.

Use a tool like Mimikatz or PowerView to request replication:

```powershell
Get-DomainObject -Identity RODC$ | Select-Object -ExpandProperty msDS-RevealOnDemandGroup
```

> If successful, proceed to credential dumping procedures. Monitor for replication events in AD logs to confirm.
