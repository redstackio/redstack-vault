---
id: d9132d25-4309-4deb-81c9-d88cb7840d95
name: Enumerate-OUs-for-LAPS-Permissions
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T18:59:53.055904+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/Get-DomainOU-LAPS-Acls-PowerView]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
validated: true
---

# Enumerate-OUs-for-LAPS-Permissions

## Summary

This procedure enumerates Organizational Units (OUs) in an Active Directory domain to identify Local Administrator Password Solution (LAPS) artifacts, specifically checking for permissions on the ms-Mcs-AdmPwd attribute that allow reading local administrator passwords for domain-joined computers. It uses PowerView to query ACLs and detect users or groups with ReadProperty rights on LAPS-enabled OUs, enabling discovery of potential privilege escalation paths via stored credentials.

## Description

LAPS is a Microsoft solution that manages local administrator account passwords for domain-joined computers, storing the encrypted passwords in the ms-Mcs-AdmPwd attribute within the computer's AD object and the expiration time in ms-Mcs-AdmPwdExpirationTime. To access these plaintext passwords, a user must have appropriate ACL permissions on the OU containing the computer objects. This procedure focuses on enumerating OUs to find these permissions, revealing which accounts can retrieve LAPS passwords for lateral movement or privilege escalation. It is particularly useful in red team engagements targeting Windows Active Directory environments where LAPS is deployed but permissions may be misconfigured. The technique involves querying domain OUs, retrieving their ACLs, and filtering for LAPS-specific attributes with read access.

## Requirements

1. Active Directory domain access with authenticated credentials (domain user or higher).
2. PowerView PowerShell module loaded in the current session.
3. Network connectivity to a domain controller for LDAP queries.
4. PowerShell execution policy allowing script execution (Bypass or Unrestricted).

## Defense

Defensive measures and detection strategies:

- Monitor LDAP queries for Get-DomainOU and Get-DomainObjectAcl patterns using tools like Microsoft ATA or custom SIEM rules.
- Restrict ACL permissions on OUs to only necessary service accounts; audit LAPS delegation regularly with tools like BloodHound.
- Enable advanced auditing on AD objects for permission changes and access attempts to ms-Mcs-AdmPwd attributes.
- Deploy LAPS with strict delegation policies and monitor for anomalous password retrievals via event logs (Event ID 4728/4732 for group changes).

## Objectives

1. Identify OUs configured with LAPS artifacts (ms-Mcs-AdmPwd and ms-Mcs-AdmPwdExpirationTime).
2. Discover users or groups with ReadProperty permissions on LAPS attributes for potential credential access.
3. Map permission structures to assess privilege escalation risks in the domain.
4. Verify LAPS deployment and misconfigurations across the AD environment.

## Instructions

### Step 1: Load PowerView and Enumerate Domain OUs for LAPS ACLs

**Context**: This step retrieves all domain OUs and inspects their Access Control Lists (ACLs) to find entries granting ReadProperty rights on the ms-Mcs-AdmPwd attribute, which stores LAPS passwords. It resolves SIDs to names for easier analysis and identifies potential credential access points. Run this from a compromised host with domain credentials.

**Command** ([[commands/Get-DomainOU-LAPS-Acls-PowerView]]):
```powershell
Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | Where-Object {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and ($_.ActiveDirectoryRights -match 'ReadProperty')} | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_}
```

> This command chains PowerView functions to enumerate OUs, fetch ACLs, filter for LAPS-specific permissions, and add resolved identity names. If successful, it outputs ACL entries showing who can read LAPS passwords. Pipe to Format-Table or Export-Csv for better readability if needed. Decision point: If no results, LAPS may not be deployed or permissions are tightly controlled; proceed to broader AD enumeration.

### Step 2: Analyze Results for Actionable Permissions

**Context**: Review the output to identify high-value targets, such as domain admins or service accounts with LAPS read access. This helps prioritize follow-on actions like retrieving passwords with Get-DomainObject ms-Mcs-AdmPwd -Identity ComputerName.

**Command** (No specific command; use PowerShell filtering):
```powershell
$lapsAcls | Where-Object { $_.IdentityName -like '*Admin*' } | Select-Object ObjectDN, IdentityName, ActiveDirectoryRights
```

> Filter the previous results ($lapsAcls variable) for admin-related identities. Expected outcome: List of OUs and principals with LAPS access. If admin groups appear, note for escalation; otherwise, check your own permissions by running WhoAmI in the context.
